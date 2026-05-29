"""
ÍNDICE Y GUÍA DE ARCHIVOS DEL PROYECTO
Dataset de Reconocimiento Facial
"""

INDICE_ARCHIVOS = """
╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║              PROYECTO: DATASET DE RECONOCIMIENTO FACIAL                  ║
║         Vencimiento: 5 de abril de 2026 - 23:59                         ║
║                                                                            ║
║              ÍNDICE COMPLETO DE ARCHIVOS Y MODULES                        ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝

📚 ESTRUCTURA DE ARCHIVOS
═════════════════════════════════════════════════════════════════════════════

ARCHIVOS PRINCIPALES
───────────────────────────────────────────────────────────────────────────

1. 🚀 arranque_rapido.py
   ├─ Descripción: Menú interactivo principal - PUNTO DE ENTRADA RECOMENDADO
   ├─ Función: Proporciona interfaz fácil para acceder a todas las herramientas
   ├─ Uso: python arranque_rapido.py
   ├─ Características:
   │  ├─ Menú principal intuitivo
   │  ├─ Verificación de dependencias automática
   │  ├─ Creación de estructura inicial
   │  ├─ Acceso a todas las herramientas
   │  └─ Sistema de ayuda integrado
   └─ Recomendado para: PRINCIPIANTES

2. ⚙️  procesador_rostros.py
   ├─ Descripción: Motor principal de procesamiento de imágenes
   ├─ Función: Detecta, recorta, alinea y aumenta imágenes
   ├─ Uso: python procesador_rostros.py
   ├─ Características:
   │  ├─ Detección de rostros (Haar Cascades)
   │  ├─ Recorte automático a 160x160 píxeles
   │  ├─ Aumentación de datos (rotación, brillo, espejo)
   │  ├─ Generación de reportes
   │  └─ Procesamiento por categorías
   └─ Recomendado para: PROCESAMIENTO PRINCIPAL

3. 📦 procesador_lotes.py
   ├─ Descripción: Procesador optimizado para múltiples categorías
   ├─ Función: Procesa lotes completos eficientemente
   ├─ Uso: python procesador_lotes.py
   ├─ Características:
   │  ├─ Procesamiento por lotes
   │  ├─ Barra de progreso
   │  ├─ Estadísticas detalladas
   │  ├─ Procesamiento de múltiples categorías
   │  └─ Optimizaciones de velocidad
   └─ Recomendado para: GRAN VOLUMEN DE DATOS

HERRAMIENTAS Y UTILIDADES
───────────────────────────────────────────────────────────────────────────

4. 🧪 prueba_deteccion.py
   ├─ Descripción: Herramienta para probar detección de rostros
   ├─ Función: Visualiza detección antes de procesar
   ├─ Uso: python prueba_deteccion.py
   ├─ Características:
   │  ├─ Prueba de imágenes individuales
   │  ├─ Prueba de carpetas completas
   │  ├─ Visualización con rectángulos
   │  ├─ Guardado de resultados
   │  └─ Resumen de detecciones
   └─ Recomendado para: VALIDAR CALIDAD DE FOTOS

5. 🖼️  visualizador_dataset.py
   ├─ Descripción: Visualizador de imágenes procesadas
   ├─ Función: Ver y comparar imágenes del dataset
   ├─ Uso: python visualizador_dataset.py
   ├─ Características:
   │  ├─ Galerías de imágenes
   │  ├─ Comparación antes/después
   │  ├─ Visualización individual
   │  ├─ Estadísticas del dataset
   │  └─ Menú interactivo
   └─ Recomendado para: REVISAR RESULTADOS

6. 🎨 generador_pruebas.py
   ├─ Descripción: Genera imágenes de prueba automáticamente
   ├─ Función: Crear dataset sintético para demostración
   ├─ Uso: python generador_pruebas.py
   ├─ Características:
   │  ├─ Generación de rostros sintéticos
   │  ├─ Variantes automáticas
   │  ├─ Múltiples categorías
   │  ├─ Rápido para testing
   │  └─ No requiere fotos reales
   └─ Recomendado para: TESTING Y DEMOSTRACIÓN

7. 🛠️  utilidades_dataset.py
   ├─ Descripción: Utilitarios generales del dataset
   ├─ Función: Tareas auxiliares de configuración
   ├─ Uso: python utilidades_dataset.py
   ├─ Características:
   │  ├─ Crear estructura de directorios
   │  ├─ Contar imágenes
   │  ├─ Guía de captura
   │  ├─ Herramientas varias
   │  └─ Menú interactivo
   └─ Recomendado para: SETUP INICIAL

8. 📦 instalar_dependencias.py
   ├─ Descripción: Instala paquetes Python requeridos
   ├─ Función: Configurar ambiente
   ├─ Uso: python instalar_dependencias.py
   ├─ Características:
   │  ├─ Instalación automática de OpenCV
   │  ├─ Instalación de NumPy
   │  ├─ Manejo de errores
   │  └─ Verificación de éxito
   └─ Recomendado para: PRIMERA VEZ

ARCHIVOS DE CONFIGURACIÓN
───────────────────────────────────────────────────────────────────────────

9. ⚙️  configuracion.py
   ├─ Descripción: Parámetros personalizables del proyecto
   ├─ Contenido:
   │  ├─ Tamaño de rostro (160x160)
   │  ├─ Parámetros de detección
   │  ├─ Configuración de aumentación
   │  ├─ Categorías del dataset
   │  └─ Parámetros avanzados
   ├─ Uso: Editar directamente o importar en scripts
   └─ Recomendado para: PERSONALIZACIÓN

DOCUMENTACIÓN
───────────────────────────────────────────────────────────────────────────

10. 📖 README.md
    ├─ Descripción: Documentación completa del proyecto
    ├─ Contenido:
    │  ├─ Descripción general
    │  ├─ Composición del dataset
    │  ├─ Metodología de adquisición
    │  ├─ Instrucciones de uso
    │  ├─ Ejemplos de salida
    │  ├─ Solución de problemas
    │  └─ Referencias
    └─ Recomendado para: ENTENDIMIENTO COMPLETO

11. 📄 GUIA_ARCHIVOS.md (Este archivo)
    └─ Descripción: Índice y descripción de todos los archivos


FLUJO DE TRABAJO RECOMENDADO
═════════════════════════════════════════════════════════════════════════════

OPCIÓN 1: BEGINNER (Principiante)
─────────────────────────────────────────────────────────────────────────
  1. python instalar_dependencias.py     ← Instalar el sistema
  2. python arranque_rapido.py            ← Menú principal
  3. Opción 1: Crear estructura
  4. Opción 2: Generar imágenes de prueba
  5. Opción 3: Procesar dataset
  6. Opción 4: Visualizar resultados

OPCIÓN 2: INTERMEDIO
─────────────────────────────────────────────────────────────────────────
  1. python instalar_dependencias.py     ← Una sola vez
  2. python utilidades_dataset.py         ← Crear estructura
  3. Copiar fotos a Dataset/Alumno1, etc.
  4. python prueba_deteccion.py           ← Validar calidad
  5. python procesador_rostros.py         ← Procesar
  6. python visualizador_dataset.py       ← Revisar

OPCIÓN 3: AVANZADO
─────────────────────────────────────────────────────────────────────────
  1. Editar configuracion.py              ← Personalizar parámetros
  2. python procesador_lotes.py           ← Procesamiento optimizado
  3. Importar en scripts personalizados   ← Automatización
  4. Integración con tu propia pipeline   ← Personalización avanzada


DEPENDENCIAS Y REQUISITOS
═════════════════════════════════════════════════════════════════════════════

REQUISITOS MÍNIMOS
───────────────────────────────────────────────────────────────────────────
  • Python 3.6 o superior
  • Windows/Mac/Linux
  • 100 MB de espacio disponible (para dataset)
  • Conexión a internet (para instalación inicial)

PAQUETES PYTHON REQUERIDOS
───────────────────────────────────────────────────────────────────────────
  • opencv-python (cv2)     - Procesamiento de imágenes
  • numpy                   - Cálculos numéricos
  • Pillow (PIL)           - Manejo de imágenes (opcional)

Se instalan automáticamente con instalar_dependencias.py


ESTRUCTURA DE DIRECTORIOS ESPERADA
═════════════════════════════════════════════════════════════════════════════

Dataset/
├── Alumno1/                    ← Fotos originales
├── Alumno2/
├── Alumno3/
├── Famoso1/
├── Famoso2/
├── Famoso3/
├── procesadas/                 ← Fotos detectadas, recortadas
│   ├── Alumno1/
│   ├── Alumno2/
│   └── ...
├── aumentadas/                 ← Fotos aumentadas
│   ├── Alumno1/
│   ├── Alumno2/
│   └── ...
└── [archivos .py]              ← Scripts de procesamiento


GUÍA RÁPIDA DE PROBLEMAS COMUNES
═════════════════════════════════════════════════════════════════════════════

❌ "ModuleNotFoundError: No module named 'cv2'"
   → Solución: python instalar_dependencias.py

❌ "No se detectaron rostros"
   → Solución 1: Mejorar iluminación de fotos
   → Solución 2: Usar prueba_deteccion.py para validar
   → Solución 3: Rostro debe ser >= 30x30 píxeles

❌ "Permission denied" (en Linux/Mac)
   → Solución: chmod +x *.py

❌ Las imágenes processadas se ven pixeladas
   → Solución: Usar imágenes de entrada más grandes

❌ Proceso muy lento
   → Solución: Usar procesador_lotes.py en lugar de procesador_rostros.py


CONTACTO Y SOPORTE
═════════════════════════════════════════════════════════════════════════════

Este proyecto es para fines educativos en reconocimiento facial.

Documentación: Ver README.md
Configuración: Ver configuracion.py
Ayuda: Ejecuta python arranque_rapido.py

═════════════════════════════════════════════════════════════════════════════

Fecha: 10 de abril de 2026
Versión: 1.0
Estado: COMPLETO Y LISTO PARA USAR

═════════════════════════════════════════════════════════════════════════════
"""


def mostrar_indice():
    """Muestra el índice de archivos"""
    print(INDICE_ARCHIVOS)


def generar_archivo_indice():
    """Genera un archivo de índice"""
    with open('INDICE_ARCHIVOS.md', 'w', encoding='utf-8') as f:
        f.write(INDICE_ARCHIVOS)
    print("✓ Archivo INDICE_ARCHIVOS.md generado")


def main():
    """Función principal"""
    print(INDICE_ARCHIVOS)
    
    print("\n" + "="*60)
    print("OPCIONES")
    print("="*60)
    print("\n1. Mostrar este índice de nuevo")
    print("2. Guardar índice en archivo (INDICE_ARCHIVOS.md)")
    print("3. Salir")
    print("\n" + "="*60)
    
    opcion = input("\nSelecciona: ").strip()
    
    if opcion == '2':
        generar_archivo_indice()
    elif opcion == '3':
        print("\n✓ Saliendo...\n")


if __name__ == "__main__":
    main()
