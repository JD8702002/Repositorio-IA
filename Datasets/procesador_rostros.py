"""
Procesador de Dataset de Reconocimiento Facial
Proyecto: Dataset híbrido de rostros para reconocimiento facial
Vencimiento: 5 de abril de 2026 23:59
"""

import os
import cv2
import numpy as np
from pathlib import Path
from datetime import datetime
import shutil


class ProcesadorRostros:
    """Clase para procesar y aumentar imágenes de rostros"""
    
    def __init__(self, ruta_dataset='Dataset', tamaño_rostro=(160, 160)):
        """
        Inicializa el procesador
        
        Args:
            ruta_dataset (str): Ruta del directorio del dataset
            tamaño_rostro (tuple): Tamaño de salida de los rostros procesados
        """
        self.ruta_dataset = ruta_dataset
        self.tamaño_rostro = tamaño_rostro
        
        # Cargar cascadas para detección de rostros (Haar Cascades)
        ruta_cascada = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        self.detector_rostros = cv2.CascadeClassifier(ruta_cascada)
        
        # Crear directorio principal si no existe
        Path(self.ruta_dataset).mkdir(parents=True, exist_ok=True)
        
        # Crear subdirectorio para imágenes procesadas
        self.ruta_procesadas = os.path.join(self.ruta_dataset, 'procesadas')
        Path(self.ruta_procesadas).mkdir(parents=True, exist_ok=True)
        
        # Crear subdirectorio para aumentación
        self.ruta_aumentadas = os.path.join(self.ruta_dataset, 'aumentadas')
        Path(self.ruta_aumentadas).mkdir(parents=True, exist_ok=True)
    
    def crear_estructura_dataset(self, categorias):
        """
        Crea la estructura de carpetas para el dataset
        
        Args:
            categorias (list): Lista de nombres de categorías (alumnos y famosos)
        """
        print("Creando estructura del dataset...")
        for categoria in categorias:
            ruta_categoria = os.path.join(self.ruta_dataset, categoria)
            Path(ruta_categoria).mkdir(parents=True, exist_ok=True)
            print(f"✓ Carpeta creada: {ruta_categoria}")
    
    def detectar_rostro(self, imagen):
        """
        Detecta rostros en una imagen
        
        Args:
            imagen: imagen de OpenCV
            
        Returns:
            lista de rostros detectados (x, y, ancho, alto)
        """
        gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        rostros = self.detector_rostros.detectMultiScale(
            gris, 
            scaleFactor=1.1, 
            minNeighbors=5, 
            minSize=(30, 30)
        )
        return rostros
    
    def procesar_imagen(self, ruta_imagen, ruta_salida):
        """
        Procesa una imagen: detecta, recorta y alinea el rostro
        
        Args:
            ruta_imagen (str): Ruta de la imagen original
            ruta_salida (str): Ruta donde guardar la imagen procesada
            
        Returns:
            bool: True si se procesó correctamente
        """
        try:
            # Leer imagen
            imagen = cv2.imread(ruta_imagen)
            if imagen is None:
                print(f"✗ No se pudo leer: {ruta_imagen}")
                return False
            
            # Detectar rostros
            rostros = self.detectar_rostro(imagen)
            
            if len(rostros) == 0:
                print(f"⚠ No se detectaron rostros en: {os.path.basename(ruta_imagen)}")
                return False
            
            # Procesar el rostro más grande
            (x, y, w, h) = max(rostros, key=lambda r: r[2] * r[3])
            
            # Agregar margen
            margen = int(0.1 * min(w, h))
            x_inicio = max(0, x - margen)
            y_inicio = max(0, y - margen)
            x_fin = min(imagen.shape[1], x + w + margen)
            y_fin = min(imagen.shape[0], y + h + margen)
            
            # Recortar rostro
            rostro_recortado = imagen[y_inicio:y_fin, x_inicio:x_fin]
            
            # Redimensionar a tamaño uniforme
            rostro_procesado = cv2.resize(rostro_recortado, self.tamaño_rostro)
            
            # Guardar
            cv2.imwrite(ruta_salida, rostro_procesado)
            print(f"✓ Procesada: {os.path.basename(ruta_imagen)}")
            return True
            
        except Exception as e:
            print(f"✗ Error procesando {ruta_imagen}: {str(e)}")
            return False
    
    def aumentar_imagen(self, imagen, tipo='rotacion'):
        """
        Aplica técnicas de aumentación a una imagen
        
        Args:
            imagen: imagen de OpenCV
            tipo (str): tipo de aumentación ('rotacion', 'brillo', 'espejo')
            
        Returns:
            imagen aumentada
        """
        if tipo == 'rotacion':
            # Rotación aleatoria entre -15 y 15 grados
            angulo = np.random.uniform(-15, 15)
            h, w = imagen.shape[:2]
            centro = (w // 2, h // 2)
            matriz = cv2.getRotationMatrix2D(centro, angulo, 1.0)
            return cv2.warpAffine(imagen, matriz, (w, h))
        
        elif tipo == 'brillo':
            # Cambio de brillo
            ajuste = np.random.uniform(0.7, 1.3)
            return cv2.convertScaleAbs(imagen, alpha=ajuste, beta=0)
        
        elif tipo == 'espejo':
            # Espejo horizontal
            return cv2.flip(imagen, 1)
        
        elif tipo == 'desenfoque':
            # Desenfoque leve
            return cv2.GaussianBlur(imagen, (3, 3), 0)
        
        return imagen
    
    def procesar_carpeta(self, ruta_categoria):
        """
        Procesa todas las imágenes en una carpeta de categoría
        
        Args:
            ruta_categoria (str): Ruta de la categoría
        """
        nombre_categoria = os.path.basename(ruta_categoria)
        ruta_salida = os.path.join(self.ruta_procesadas, nombre_categoria)
        Path(ruta_salida).mkdir(parents=True, exist_ok=True)
        
        print(f"\n📁 Procesando: {nombre_categoria}")
        contador = 0
        
        # Extensiones soportadas
        extensiones = ('.jpg', '.jpeg', '.png', '.bmp')
        
        for archivo in os.listdir(ruta_categoria):
            if archivo.lower().endswith(extensiones):
                ruta_imagen = os.path.join(ruta_categoria, archivo)
                nombre_salida = f"{os.path.splitext(archivo)[0]}_procesada.jpg"
                ruta_imagen_salida = os.path.join(ruta_salida, nombre_salida)
                
                if self.procesar_imagen(ruta_imagen, ruta_imagen_salida):
                    contador += 1
        
        print(f"   {contador} imagen(s) procesada(s)")
        return contador
    
    def aumentar_dataset(self, num_aumentaciones=2):
        """
        Aplica aumentación de datos a las imágenes procesadas
        
        Args:
            num_aumentaciones (int): Número de versiones aumentadas por imagen
        """
        print(f"\n🔄 Aumentando dataset ({num_aumentaciones} versiones por imagen)...")
        
        tipos_aumentacion = ['rotacion', 'brillo', 'espejo', 'desenfoque']
        contador_total = 0
        
        for categoria in os.listdir(self.ruta_procesadas):
            ruta_categoria = os.path.join(self.ruta_procesadas, categoria)
            if not os.path.isdir(ruta_categoria):
                continue
            
            ruta_salida_categoria = os.path.join(self.ruta_aumentadas, categoria)
            Path(ruta_salida_categoria).mkdir(parents=True, exist_ok=True)
            
            for archivo in os.listdir(ruta_categoria):
                if archivo.lower().endswith(('.jpg', '.jpeg', '.png')):
                    ruta_imagen = os.path.join(ruta_categoria, archivo)
                    imagen = cv2.imread(ruta_imagen)
                    
                    if imagen is None:
                        continue
                    
                    nombre_base = os.path.splitext(archivo)[0]
                    
                    for i in range(num_aumentaciones):
                        tipo = tipos_aumentacion[i % len(tipos_aumentacion)]
                        imagen_aumentada = self.aumentar_imagen(imagen, tipo)
                        
                        nombre_salida = f"{nombre_base}_aug{i+1}_{tipo}.jpg"
                        ruta_salida = os.path.join(ruta_salida_categoria, nombre_salida)
                        cv2.imwrite(ruta_salida, imagen_aumentada)
                        contador_total += 1
        
        print(f"✓ {contador_total} imagen(s) aumentada(s) creada(s)")
    
    def generar_reporte(self):
        """Genera un reporte del estado del dataset"""
        print("\n" + "="*60)
        print("📊 REPORTE DEL DATASET")
        print("="*60)
        
        total_categorias = 0
        total_originales = 0
        total_procesadas = 0
        total_aumentadas = 0
        
        # Contar originales
        for item in os.listdir(self.ruta_dataset):
            ruta_completa = os.path.join(self.ruta_dataset, item)
            if os.path.isdir(ruta_completa) and item not in ['procesadas', 'aumentadas']:
                total_categorias += 1
                for archivo in os.listdir(ruta_completa):
                    if archivo.lower().endswith(('.jpg', '.jpeg', '.png')):
                        total_originales += 1
        
        # Contar procesadas
        if os.path.exists(self.ruta_procesadas):
            for categoria in os.listdir(self.ruta_procesadas):
                ruta = os.path.join(self.ruta_procesadas, categoria)
                if os.path.isdir(ruta):
                    total_procesadas += len([f for f in os.listdir(ruta) 
                                           if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
        
        # Contar aumentadas
        if os.path.exists(self.ruta_aumentadas):
            for categoria in os.listdir(self.ruta_aumentadas):
                ruta = os.path.join(self.ruta_aumentadas, categoria)
                if os.path.isdir(ruta):
                    total_aumentadas += len([f for f in os.listdir(ruta) 
                                           if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
        
        print(f"Categorías: {total_categorias}")
        print(f"Imágenes originales: {total_originales}")
        print(f"Imágenes procesadas: {total_procesadas}")
        print(f"Imágenes aumentadas: {total_aumentadas}")
        print(f"Total de imágenes: {total_originales + total_procesadas + total_aumentadas}")
        print(f"Tamaño de rostro: {self.tamaño_rostro[0]}x{self.tamaño_rostro[1]} píxeles")
        print(f"Fecha de generación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*60)


def main():
    """Función principal"""
    print("\n" + "="*60)
    print("🎯 PROCESADOR DE DATASET DE RECONOCIMIENTO FACIAL")
    print("="*60)
    
    # Crear instancia del procesador
    procesador = ProcesadorRostros(
        ruta_dataset='.',
        tamaño_rostro=(160, 160)
    )
    
    # Definir categorías dinámicamente
    base_dir = '.'
    categorias = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d)) and (d.startswith('Alumno') or d.startswith('Famoso'))]
    if not categorias:
        categorias = [
            'Alumno1', 'Alumno2', 'Alumno3',
            'Famoso1', 'Famoso2', 'Famoso3'
        ]
    
    # Crear estructura de directorios
    procesador.crear_estructura_dataset(categorias)
    
    # Procesar todas las categorías
    total_procesadas = 0
    for categoria in categorias:
        ruta_categoria = os.path.join(procesador.ruta_dataset, categoria)
        if os.path.exists(ruta_categoria) and os.listdir(ruta_categoria):
            total_procesadas += procesador.procesar_carpeta(ruta_categoria)
    
    if total_procesadas > 0:
        # Aplicar aumentación si hay imágenes procesadas
        procesador.aumentar_dataset(num_aumentaciones=3)
        
        # Generar reporte
        procesador.generar_reporte()
    else:
        print("\n⚠ No se encontraron imágenes para procesar.")
        print("Coloca imágenes en las carpetas de categorías (Alumno1, Alumno2, etc.)")
        print("\nEstructura esperada:")
        print("Dataset/")
        print("  ├── Alumno1/")
        print("  │   ├── foto1.jpg")
        print("  │   ├── foto2.jpg")
        print("  │   └── ...")
        print("  ├── Alumno2/")
        print("  ├── Famoso1/")
        print("  └── ...")
        
        # Generar reporte de todas formas
        procesador.generar_reporte()


if __name__ == "__main__":
    main()
