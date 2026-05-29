#!/usr/bin/env python3
"""
ARRANQUE RÁPIDO - Dataset de Reconocimiento Facial
Script de iniciación fácil para empezar rápidamente
"""

import os
import sys
import subprocess
from pathlib import Path

# Cambiar el directorio de trabajo a la carpeta de este script
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def limpiar_pantalla():
    """Limpia la pantalla del terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_banner():
    """Muestra el banner inicial"""
    banner = """
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║   🎯 DATASET DE RECONOCIMIENTO FACIAL - ARRANQUE RÁPIDO      ║
║                                                                ║
║   Proyecto: Dataset Híbrido de Rostros                       ║
║   Vencimiento: 5 de abril de 2026 - 23:59                   ║
║                                                                ║
║   Estado: LISTO PARA USAR                                    ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
"""
    print(banner)


def verificar_dependencias():
    """Verifica si todas las dependencias están instaladas"""
    print("\n📦 Verificando dependencias...\n")
    
    dependencias = ['cv2', 'numpy']
    faltantes = []
    
    for dep in dependencias:
        try:
            __import__(dep)
            print(f"✓ {dep} - OK")
        except ImportError:
            print(f"✗ {dep} - NO INSTALADO")
            faltantes.append(dep)
    
    if faltantes:
        print("\n⚠️  Faltan dependencias. Instalando...\n")
        subprocess.check_call([sys.executable, "-m", "pip", "install", 
                             "opencv-python", "numpy"])
        print("\n✓ Dependencias instaladas")
    
    return len(faltantes) == 0


def crear_estructura_inicial():
    """Crea la estructura básica del dataset"""
    print("\n📁 Preparando estructura de directorios...\n")
    
    categorias = ['Alumno1', 'Alumno2', 'Alumno3', 
                 'Famoso1', 'Famoso2', 'Famoso3']
    
    for cat in categorias:
        Path(cat).mkdir(parents=True, exist_ok=True)
        print(f"✓ {cat}")
    
    # Crear subdirectorios especiales
    Path('procesadas').mkdir(parents=True, exist_ok=True)
    Path('aumentadas').mkdir(parents=True, exist_ok=True)
    print("✓ procesadas")
    print("✓ aumentadas")


def menu_principal():
    """Menú de opciones principales"""
    limpiar_pantalla()
    mostrar_banner()
    
    # Verificar dependencias
    if not verificar_dependencias():
        print("\n❌ No se pudieron instalar las dependencias")
        return
    
    # Verificar/crear estructura
    crear_estructura_inicial()
    
    # Menú interactivo
    while True:
        print("\n" + "="*60)
        print("🚀 OPCIONES DISPONIBLES")
        print("="*60)
        print("\n1. 📋 Configurar estructura del dataset")
        print("2. 🧪 Probar detección de rostros")
        print("3. ⚙️  Procesar dataset completo")
        print("4. 🖼️  Visualizar resultados")
        print("5. 📊 Ver estadísticas")
        print("6. 📖 Leer documentación")
        print("7. 🔧 Acceso a herramientas avanzadas")
        print("8. ❌ Salir")
        print("\n" + "="*60)
        
        opcion = input("\nSelecciona una opción (1-8): ").strip()
        
        if opcion == '1':
            submenu_configuracion()
        
        elif opcion == '2':
            limpiar_pantalla()
            print("🧪 Iniciando herramienta de prueba...\n")
            try:
                subprocess.run([sys.executable, "prueba_deteccion.py"], check=False)
            except FileNotFoundError:
                print("❌ No se encontró prueba_deteccion.py")
        
        elif opcion == '3':
            limpiar_pantalla()
            print("⚙️  Iniciando procesador de dataset...\n")
            try:
                subprocess.run([sys.executable, "procesador_rostros.py"], check=False)
            except FileNotFoundError:
                print("❌ No se encontró procesador_rostros.py")
        
        elif opcion == '4':
            limpiar_pantalla()
            print("🖼️  Abriendo visualizador...\n")
            try:
                subprocess.run([sys.executable, "visualizador_dataset.py"], check=False)
            except FileNotFoundError:
                print("❌ No se encontró visualizador_dataset.py")
        
        elif opcion == '5':
            mostrar_estadisticas()
        
        elif opcion == '6':
            mostrar_documentacion()
        
        elif opcion == '7':
            submenu_herramientas()
        
        elif opcion == '8':
            print("\n✓ ¡Hasta luego!\n")
            break
        
        else:
            print("❌ Opción no válida")
        
        input("\nPresiona Enter para continuar...")


def submenu_configuracion():
    """Submenu de configuración"""
    limpiar_pantalla()
    print("\n📋 CONFIGURACIÓN DEL DATASET\n")
    print("="*60)
    
    print("\n1. Crear estructura básica (3 alumnos + 3 famosos)")
    print("2. Crear estructura personalizada")
    print("3. Ver guía de fotografía")
    print("4. Volver")
    print("\n" + "="*60)
    
    opcion = input("\nSelecciona: ").strip()
    
    if opcion == '1':
        crear_estructura_inicial()
        print("\n✓ Estructura creada")
    
    elif opcion == '2':
        try:
            subprocess.run([sys.executable, "utilidades_dataset.py"], check=False)
        except FileNotFoundError:
            print("❌ No se encontró utilidades_dataset.py")
    
    elif opcion == '3':
        try:
            subprocess.run([sys.executable, "-c", 
                          "from utilidades_dataset import UtilsDataset; print(UtilsDataset.generar_guia_captura())"],
                          check=False)
        except:
            print("⚠️  No se pudo mostrar la guía")


def submenu_herramientas():
    """Submenu de herramientas avanzadas"""
    limpiar_pantalla()
    print("\n🔧 HERRAMIENTAS AVANZADAS\n")
    print("="*60)
    
    print("\n1. Utilidades del dataset")
    print("2. Ver configuración actual")
    print("3. Instalar/Actualizar dependencias")
    print("4. Volver")
    print("\n" + "="*60)
    
    opcion = input("\nSelecciona: ").strip()
    
    if opcion == '1':
        try:
            subprocess.run([sys.executable, "utilidades_dataset.py"], check=False)
        except FileNotFoundError:
            print("❌ No se encontró utilidades_dataset.py")
    
    elif opcion == '2':
        try:
            subprocess.run([sys.executable, "configuracion.py"], check=False)
        except FileNotFoundError:
            print("❌ No se encontró configuracion.py")
    
    elif opcion == '3':
        print("\nInstalando dependencias...\n")
        try:
            subprocess.run([sys.executable, "instalar_dependencias.py"], check=False)
        except FileNotFoundError:
            print("❌ No se encontró instalar_dependencias.py")


def mostrar_estadisticas():
    """Muestra estadísticas del dataset actual"""
    limpiar_pantalla()
    print("\n" + "="*60)
    print("📊 ESTADÍSTICAS DEL DATASET")
    print("="*60)
    
    directorio_base = 'Dataset'
    
    if not os.path.exists(directorio_base):
        print("\n⚠️  El directorio Dataset no existe aún")
        return
    
    secciones = ['Dataset (Original)', 'Procesadas', 'Aumentadas']
    rutas = ['Dataset', os.path.join('Dataset', 'procesadas'), 
             os.path.join('Dataset', 'aumentadas')]
    
    total_general = 0
    total_categorias = 0
    
    for nombre, ruta in zip(secciones, rutas):
        print(f"\n{nombre}:")
        print("-" * 40)
        
        if not os.path.exists(ruta):
            print("  (No existe aún)")
            continue
        
        subtotal = 0
        for carpeta in sorted(os.listdir(ruta)):
            ruta_carpeta = os.path.join(ruta, carpeta)
            if os.path.isdir(ruta_carpeta):
                imagenes = [f for f in os.listdir(ruta_carpeta) 
                          if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
                if imagenes:
                    print(f"  {carpeta}: {len(imagenes)} imágenes")
                    subtotal += len(imagenes)
                    if nombre == 'Dataset (Original)':
                        total_categorias += 1
        
        if subtotal > 0:
            print(f"  Total: {subtotal} imágenes")
            total_general += subtotal
    
    print("\n" + "="*60)
    print(f"Resumen total: {total_general} imágenes")
    if total_categorias > 0:
        print(f"Categorías activas: {total_categorias}")
    print("="*60)


def mostrar_documentacion():
    """Muestra documentación del proyecto"""
    limpiar_pantalla()
    print("\n" + "="*60)
    print("📖 DOCUMENTACIÓN")
    print("="*60)
    
    doc = """
