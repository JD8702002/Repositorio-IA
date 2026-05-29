"""
Script de prueba para detección de rostros
Permite probar la detección antes de procesar el dataset completo
"""

import cv2
import os
import sys
from pathlib import Path


class PruebaDeteccion:
    """Clase para pruebas de detección de rostros"""
    
    def __init__(self):
        """Inicializa el detector"""
        ruta_cascada = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        self.detector = cv2.CascadeClassifier(ruta_cascada)
        
        if self.detector.empty():
            print("❌ Error: No se pudo cargar el detector de rostros")
            sys.exit(1)
    
    def detectar_en_imagen(self, ruta_imagen, mostrar=True, guardar_resultado=False):
        """
        Detecta rostros en una imagen individual
        
        Args:
            ruta_imagen (str): Ruta de la imagen
            mostrar (bool): Mostrar la imagen con detecciones
            guardar_resultado (bool): Guardar imagen con detecciones
        
        Returns:
            tuple: (cantidad de rostros detectados, imagen procesada)
        """
        # Leer imagen
        imagen = cv2.imread(ruta_imagen)
        if imagen is None:
            print(f"❌ No se pudo leer la imagen: {ruta_imagen}")
            return 0, None
        
        # Convertir a escala de grises
        gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        
        # Detectar rostros
        rostros = self.detector.detectMultiScale(
            gris,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        
        # Copiar imagen para dibujar
        imagen_resultado = imagen.copy()
        
        # Dibujar rectángulos alrededor de los rostros detectados
        for i, (x, y, w, h) in enumerate(rostros):
            # Dibujar rectángulo
            cv2.rectangle(imagen_resultado, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            # Dibujar pequeño cuadrado en la esquina superior
            cv2.rectangle(imagen_resultado, (x, y), (x + 10, y + 10), (0, 255, 0), -1)
            
            # Mostrar número del rostro
            cv2.putText(imagen_resultado, f"Rostro {i + 1}",
                       (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        # Mostrar cantidad de rostros detectados
        cv2.putText(imagen_resultado, f"Rostros detectados: {len(rostros)}", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        # Mostrar información
        print(f"\n{'='*60}")
        print(f"📷 Imagen: {os.path.basename(ruta_imagen)}")
        print(f"{'='*60}")
        print(f"✓ Rostros detectados: {len(rostros)}")
        
        if len(rostros) > 0:
            for i, (x, y, w, h) in enumerate(rostros):
                print(f"  Rostro {i+1}: posición=({x}, {y}), tamaño={w}x{h}")
        else:
            print("⚠ No se detectaron rostros")
        
        print(f"{'='*60}")
        
        # Guardar resultado si se solicita
        if guardar_resultado:
            nombre_archivo = os.path.splitext(os.path.basename(ruta_imagen))[0]
            carpeta_salida = "pruebaDeteccion"
            os.makedirs(carpeta_salida, exist_ok=True)
            ruta_salida = os.path.join(carpeta_salida, f"prueba_deteccion_{nombre_archivo}.jpg")
            cv2.imwrite(ruta_salida, imagen_resultado)
            print(f"\n💾 Imagen guardada: {ruta_salida}")
        
        # Mostrar imagen si se solicita
        if mostrar:
            self._mostrar_imagen(imagen_resultado)
        
        return len(rostros), imagen_resultado
    
    def _mostrar_imagen(self, imagen, titulo="Detección de Rostros"):
        """
        Muestra una imagen en una ventana
        
        Args:
            imagen: imagen de OpenCV
            titulo (str): título de la ventana
        """
        # Redimensionar si es muy grande
        altura, ancho = imagen.shape[:2]
        if ancho > 800 or altura > 600:
            escala = min(800/ancho, 600/altura)
            imagen_redimensionada = cv2.resize(imagen, 
                                              (int(ancho*escala), int(altura*escala)))
        else:
            imagen_redimensionada = imagen
        
        cv2.imshow(titulo, imagen_redimensionada)
        print("\nPresiona cualquier tecla para continuar...")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    def detectar_en_carpeta(self, ruta_carpeta, mostrar=False, guardar_resultados=False):
        """
        Detecta rostros en todas las imágenes de una carpeta
        
        Args:
            ruta_carpeta (str): Ruta de la carpeta
            mostrar (bool): Mostrar cada imagen procesada
            guardar_resultados (bool): Guardar imágenes con detecciones
        
        Returns:
            dict: Resumen de detecciones
        """
        if not os.path.isdir(ruta_carpeta):
            print(f"❌ La carpeta no existe: {ruta_carpeta}")
            return None
        
        extensiones = ('.jpg', '.jpeg', '.png', '.bmp')
        imagenes = [f for f in os.listdir(ruta_carpeta) 
                   if f.lower().endswith(extensiones)]
        
        if not imagenes:
            print(f"⚠ No hay imágenes en: {ruta_carpeta}")
            return None
        
        print(f"\n🔍 Analizando {len(imagenes)} imagen(s) en {ruta_carpeta}...\n")
        
        resultados = {
            'total_imagenes': len(imagenes),
            'imagenes_con_rostros': 0,
            'total_rostros': 0,
            'detalles': []
        }
        
        for archivo in imagenes:
            ruta_imagen = os.path.join(ruta_carpeta, archivo)
            num_rostros, _ = self.detectar_en_imagen(
                ruta_imagen,
                mostrar=mostrar,
                guardar_resultado=guardar_resultados
            )
            
            if num_rostros > 0:
                resultados['imagenes_con_rostros'] += 1
                resultados['total_rostros'] += num_rostros
            
            resultados['detalles'].append({
                'archivo': archivo,
                'rostros_detectados': num_rostros
            })
        
        # Mostrar resumen
        self._mostrar_resumen(resultados, ruta_carpeta)
        
        return resultados
    
    def _mostrar_resumen(self, resultados, ruta_carpeta):
        """Muestra un resumen de los resultados"""
        print("\n" + "="*60)
        print("📊 RESUMEN DE DETECCIÓN")
        print("="*60)
        print(f"Carpeta: {ruta_carpeta}")
        print(f"Total de imágenes: {resultados['total_imagenes']}")
        print(f"Imágenes con rostros: {resultados['imagenes_con_rostros']}")
        print(f"Total de rostros detectados: {resultados['total_rostros']}")
        
        if resultados['total_imagenes'] > 0:
            porcentaje = (resultados['imagenes_con_rostros'] / resultados['total_imagenes']) * 100
            print(f"Tasa de éxito: {porcentaje:.1f}%")
        
        print("="*60)


def menu_principal():
    """Menú principal de la herramienta de prueba"""
    prueba = PruebaDeteccion()
    
    print("\n" + "="*60)
    print("🧪 HERRAMIENTA DE PRUEBA DE DETECCIÓN DE ROSTROS")
    print("="*60)
    print("\n1. Probar con una imagen individual")
    print("2. Probar con una carpeta completa")
    print("3. Probar todas las carpetas de Alumnos y Famosos")
    print("4. Salir")
    print("\n" + "="*60)
    
    opcion = input("Selecciona una opción (1-4): ").strip()
    
    if opcion == '1':
        ruta = input("Ingresa la ruta de la imagen: ").strip()
        if os.path.exists(ruta):
            mostrar = input("¿Mostrar la imagen? (s/n): ").lower() == 's'
            guardar = input("¿Guardar resultado? (s/n): ").lower() == 's'
            prueba.detectar_en_imagen(ruta, mostrar=mostrar, guardar_resultado=guardar)
        else:
            print(f"❌ No se encontró: {ruta}")
    
    elif opcion == '2':
        ruta = input("Ingresa la ruta de la carpeta: ").strip()
        if os.path.exists(ruta):
            mostrar = input("¿Mostrar imágenes? (s/n): ").lower() == 's'
            guardar = input("¿Guardar resultados? (s/n): ").lower() == 's'
            prueba.detectar_en_carpeta(ruta, mostrar=mostrar, guardar_resultados=guardar)
        else:
            print(f"❌ No se encontró: {ruta}")
    
    elif opcion == '3':
        base_dir = 'Dataset'
        if os.path.exists(base_dir):
            carpetas = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d)) and (d.startswith('Alumno') or d.startswith('Famoso'))]
            if carpetas:
                mostrar = input("¿Mostrar imágenes mientras procesa? (s/n): ").lower() == 's'
                guardar = input("¿Guardar resultados? (s/n): ").lower() == 's'
                for carpeta in carpetas:
                    ruta = os.path.join(base_dir, carpeta)
                    if os.listdir(ruta):
                        print(f"\n>>> Analizando carpeta: {ruta} <<<")
                        prueba.detectar_en_carpeta(ruta, mostrar=mostrar, guardar_resultados=guardar)
            else:
                print("⚠ No se encontraron carpetas de Alumnos o Famosos en Dataset/")
        else:
            print("⚠ No se encontró la carpeta Dataset (debes ejecutar desde la raíz del proyecto o dentro de Dataset)")
    
    elif opcion == '4':
        print("\n✓ Saliendo...")
    
    else:
        print("❌ Opción no válida")


if __name__ == "__main__":
    menu_principal()
