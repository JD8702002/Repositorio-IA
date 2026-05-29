"""
Generador de imágenes de prueba
Crea imágenes de prueba automáticas para demostración del sistema
"""

import cv2
import numpy as np
import os
from pathlib import Path


class GeneradorImagenesPrueba:
    """Crea imágenes de prueba para demostración"""
    
    @staticmethod
    def crear_rostro_sintetico(ancho=400, alto=400):
        """
        Crea un rostro sintético simple para pruebas
        
        Returns:
            imagen con forma de rostro
        """
        # Crear imagen en blanco
        imagen = np.ones((alto, ancho, 3), dtype=np.uint8) * 200
        
        # Dibujar "cara"
        # Cara (círculo grande)
        cv2.circle(imagen, (ancho//2, alto//2), 120, (180, 150, 120), -1)
        
        # Ojos
        cv2.circle(imagen, (ancho//2 - 50, alto//2 - 40), 20, (50, 50, 50), -1)
        cv2.circle(imagen, (ancho//2 + 50, alto//2 - 40), 20, (50, 50, 50), -1)
        
        # Pupilas
        cv2.circle(imagen, (ancho//2 - 50, alto//2 - 40), 10, (0, 0, 0), -1)
        cv2.circle(imagen, (ancho//2 + 50, alto//2 - 40), 10, (0, 0, 0), -1)
        
        # Nariz
        pts = np.array([[ancho//2, alto//2], 
                       [ancho//2 - 15, alto//2 + 30],
                       [ancho//2 + 15, alto//2 + 30]], np.int32)
        cv2.polylines(imagen, [pts], True, (100, 80, 60), 2)
        
        # Boca
        cv2.ellipse(imagen, (ancho//2, alto//2 + 70), (40, 20), 0, 0, 180, (100, 50, 50), 2)
        
        return imagen
    
    @staticmethod
    def generar_variantes_del_rostro(rostro_base, num_variantes=10):
        """
        Genera variantes del mismo rostro con diferentes transformaciones
        
        Args:
            rostro_base: Imagen base del rostro
            num_variantes: Número de variantes a generar
            
        Returns:
            lista de imágenes modificadas
        """
        variantes = [rostro_base]
        
        h, w = rostro_base.shape[:2]
        centro = (w//2, h//2)
        
        for i in range(1, num_variantes):
            copia = rostro_base.copy()
            
            if i % 4 == 1:
                # Rotación
                angulo = np.random.uniform(-15, 15)
                matriz = cv2.getRotationMatrix2D(centro, angulo, 1.0)
                copia = cv2.warpAffine(copia, matriz, (w, h), 
                                      borderMode=cv2.BORDER_CONSTANT, 
                                      borderValue=(200, 200, 200))
            
            elif i % 4 == 2:
                # Cambio de brillo
                factor = np.random.uniform(0.7, 1.3)
                copia = cv2.convertScaleAbs(copia, alpha=factor, beta=0)
            
            elif i % 4 == 3:
                # Ruido
                ruido = np.random.normal(0, 10, copia.shape)
                copia = np.clip(copia + ruido, 0, 255).astype(np.uint8)
            
            else:
                # Espejo
                copia = cv2.flip(copia, 1)
            
            variantes.append(copia)
        
        return variantes
    
    @staticmethod
    def generar_dataset_prueba(ruta_dataset='Dataset', categorias=None, 
                              imagenes_por_categoria=15):
        """
        Genera un dataset de prueba automático
        
        Args:
            ruta_dataset (str): Ruta del dataset
            categorias (list): Categorías a crear (si es None, usa default)
            imagenes_por_categoria (int): Cantidad de imágenes por categoría
        """
        if categorias is None:
            categorias = ['Alumno1', 'Alumno2', 'Alumno3', 
                         'Famoso1', 'Famoso2', 'Famoso3']
        
        print("="*60)
        print("🎨 GENERADOR DE DATASET DE PRUEBA")
        print("="*60)
        print(f"\nGenerando {len(categorias)} categorías con")
        print(f"{imagenes_por_categoria} imágenes cada una...")
        print()
        
        generador = GeneradorImagenesPrueba()
        
        for categoria in categorias:
            ruta_categoria = os.path.join(ruta_dataset, categoria)
            Path(ruta_categoria).mkdir(parents=True, exist_ok=True)
            
            # Crear rostro base
            rostro_base = generador.crear_rostro_sintetico()
            
            # Generar variantes
            variantes = generador.generar_variantes_del_rostro(
                rostro_base, 
                imagenes_por_categoria
            )
            
            # Guardar imágenes
            for idx, variante in enumerate(variantes):
                nombre_archivo = os.path.join(
                    ruta_categoria, 
                    f"{categoria}_prueba_{idx:03d}.jpg"
                )
                cv2.imwrite(nombre_archivo, variante)
            
            print(f"✓ {categoria}: {len(variantes)} imágenes generadas")
        
        print("\n" + "="*60)
        print("✓ Dataset de prueba generado exitosamente")
        print("="*60)
        print("\nPróximos pasos:")
        print("1. Ejecuta: python procesador_rostros.py")
        print("2. O accede a través del menú principal")
        print()


def menu_generador():
    """Menú del generador de pruebas"""
    print("\n" + "="*60)
    print("🎨 GENERADOR DE DATASET DE PRUEBA")
    print("="*60)
    
    print("\n1. Generar dataset de prueba (estructura completa)")
    print("2. Generar dataset mínimo (solo 3 categorías)")
    print("3. Generar una sola categoría")
    print("4. Ver instrucciones")
    print("5. Salir")
    print("\n" + "="*60)
    
    opcion = input("\nSelecciona una opción (1-5): ").strip()
    
    if opcion == '1':
        GeneradorImagenesPrueba.generar_dataset_prueba(
            imagenes_por_categoria=15
        )
    
    elif opcion == '2':
        GeneradorImagenesPrueba.generar_dataset_prueba(
            categorias=['Alumno1', 'Alumno2', 'Famoso1'],
            imagenes_por_categoria=10
        )
    
    elif opcion == '3':
        nombre = input("\nIngresa el nombre de la categoría: ").strip()
        if nombre:
            GeneradorImagenesPrueba.generar_dataset_prueba(
                categorias=[nombre],
                imagenes_por_categoria=10
            )
    
    elif opcion == '4':
        mostrar_instrucciones()
    
    elif opcion == '5':
        print("\n✓ Saliendo...")
    
    else:
        print("❌ Opción no válida")


def mostrar_instrucciones():
    """Muestra instrucciones de uso"""
    instrucciones = """
╔════════════════════════════════════════════════════════════════╗
║          GENERADOR DE DATASET DE PRUEBA - INSTRUCCIONES       ║
╚════════════════════════════════════════════════════════════════╝

📋 ¿QUÉ ES UN DATASET DE PRUEBA?
═════════════════════════════════════════════════════════════════
Un conjunto de imágenes sintéticas generadas automáticamente para:
  ✓ Probar el sistema sin capturar fotos reales
  ✓ Demostrar el funcionamiento
  ✓ Hacer debugging antes de datos reales
  ✓ Entrenamiento de prueba rápido

🎯 CARACTERÍSTICAS
═════════════════════════════════════════════════════════════════
  • Genera automáticamente rostros sintéticos
  • Crea variantes con rotación, brillo, ruido
  • Genera múltiples imágenes por categoría
  • Listo para usar con el procesador

🚀 PASOS
═════════════════════════════════════════════════════════════════
1. Ejecuta este script
2. Elige "Generar dataset de prueba"
3. Las imágenes se crearán automáticamente
4. Procesa con: python procesador_rostros.py
5. Visualiza con: python visualizador_dataset.py

💡 VENTAJAS
═════════════════════════════════════════════════════════════════
  ✓ No requiere captura de fotos
  ✓ Reproducible exactamente
  ✓ Perfecto para testing
  ✓ Genera variantes automáticamente
  ✓ Proceso muy rápido

⚠️  NOTA
═════════════════════════════════════════════════════════════════
Las imágenes generadas son solo para PRUEBAS. Para un dataset
real, captura fotografías auténticas de personas.

═════════════════════════════════════════════════════════════════
    
"""
    print(instrucciones)


if __name__ == "__main__":
    menu_generador()
