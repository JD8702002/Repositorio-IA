#!/usr/bin/env python3
"""
INICIADOR PRINCIPAL - Dataset de Reconocimiento Facial
Punto de entrada único para todo el proyecto
"""

import os
import sys

# Cambiar el directorio de trabajo a la carpeta de este script
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def mostrar_introduccion():
    """Muestra introducción y bienvenida"""
    introduccion = """

╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║                  🎯 DATASET DE RECONOCIMIENTO FACIAL                      ║
║                                                                            ║
║                   PROYECTO EDUCATIVO - COMPLETE Y LISTO                   ║
║                                                                            ║
║               Vencimiento: 5 de abril de 2026 - 23:59                    ║
║                         Estado: ✅ FINALIZADO                            ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝

📦 ARCHIVOS INSTALADOS EXITOSAMENTE
═════════════════════════════════════════════════════════════════════════════

✓ procesador_rostros.py         - Motor principal de procesamiento
✓ procesador_lotes.py           - Procesador optimizado por lotes
✓ prueba_deteccion.py           - Herramienta de validación
✓ visualizador_dataset.py       - Visualizador de resultados
✓ generador_pruebas.py          - Generador de imágenes sintéticas
✓ utilidades_dataset.py         - Utilidades y herramientas
✓ arranque_rapido.py            - Interfaz principal (RECOMENDADO)
✓ instalar_dependencias.py      - Instalador de dependencias
✓ configuracion.py              - Archivo de configuración
✓ indice_archivos.py            - Índice de archivos
✓ README.md                     - Documentación completa

═════════════════════════════════════════════════════════════════════════════
🚀 CÓMO EMPEZAR (3 PASOS)
═════════════════════════════════════════════════════════════════════════════

PASO 1: Instalar dependencias (PRIMERA VEZ SOLAMENTE)
───────────────────────────────────────────────────────────────
  python instalar_dependencias.py

PASO 2: Ejecutar interfaz principal  
───────────────────────────────────────────────────────────────
  python arranque_rapido.py
  
  O (alternativa - desde menú Python):
  python inicio.py

PASO 3: Seguir el menú interactivo
───────────────────────────────────────────────────────────────
  Selecciona entre múltiples opciones:
  ├─ Crear estructura de dataset
  ├─ Generar imágenes de prueba
  ├─ Procesar imágenes existentes
  ├─ Ver resultados
  └─ Acceder a herramientas avanzadas


═════════════════════════════════════════════════════════════════════════════
📚 CONTENIDO DEL PROYECTO
═════════════════════════════════════════════════════════════════════════════

El proyecto incluye:

1. PROCESAMIENTO DE IMÁGENES
   ├─ Detección de rostros con Haar Cascades
   ├─ Recorte automático a 160x160 píxeles
   ├─ Alineación de rostros
   └─ Aumentación de datos (rotation, brillo, espejo)

2. HERRAMIENTAS DE VALIDACIÓN
   ├─ Pruebas individuales de detección
   ├─ Análisis de carpetas completas
   ├─ Visualización con anotaciones
   └─ Reportes detallados

3. VISUALIZACIÓN Y ANÁLISIS
   ├─ Galerías de imágenes
   ├─ Comparación antes/después
   ├─ Estadísticas del dataset
   └─ Menús interactivos

4. GENERACIÓN DE PRUEBAS
   ├─ Rostros sintéticos automáticos
   ├─ Variantes con transformaciones
   ├─ Dataset de demostración rápido
   └─ Sin necesidad de fotos reales

═════════════════════════════════════════════════════════════════════════════
✨ CARACTERÍSTICAS PRINCIPALES
═════════════════════════════════════════════════════════════════════════════

✓ Interfaz intuitiva con menús interactivos
✓ Procesamiento automático en lotes
✓ Detección de rostros con Haar Cascades
✓ Aumentación de datos automática
✓ Generación de reportes estadísticos
✓ Visualización de resultados
✓ Generador de datos de prueba
✓ Configuración personalizable
✓ Documentación completa en español
✓ Sistema de validación de detección


═════════════════════════════════════════════════════════════════════════════
📂 ESTRUCTURA DE TRABAJO
═════════════════════════════════════════════════════════════════════════════

Dataset/                          ← DIRECTORIO PRINCIPAL
├── Alumno1/                      ← Carpetas de categorías
├── Alumno2/
├── Alumno3/
├── Famoso1/
├── Famoso2/
├── Famoso3/
├── procesadas/                   ← Resultados procesados
│   └── [automático]
└── aumentadas/                   ← Datos aumentados
    └── [automático]


═════════════════════════════════════════════════════════════════════════════
🎯 FLUJO DE TRABAJO TÍPICO
═════════════════════════════════════════════════════════════════════════════

1️⃣  python instalar_dependencias.py
    └─ Una sola vez para instalar librerías

2️⃣  python arranque_rapido.py
    └─ Interfaz principal (recomendado para empezar)

3️⃣  Crear estructura de directorios
    └─ Automático o manual

4️⃣  Agregar imágenes originales
    └─ Copiar fotos a Dataset/Alumno1, Dataset/Alumno2, etc.

5️⃣  Procesar dataset
    └─ python procesador_rostros.py
    
       O (más rápido):
       python procesador_lotes.py

6️⃣  Visualizar resultados
    └─ python visualizador_dataset.py


═════════════════════════════════════════════════════════════════════════════
⚡ ALTERNATIVAS RÁPIDAS
═════════════════════════════════════════════════════════════════════════════

SOLO QUIERO PROBAR RÁPIDO:
  1. python generador_pruebas.py  → Generar imágenes de prueba
  2. python procesador_rostros.py → Procesar
  3. python visualizador_dataset.py → Ver resultados
  
  Listo en minutos, sin necesidad de fotos reales.


TENGO MUCHAS IMÁGENES:
  1. Copiar a Dataset/categorías
  2. python procesador_lotes.py   → Procesador optimizado
  3. Ver Dataset/procesadas/
  
  Procesamiento rápido y eficiente.


NECESITO VALIDAR FOTOS:
  1. Copiar a Dataset/Alumno1 (por ejemplo)
  2. python prueba_deteccion.py
  3. Ver qué fotos se detectan bien
  4. Reemplazar malas fotos
  5. Procesar finalmente


═════════════════════════════════════════════════════════════════════════════
📖 DOCUMENTACIÓN
═════════════════════════════════════════════════════════════════════════════

Para documentación completa: Ver README.md
Para índice de archivos: python indice_archivos.py
Para configuración: Ver configuracion.py
Para ejemplos: Ver docstrings en cada archivo .py


═════════════════════════════════════════════════════════════════════════════
🔧 REQUISITOS TÉCNICOS
═════════════════════════════════════════════════════════════════════════════

Sistema operativo:  Windows, macOS, Linux
Python:            Versión 3.6+
Espacio disco:     100 MB (mínimo)
RAM:               512 MB (mínimo, 2 GB recomendado)
Conexión internet: Solo para instalación inicial

Dependencias automáticas:
  • opencv-python
  • numpy
  • Pillow (opcional)


═════════════════════════════════════════════════════════════════════════════
✅ VERIFICACIÓN DE ÉXITO
═════════════════════════════════════════════════════════════════════════════

El proyecto está listo cuando:

✓ Se ejecuta: python arranque_rapido.py
✓ Se instalan dependencias sin errores
✓ Se crea carpeta Dataset/ automáticamente
✓ Se pueden procesar imágenes
✓ Se genera Dataset/procesadas/ con resultados


═════════════════════════════════════════════════════════════════════════════
🚀 ¡LISTO PARA COMENZAR!
═════════════════════════════════════════════════════════════════════════════

Ejecuta ahora:    python arranque_rapido.py

O en terminal:    
  
  1. Primer uso:     python instalar_dependencias.py
  2. Luego siempre:  python arranque_rapido.py

═════════════════════════════════════════════════════════════════════════════

Proyecto: Dataset Híbrido de Reconocimiento Facial
Vencimiento: 5 de abril de 2026 - 23:59
Fecha de creación: 10 de abril de 2026
Versión: 1.0 - RELEASE
Estado: ✅ COMPLETO Y FUNCIONAL

═════════════════════════════════════════════════════════════════════════════
"""
    print(introduccion)


