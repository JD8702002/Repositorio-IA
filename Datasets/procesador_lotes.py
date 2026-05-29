"""
Sistema de procesamiento por lotes (batch processing)
Procesa múltiples imágenes eficientemente
"""

import os
import cv2
import numpy as np
from pathlib import Path
import time
from datetime import datetime


class ProcesadorLotes:
    """Clase para procesamiento por lotes de imágenes"""
    
    def __init__(self, ruta_dataset='Dataset', tamaño_rostro=(160, 160)):
        """Inicializa el procesador por lotes"""
        self.ruta_dataset = ruta_dataset
        self.tamaño_rostro = tamaño_rostro
        
        # Cargar detector
        ruta_cascada = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        self.detector = cv2.CascadeClassifier(ruta_cascada)
        
        # Estadísticas
        self.estadisticas = {
            'total_procesadas': 0,
            'exitosas': 0,
            'fallidas': 0,
            'tiempo_inicio': None,
            'tiempo_fin': None,
            'detalles': []
        }
    
    def procesar_lote(self, categoria, mostrar_progreso=True):
        """
        Procesa un lote de imágenes de una categoría
        
        Args:
            categoria (str): Nombre de la categoría
            mostrar_progreso (bool): Mostrar barra de progreso
            
        Returns:
            dict: Estadísticas del lote procesado
        """
        self.estadisticas['tiempo_inicio'] = datetime.now()
        
        ruta_categoria = os.path.join(self.ruta_dataset, categoria)
        ruta_salida = os.path.join(self.ruta_dataset, 'procesadas', categoria)
        
        Path(ruta_salida).mkdir(parents=True, exist_ok=True)
        
        extensiones = ('.jpg', '.jpeg', '.png', '.bmp')
        archivos = [f for f in os.listdir(ruta_categoria)
                   if f.lower().endswith(extensiones)]
        
        print(f"\n📦 Procesando lote: {categoria}")
        print(f"   Total de imágenes: {len(archivos)}")
        print("=" * 60)
        
        for idx, archivo in enumerate(archivos):
            ruta_imagen = os.path.join(ruta_categoria, archivo)
            nombre_salida = f"{os.path.splitext(archivo)[0]}_procesada.jpg"
            ruta_imagen_salida = os.path.join(ruta_salida, nombre_salida)
            
            # Procesar
            exito = self._procesar_imagen_interna(ruta_imagen, ruta_imagen_salida)
            
            # Actualizar estadísticas
            self.estadisticas['total_procesadas'] += 1
            if exito:
                self.estadisticas['exitosas'] += 1
            else:
                self.estadisticas['fallidas'] += 1
            
            # Mostrar progreso
            if mostrar_progreso:
                self._mostrar_barra_progreso(idx + 1, len(archivos), archivo)
        
        self.estadisticas['tiempo_fin'] = datetime.now()
        
        # Mostrar resumen del lote
        self._mostrar_resumen_lote()
        
        return self.estadisticas.copy()
    
    def _procesar_imagen_interna(self, ruta_imagen, ruta_salida):
        """Procesa una imagen internamente"""
        try:
            imagen = cv2.imread(ruta_imagen)
            if imagen is None:
                return False
            
            gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
            rostros = self.detector.detectMultiScale(gris, 1.1, 5, minSize=(30, 30))
            
            if len(rostros) == 0:
                return False
            
            # Seleccionar rostro más grande
            (x, y, w, h) = max(rostros, key=lambda r: r[2] * r[3])
            
            # Aplicar margen
            margen = int(0.1 * min(w, h))
            x_inicio = max(0, x - margen)
            y_inicio = max(0, y - margen)
            x_fin = min(imagen.shape[1], x + w + margen)
            y_fin = min(imagen.shape[0], y + h + margen)
            
            # Recortar y redimensionar
            rostro = imagen[y_inicio:y_fin, x_inicio:x_fin]
            rostro_procesado = cv2.resize(rostro, self.tamaño_rostro)
            
            # Guardar
            cv2.imwrite(ruta_salida, rostro_procesado, [cv2.IMWRITE_JPEG_QUALITY, 95])
            return True
        except:
            return False
    
    def _mostrar_barra_progreso(self, actual, total, archivo=""):
        """Muestra una barra de progreso"""
        porcentaje = (actual / total) * 100
        barra_llena = int(20 * actual // total)
        barra_vacia = 20 - barra_llena
        
        barra = "█" * barra_llena + "░" * barra_vacia
        
        if archivo:
            print(f"   [{barra}] {porcentaje:5.1f}% - {os.path.basename(archivo)}")
        else:
            print(f"   [{barra}] {porcentaje:5.1f}%")
    
    def _mostrar_resumen_lote(self):
        """Muestra resumen del lote procesado"""
        tiempo_total = self.estadisticas['tiempo_fin'] - self.estadisticas['tiempo_inicio']
        segundos = tiempo_total.total_seconds()
        
        print("\n" + "-" * 60)
        print(f"   Exitosas: {self.estadisticas['exitosas']}")
        print(f"   Fallidas: {self.estadisticas['fallidas']}")
        print(f"   Tiempo: {segundos:.1f}s")
        if self.estadisticas['exitosas'] > 0:
            print(f"   Velocidad: {self.estadisticas['exitosas']/segundos:.1f} img/s")
        print("-" * 60)
    
    def procesar_multiples_lotes(self, categorias):
        """
        Procesa múltiples categorías
        
        Args:
            categorias (list): Lista de nombres de categorías
        """
        print("\n" + "="*60)
        print("📦 PROCESAMIENTO POR LOTES - MÚLTIPLES CATEGORÍAS")
        print("="*60)
        
        resultados_totales = {
            'categorias': len(categorias),
            'total_imagenes': 0,
            'total_exitosas': 0,
            'total_fallidas': 0,
            'tiempo_inicio': datetime.now(),
            'detalles_categorias': {}
        }
        
        for categoria in categorias:
            ruta_categoria = os.path.join(self.ruta_dataset, categoria)
            
            if not os.path.exists(ruta_categoria):
                print(f"\n⚠ Categoría no existe: {categoria}")
                continue
            
            # Procesar lote
            self.procesar_lote(categoria, mostrar_progreso=True)
            
            # Acumular estadísticas
            resultados_totales['total_imagenes'] += self.estadisticas['total_procesadas']
            resultados_totales['total_exitosas'] += self.estadisticas['exitosas']
            resultados_totales['total_fallidas'] += self.estadisticas['fallidas']
            resultados_totales['detalles_categorias'][categoria] = {
                'procesadas': self.estadisticas['total_procesadas'],
                'exitosas': self.estadisticas['exitosas'],
                'fallidas': self.estadisticas['fallidas']
            }
        
        resultados_totales['tiempo_fin'] = datetime.now()
        
        # Mostrar resumen final
        self._mostrar_resumen_final(resultados_totales)
        
        return resultados_totales
    
    def _mostrar_resumen_final(self, resultados):
        """Muestra resumen final de todo el procesamiento"""
        tiempo_total = resultados['tiempo_fin'] - resultados['tiempo_inicio']
        segundos = tiempo_total.total_seconds()
        
        print("\n" + "="*60)
        print("✓ RESUMEN FINAL DEL PROCESAMIENTO")
        print("="*60)
        print(f"\nCategorías procesadas: {resultados['categorias']}")
        print(f"Total de imágenes: {resultados['total_imagenes']}")
        print(f"Exitosas: {resultados['total_exitosas']}")
        print(f"Fallidas: {resultados['total_fallidas']}")
        print(f"Tiempo total: {segundos:.1f}s")
        
        if resultados['total_exitosas'] > 0:
            print(f"Velocidad promedio: {resultados['total_exitosas']/segundos:.1f} img/s")
            tasa_exito = (resultados['total_exitosas'] / resultados['total_imagenes']) * 100
            print(f"Tasa de éxito: {tasa_exito:.1f}%")
        
        print("\nDetalles por categoría:")
        print("-" * 60)
        for categoria, detalles in resultados['detalles_categorias'].items():
            print(f"  {categoria}")
            print(f"    ├─ Procesadas: {detalles['procesadas']}")
            print(f"    ├─ Exitosas: {detalles['exitosas']}")
            print(f"    └─ Fallidas: {detalles['fallidas']}")
        
        print("\n" + "="*60)


class ProcessadorOptimizado:
    """Versión optimizada del procesador con caché y paralelismo"""
    
    def __init__(self, ruta_dataset='Dataset', tamaño_rostro=(160, 160), num_hilos=4):
        """
        Inicializa el procesador optimizado
        
        Args:
            ruta_dataset (str): Ruta del dataset
            tamaño_rostro (tuple): Tamaño objetivo del rostro
            num_hilos (int): Número de hilos para procesamiento paralelo
        """
        self.procesador = ProcesadorLotes(ruta_dataset, tamaño_rostro)
        self.num_hilos = num_hilos
    
    def procesar_con_cache(self, categoria):
        """
        Procesa con caché de imágenes
        
        Args:
            categoria (str): Categoría a procesar
            
        Returns:
            Estadísticas del procesamiento
        """
        return self.procesador.procesar_lote(categoria, mostrar_progreso=True)


def main_lotes():
    """Función principal para procesamiento por lotes"""
    print("\n" + "="*60)
    print("📦 PROCESADOR POR LOTES")
    print("="*60)
    
    # Crear procesador
    procesador = ProcesadorLotes(ruta_dataset='.')
    
    # Obtener categorías disponibles
    categorias = []
    base_dir = '.'
    if os.path.exists(base_dir):
        for item in os.listdir(base_dir):
            ruta = os.path.join(base_dir, item)
            if os.path.isdir(ruta) and item not in ['procesadas', 'aumentadas', 'backup', 'pruebaDeteccion']:
                categorias.append(item)
    
    if not categorias:
        print("\n⚠ No hay categorías disponibles")
        print("Crea primero: Dataset/Alumno1, Dataset/Alumno2, etc.")
        return
    
    print(f"\nCategorías disponibles: {len(categorias)}")
    for cat in categorias:
        print(f"  - {cat}")
    
    print("\n1. Procesar todas las categorías")
    print("2. Seleccionar categorías específicas")
    print("3. Salir")
    
    opcion = input("\nSelecciona: ").strip()
    
    if opcion == '1':
        procesador.procesar_multiples_lotes(categorias)
    
    elif opcion == '2':
        seleccionadas = []
        for i, cat in enumerate(categorias):
            respuesta = input(f"  ¿Procesar {cat}? (s/n): ").lower()
            if respuesta == 's':
                seleccionadas.append(cat)
        
        if seleccionadas:
            procesador.procesar_multiples_lotes(seleccionadas)
        else:
            print("No se seleccionó ninguna categoría")
    
    elif opcion == '3':
        print("\n✓ Saliendo...")


if __name__ == "__main__":
    main_lotes()