📚 GUÍA RÁPIDA
═══════════════════════════════════════════════════════════════

1. INICIO RÁPIDO
   ├─ Coloca fotos en Dataset/Alumno1, Dataset/Alumno2, etc.
   ├─ Ejecuta: Opción 3 (Procesar dataset)
   └─ Resultados en Dataset/procesadas y Dataset/aumentadas

2. ESTRUCTURA RECOMENDADA
   ├─ Alumno1, Alumno2, Alumno3
   ├─ Famoso1, Famoso2, Famoso3
   └─ Mínimo 10-20 fotos por categoría

3. REQUISITOS DE FOTO
   ├─ Formato: JPG, PNG, BMP
   ├─ Rostro visible y nítido
   ├─ Mínimo 400x400 píxeles
   └─ Buena iluminación

4. PROCESAMIENTO AUTOMÁTICO
   ├─ Detección de rostros (Haar Cascades)
   ├─ Recorte y alineación (160x160 píxeles)
   ├─ Aumentación de datos (rotación, brillo, espejo)
   └─ Genera múltiples versiones de cada imagen

5. SALIDA
   ├─ Dataset/procesadas/ = Imágenes normalizadas
   ├─ Dataset/aumentadas/ = Versiones aumentadas
   └─ Listo para entrenar modelos de ML

═══════════════════════════════════════════════════════════════
📝 Consulta README.md para documentación completa
═══════════════════════════════════════════════════════════════
"""
    print(doc)


def main():
    """Función principal"""
    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\n\n❌ Operación cancelada por el usuario")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