def main():
    """Función principal"""
    mostrar_introduccion()
    
    print("\n" + "="*80)
    print("¿Qué deseas hacer?")
    print("="*80)
    
    print("\n1. 🚀 Ejecutar INTERFAZ PRINCIPAL (arranque_rapido.py)")
    print("2. 📦 Instalar DEPENDENCIAS (instalar_dependencias.py)")
    print("3. 📜 Ver DOCUMENTACIÓN (README.md)")
    print("4. 📋 Ver ÍNDICE DE ARCHIVOS (indice_archivos.py)")
    print("5. ✋ Salir")
    
    print("\n" + "="*80)
    opcion = input("\nSelecciona una opción (1-5): ").strip()
    
    if opcion == '1':
        print("\nAbriendo interfaz principal...\n")
        os.system("python arranque_rapido.py")
    
    elif opcion == '2':
        print("\nInstalando dependencias...\n")
        os.system("python instalar_dependencias.py")
    
    elif opcion == '3':
        print("\nAbriendo README.md...\n")
        if os.path.exists("README.md"):
            with open("README.md", 'r', encoding='utf-8') as f:
                print(f.read())
        else:
            print("❌ README.md no encontrado")
    
    elif opcion == '4':
        print("\nAbriendo índice de archivos...\n")
        os.system("python indice_archivos.py")
    
    elif opcion == '5':
        print("\n✓ ¡Hasta luego!\n")
    
    else:
        print("\n❌ Opción no válida")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n✋ Operación cancelada")
    except Exception as e:
        print(f"\n❌ Error: {e}")
