"""
Script para visualizar y comparar imágenes del dataset
Permite ver las imágenes originales, procesadas y aumentadas
"""

import cv2
import os
import numpy as np
from pathlib import Path


class VisualizadorDataset:
    """Clase para visualizar imágenes del dataset"""
    
    @staticmethod
    def mostrar_imagen(ruta_imagen, titulo="Imagen"):
        """
        Muestra una imagen individual
        
        Args:
            ruta_imagen (str): Ruta de la imagen
            titulo (str): Título de la ventana
        """
        imagen = cv2.imread(ruta_imagen)
        if imagen is None:
            print(f"❌ No se pudo leer: {ruta_imagen}")
            return
        
        # Redimensionar si es muy grande
        altura, ancho = imagen.shape[:2]
        if ancho > 800 or altura > 600:
            escala = min(800/ancho, 600/altura)
            imagen = cv2.resize(imagen, (int(ancho*escala), int(altura*escala)))
        
        cv2.imshow(titulo, imagen)
        print(f"Mostrando: {os.path.basename(ruta_imagen)}")
        print("Presiona cualquier tecla para cerrar...")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    @staticmethod
    def comparar_original_procesada(categoria, num_imagen=0):
        """
        Compara una imagen original con su versión procesada
        
        Args:
            categoria (str): Nombre de la categoría
            num_imagen (int): Índice de la imagen a comparar
        """
        ruta_original = os.path.join('Dataset', categoria)
        ruta_procesada = os.path.join('Dataset', 'procesadas', categoria)
        
        # Obtener archivos
        archivos_original = [f for f in os.listdir(ruta_original) 
                            if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        archivos_procesado = [f for f in os.listdir(ruta_procesada) 
                             if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        
        if not archivos_original or not archivos_procesado:
            print(f"⚠ No hay imágenes para comparar en {categoria}")
            return
        
        if num_imagen >= len(archivos_original):
            num_imagen = 0
        
        archivo_orig = archivos_original[num_imagen]
        ruta_img_original = os.path.join(ruta_original, archivo_orig)
        ruta_img_procesada = os.path.join(ruta_procesada, archivos_procesado[num_imagen])
        
        # Leer imágenes
        orig = cv2.imread(ruta_img_original)
        proc = cv2.imread(ruta_img_procesada)
        
        if orig is None or proc is None:
            print("❌ Error al leer las imágenes")
            return
        
        # Redimensionar ambas al mismo tamaño
        altura, ancho = 300, 300
        orig = cv2.resize(orig, (ancho, altura))
        proc = cv2.resize(proc, (ancho, altura))
        
        # Crear imagen comparativa
        resultado = np.hstack([orig, proc])
        
        # Agregar títulos
        cv2.putText(resultado, "ORIGINAL", (50, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(resultado, "PROCESADA", (ancho + 50, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        cv2.imshow(f"Comparación - {categoria}", resultado)
        print(f"Original: {archivo_orig}")
        print(f"Procesada: {archivos_procesado[num_imagen]}")
        print("Presiona cualquier tecla para cerrar...")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    @staticmethod
    def mostrar_galeria_categoria(carpeta, max_imagenes=9):
        """
        Muestra una galería de imágenes de una carpeta
        
        Args:
            carpeta (str): Ruta de la carpeta
            max_imagenes (int): Número máximo de imágenes a mostrar
        """
        if not os.path.exists(carpeta):
            print(f"❌ La carpeta no existe: {carpeta}")
            return
        
        archivos = [f for f in os.listdir(carpeta) 
                   if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp'))]
        
        if not archivos:
            print(f"⚠ No hay imágenes en {carpeta}")
            return
        
        archivos = archivos[:max_imagenes]
        
        # Tamaño de cada imagen en la galería
        tamaño = 150
        
        # Calcular grid
        cols = 3
        filas = (len(archivos) + cols - 1) // cols
        
        # Crear imagen en blanco
        galeria = np.ones((tamaño * filas + 20 * (filas - 1), 
                          tamaño * cols + 20 * (cols - 1), 3), dtype=np.uint8) * 255
        
        # Agregar imágenes
        for idx, archivo in enumerate(archivos):
            fila = idx // cols
            col = idx % cols
            
            ruta = os.path.join(carpeta, archivo)
            img = cv2.imread(ruta)
            
            if img is None:
                continue
            
            # Redimensionar
            img = cv2.resize(img, (tamaño, tamaño))
            
            # Calcular posición
            y_inicio = fila * (tamaño + 20)
            x_inicio = col * (tamaño + 20)
            
            # Colocar en galería
            galeria[y_inicio:y_inicio + tamaño, 
                   x_inicio:x_inicio + tamaño] = img
        
        # Mostrar
        cv2.imshow(f"Galería - {os.path.basename(carpeta)}", galeria)
        print(f"Mostrando {len(archivos)} imagen(s) de {os.path.basename(carpeta)}")
        print("Presiona cualquier tecla para cerrar...")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    @staticmethod
    def mostrar_estadisticas():
        """Muestra estadísticas del dataset"""
        print("\n" + "="*60)
        print("📊 ESTADÍSTICAS DEL DATASET")
        print("="*60)
        
        rutas = {
            'Original': os.path.join('Dataset'),
            'Procesadas': os.path.join('Dataset', 'procesadas'),
            'Aumentadas': os.path.join('Dataset', 'aumentadas')
        }
        
        for nombre, ruta in rutas.items():
            print(f"\n{nombre}:")
            print("-" * 40)
            
            if not os.path.exists(ruta):
                print("  No existe")
                continue
            
            total_imagenes = 0
            total_carpetas = 0
            
            for carpeta in os.listdir(ruta):
                ruta_carpeta = os.path.join(ruta, carpeta)
                
                if not os.path.isdir(ruta_carpeta):
                    continue
                
                archivos = [f for f in os.listdir(ruta_carpeta) 
                           if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
                
                if archivos:
                    print(f"  {carpeta}: {len(archivos)} imágenes")
                    total_imagenes += len(archivos)
                    total_carpetas += 1
            
            print(f"\n  Total: {total_imagenes} imágenes en {total_carpetas} categorías")
        
        print("\n" + "="*60)


def menu_visualizador():
    """Menú principal del visualizador"""
    while True:
        print("\n" + "="*60)
        print("🖼️  VISUALIZADOR DE DATASET")
        print("="*60)
        print("\n1. Ver galería de categoría")
        print("2. Comparar original vs procesada")
        print("3. Mostrar imagen individual")
        print("4. Ver estadísticas")
        print("5. Salir")
        print("\n" + "="*60)
        
        opcion = input("Selecciona una opción (1-5): ").strip()
        
        if opcion == '1':
            carpetas = []
            
            # Listar categorías disponibles
            if os.path.exists('Dataset'):
                for item in os.listdir('Dataset'):
                    ruta = os.path.join('Dataset', item)
                    if os.path.isdir(ruta) and item not in ['procesadas', 'aumentadas', 'backup']:
                        carpetas.append(('Original', item))
            
            if os.path.exists(os.path.join('Dataset', 'procesadas')):
                for item in os.listdir(os.path.join('Dataset', 'procesadas')):
                    carpetas.append(('Procesada', item))
            
            if os.path.exists(os.path.join('Dataset', 'aumentadas')):
                for item in os.listdir(os.path.join('Dataset', 'aumentadas')):
                    carpetas.append(('Aumentada', item))
            
            if not carpetas:
                print("⚠ No hay categorías disponibles")
                continue
            
            print("\nCategorías disponibles:")
            for idx, (tipo, nombre) in enumerate(carpetas):
                print(f"  {idx + 1}. {nombre} [{tipo}]")
            
            try:
                idx = int(input("\nSelecciona una categoría: ")) - 1
                if 0 <= idx < len(carpetas):
                    tipo, nombre = carpetas[idx]
                    if tipo == 'Original':
                        ruta = os.path.join('Dataset', nombre)
                    elif tipo == 'Procesada':
                        ruta = os.path.join('Dataset', 'procesadas', nombre)
                    else:
                        ruta = os.path.join('Dataset', 'aumentadas', nombre)
                    
                    VisualizadorDataset.mostrar_galeria_categoria(ruta)
            except (ValueError, IndexError):
                print("❌ Selección inválida")
        
        elif opcion == '2':
            categorias = []
            if os.path.exists('Dataset'):
                for item in os.listdir('Dataset'):
                    ruta = os.path.join('Dataset', item)
                    if os.path.isdir(ruta) and item not in ['procesadas', 'aumentadas', 'backup']:
                        categorias.append(item)
            
            if not categorias:
                print("⚠ No hay categorías disponibles")
                continue
            
            print("\nCategorías:")
            for idx, cat in enumerate(categorias):
                print(f"  {idx + 1}. {cat}")
            
            try:
                idx = int(input("\nSelecciona una categoría: ")) - 1
                if 0 <= idx < len(categorias):
                    VisualizadorDataset.comparar_original_procesada(categorias[idx])
            except (ValueError, IndexError):
                print("❌ Selección inválida")
        
        elif opcion == '3':
            ruta = input("Ingresa la ruta de la imagen: ").strip()
            if os.path.exists(ruta):
                VisualizadorDataset.mostrar_imagen(ruta, os.path.basename(ruta))
            else:
                print(f"❌ No se encontró: {ruta}")
        
        elif opcion == '4':
            VisualizadorDataset.mostrar_estadisticas()
        
        elif opcion == '5':
            print("\n✓ Saliendo...")
            break
        
        else:
            print("❌ Opción no válida")


if __name__ == "__main__":
    menu_visualizador()
