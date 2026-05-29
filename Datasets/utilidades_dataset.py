"""
Script de utilidad para crear estructura y descargar imágenes de ejemplo
Proporciona funciones auxiliares para preparar el dataset
"""

import os
from pathlib import Path


class UtilsDataset:
    """Clase con funciones auxiliares para el dataset"""
    
    @staticmethod
    def crear_estructura_completa(ruta_base='Dataset', num_alumnos=3, num_famosos=3):
        """
        Crea una estructura de directorios completa
        
        Args:
            ruta_base (str): Ruta base del dataset
            num_alumnos (int): Número de carpetas de alumnos
            num_famosos (int): Número de carpetas de famosos
        """
        print("="*60)
        print("📁 CREANDO ESTRUCTURA DE DIRECTORIOS")
        print("="*60)
        
        categorias = []
        
        # Crear carpetas de alumnos
        for i in range(1, num_alumnos + 1):
            categoria = f'Alumno{i}'
            categorias.append(categoria)
        
        # Crear carpetas de famosos
        for i in range(1, num_famosos + 1):
            categoria = f'Famoso{i}'
            categorias.append(categoria)
        
        # Crear directorios
        for categoria in categorias:
            ruta = os.path.join(ruta_base, categoria)
            Path(ruta).mkdir(parents=True, exist_ok=True)
            print(f"✓ {ruta}")
        
        # Crear subdirectorios especiales
        subdirs = ['procesadas', 'aumentadas', 'backup']
        for subdir in subdirs:
            ruta = os.path.join(ruta_base, subdir)
            Path(ruta).mkdir(parents=True, exist_ok=True)
            print(f"✓ {ruta}")
        
        print("\n" + "="*60)
        print(f"✓ Estructura creada con {len(categorias)} categorías")
        print("="*60)
        
        # Información para el usuario
        print("\n📝 PRÓXIMOS PASOS:")
        print("\n1. Coloca imágenes en cada carpeta:")
        for categoria in categorias[:3]:
            print(f"   - Dataset/{categoria}/foto1.jpg")
            print(f"   - Dataset/{categoria}/foto2.jpg")
        print(f"   - ... y más")
        print("\n2. Instala dependencias:")
        print("   - python instalar_dependencias.py")
        print("\n3. Ejecuta el procesador:")
        print("   - python procesador_rostros.py")
    
    @staticmethod
    def contar_imagenes(ruta_base='Dataset'):
        """
        Cuenta el número de imágenes en cada categoría
        
        Args:
            ruta_base (str): Ruta base del dataset
        """
        if not os.path.exists(ruta_base):
            print(f"❌ La ruta {ruta_base} no existe")
            return
        
        print("\n" + "="*60)
        print("📊 CONTEO DE IMÁGENES")
        print("="*60)
        
        extensiones_imagen = ('.jpg', '.jpeg', '.png', '.bmp', '.JPG', '.JPEG', '.PNG')
        total_general = 0
        
        for carpeta in sorted(os.listdir(ruta_base)):
            ruta_carpeta = os.path.join(ruta_base, carpeta)
            
            if not os.path.isdir(ruta_carpeta) or carpeta.startswith('.'):
                continue
            
            # Contar imágenes
            imagenes = [f for f in os.listdir(ruta_carpeta) 
                       if f.lower().endswith(extensiones_imagen)]
            
            if imagenes or carpeta not in ['procesadas', 'aumentadas', 'backup']:
                print(f"\n{carpeta}: {len(imagenes)} imagen(s)")
                total_general += len(imagenes)
        
        print("\n" + "-"*60)
        print(f"Total: {total_general} imagen(s)")
        print("="*60)
    
    @staticmethod
    def generar_guia_captura():
        """Genera una guía recomendada para la captura de fotos"""
        guia = """
╔════════════════════════════════════════════════════════════════╗
║         GUÍA DE CAPTURA DE FOTOS PARA EL DATASET             ║
╚════════════════════════════════════════════════════════════════╝

📸 RECOMENDACIONES DE FOTOGRAFÍA
═════════════════════════════════════════════════════════════════

1. CANTIDAD RECOMENDADA POR PERSONA
   ├─ Mínimo: 10-15 fotos por categoría
   ├─ Recomendado: 20-30 fotos por categoría
   └─ Óptimo: 50+ fotos por categoría

2. VARIEDAD DE ÁNGULOS
   ├─ Frontal (0°)
   ├─ Semi-perfil derecho (30-45°)
   ├─ Semi-perfil izquierdo (-30-45°)
   ├─ Perfil derecho (90°)
   └─ Perfil izquierdo (-90°)

3. VARIEDAD DE EXPRESIONES
   ├─ Cara neutral
   ├─ Sonrisa natural
   ├─ Sonrisa abierta
   ├─ Ceño fruncido
   └─ Con movimiento de cabeza

4. VARIEDAD DE ACCESORIOS
   ├─ Sin gafas
   ├─ Con gafas
   ├─ Con mascarilla
   ├─ Con sombrero/gorro
   ├─ Con bufanda
   └─ Diferentes combinaciones

5. VARIEDAD DE ILUMINACIÓN
   ├─ Luz natural (mañana)
   ├─ Luz natural (tarde)
   ├─ Luz artificial frontal
   ├─ Luz artificial lateral
   ├─ Contraluz suave
   └─ Iluminación mixta

6. VARIEDAD DE FONDOS
   ├─ Fondo neutro (pared blanca)
   ├─ Fondo común (interiores)
   ├─ Fondo exterior
   ├─ Fondo natural (parque)
   └─ Fondo con objetos

7. CALIDAD TÉCNICA
   ├─ Resolución: Mínimo 400x400 píxeles
   ├─ Formato: JPG o PNG
   ├─ Exposición: Correcta (no muy oscura ni muy clara)
   ├─ Enfoque: Nítido en el rostro
   ├─ Sin movimiento: Foto estática
   └─ Proporción: Rostro occupa 30-70% de la imagen

8. DISTANCIA RECOMENDADA
   ├─ Distancia: 30 cm a 1.5 metros
   ├─ Encuadre: Desde hombros en adelante
   └─ Espacio negativo: 20-30% alrededor del rostro

9. CONSIDERACIONES ESPECIALES
   ├─ Evitar: imágenes pixeladas o de baja calidad
   ├─ Evitar: rostros parcialmente cortados
   ├─ Evitar: exceso de maquillaje no natural
   ├─ Permitir: transpiracion natural, cicatrices, marcas
   └─ Permitir: diversidad de etnias y características

10. ESTRUCTURA DE NOMBRADO
    ├─ Usar nombres descriptivos
    │  Ej: foto_frontal_natural.jpg
    │      foto_perfil_gafas_artificial.jpg
    │      foto_sonrisa_sombrero.jpg
    │
    └─ O nombres secuenciales
       Ej: 001.jpg, 002.jpg, 003.jpg, ...

╔════════════════════════════════════════════════════════════════╗
║  💡 CONSEJO: Más diversidad = Mejor modelo entrenado           ║
║      Dedica tiempo a recopilar imágenes de calidad            ║
╚════════════════════════════════════════════════════════════════╝
"""
        return guia
    
    @staticmethod
    def mostrar_menu_utilidades():
        """Muestra un menú con utilidades disponibles"""
        print("\n" + "="*60)
        print("🛠️  UTILIDADES DEL DATASET")
        print("="*60)
        print("\n1. Crear estructura de directorios")
        print("2. Contar imágenes en el dataset")
        print("3. Mostrar guía de captura de fotos")
        print("4. Salir")
        print("\n" + "="*60)
        
        opcion = input("Selecciona una opción (1-4): ").strip()
        
        if opcion == '1':
            try:
                num_alumnos = int(input("¿Cuántos alumnos? (default: 3): ") or "3")
                num_famosos = int(input("¿Cuántos famosos? (default: 3): ") or "3")
                UtilsDataset.crear_estructura_completa(
                    num_alumnos=num_alumnos,
                    num_famosos=num_famosos
                )
            except ValueError:
                print("❌ Entrada inválida")
        
        elif opcion == '2':
            UtilsDataset.contar_imagenes()
        
        elif opcion == '3':
            print(UtilsDataset.generar_guia_captura())
        
        elif opcion == '4':
            print("\n✓ Saliendo...")
        
        else:
            print("❌ Opción no válida")


def main():
    """Función principal"""
    utils = UtilsDataset()
    utils.mostrar_menu_utilidades()


if __name__ == "__main__":
    main()
