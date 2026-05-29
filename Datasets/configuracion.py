"""
Archivo de configuración para el procesador de rostros
Personaliza aquí los parámetros sin modificar el código principal
"""

# ════════════════════════════════════════════════════════════════════════════
# CONFIGURACIÓN GENERAL
# ════════════════════════════════════════════════════════════════════════════

# Ruta base del dataset
RUTA_DATASET = 'Dataset'

# Tamaño objetivo para rostros procesados (ancho, alto)
TAMAÑO_ROSTRO = (160, 160)

# Crear backup automático antes de procesar
CREAR_BACKUP = True

# Registrar detalles de procesamiento
REGISTRAR_DETALLES = True


# ════════════════════════════════════════════════════════════════════════════
# CONFIGURACIÓN DE DETECCIÓN DE ROSTROS
# ════════════════════════════════════════════════════════════════════════════

# Parámetros para detectMultiScale (Haar Cascades)
DETECTOR_CONFIG = {
    'scaleFactor': 1.1,      # Factor de escala (1.05-1.4)
    'minNeighbors': 5,        # Mínimo de vecinos (4-8)
    'minSize': (30, 30),      # Tamaño mínimo de rostro
    'maxSize': (500, 500),    # Tamaño máximo de rostro
}

# Margen alrededor del rostro detectado (proporción)
MARGEN_ROSTRO = 0.1

# Si hay múltiples rostros, usar:
# 'mayor' = el rostro más grande
# 'central' = el rostro más cercano al centro
ROSTRO_SELECCION = 'mayor'


# ════════════════════════════════════════════════════════════════════════════
# CONFIGURACIÓN DE AUMENTACIÓN DE DATOS
# ════════════════════════════════════════════════════════════════════════════

# Número de versiones aumentadas por cada imagen procesada
NUM_AUMENTACIONES = 3

# Tipos de aumentaciones a aplicar
TIPOS_AUMENTACION = [
    'rotacion',      # Rotación aleatoria
    'brillo',        # Ajuste de brillo
    'espejo',        # Volteo horizontal
    'desenfoque',    # Desenfoque gaussiano
]

# Parámetros de aumentación
AUMENTACION_CONFIG = {
    'rotacion': {
        'angulo_min': -15,      # Grados
        'angulo_max': 15,       # Grados
    },
    'brillo': {
        'factor_min': 0.7,      # Reducir brillo
        'factor_max': 1.3,      # Aumentar brillo
    },
    'espejo': {
        'enable': True,          # Habilitar espejo
    },
    'desenfoque': {
        'kernel_size': 3,        # Tamaño del kernel (3, 5, 7, ...)
    },
}


# ════════════════════════════════════════════════════════════════════════════
# CONFIGURACIÓN DE SALIDA
# ════════════════════════════════════════════════════════════════════════════

# Calidad de las imágenes JPEG (0-100, 100=máxima calidad)
CALIDAD_JPEG = 95

# Formato de salida
FORMATO_SALIDA = '.jpg'  # '.jpg', '.png'

# Nombre de subdirectorios de salida
NOMBRE_INICIO_PROCESADAS = 'procesadas'
NOMBRE_INICIO_AUMENTADAS = 'aumentadas'


# ════════════════════════════════════════════════════════════════════════════
# CATEGORÍAS DEL DATASET
# ════════════════════════════════════════════════════════════════════════════

# Lista de categorías (cambiar según necesidad)
CATEGORIAS = [
    'Alumno1',
    'Alumno2',
    'Alumno3',
    'Famoso1',
    'Famoso2',
    'Famoso3',
    'Famoso4',
    'Famoso5',
]

# O generar automáticamente:
# CATEGORIAS = [f'Alumno{i}' for i in range(1, 4)] + [f'Famoso{i}' for i in range(1, 6)]


# ════════════════════════════════════════════════════════════════════════════
# CONFIGURACIÓN DE LOGGING
# ════════════════════════════════════════════════════════════════════════════

# Niveles: 'DEBUG', 'INFO', 'WARNING', 'ERROR'
NIVEL_LOG = 'INFO'

# Guardar log en archivo
GUARDAR_LOG = True
ARCHIVO_LOG = 'procesamiento.log'

# Mostrar barra de progreso
MOSTRAR_PROGRESO = True


# ════════════════════════════════════════════════════════════════════════════
# CONFIGURACIÓN AVANZADA
# ════════════════════════════════════════════════════════════════════════════

# Extensiones de imagen soportadas
EXTENSIONES_IMAGEN = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif')

# Tamaño mínimo de imagen en bytes (0 = sin límite)
TAMAÑO_MIN_IMAGEN_KB = 10

# Tamaño máximo de imagen en bytes (0 = sin límite)
TAMAÑO_MAX_IMAGEN_KB = 50000

# Número de hilos para procesamiento paralelo (0 = sin paralelismo)
NUM_HILOS = 0

# Modo seguro: preguntar antes de sobrescribir archivos
MODO_SEGURO = True

# Validar integridad de imágenes antes de procesar
VALIDAR_IMAGENES = True


# ════════════════════════════════════════════════════════════════════════════
# FUNCIONES DE UTILIDAD
# ════════════════════════════════════════════════════════════════════════════

def obtener_config():
    """Retorna la configuración actual como diccionario"""
    return {
        'RUTA_DATASET': RUTA_DATASET,
        'TAMAÑO_ROSTRO': TAMAÑO_ROSTRO,
        'NUM_AUMENTACIONES': NUM_AUMENTACIONES,
        'DETECTOR_CONFIG': DETECTOR_CONFIG,
        'AUMENTACION_CONFIG': AUMENTACION_CONFIG,
        'CATEGORIAS': CATEGORIAS,
    }


def mostrar_config():
    """Muestra la configuración actual"""
    print("\n" + "="*60)
    print("⚙️  CONFIGURACIÓN ACTUAL")
    print("="*60)
    print(f"Dataset: {RUTA_DATASET}")
    print(f"Tamaño de rostro: {TAMAÑO_ROSTRO[0]}x{TAMAÑO_ROSTRO[1]}")
    print(f"Aumentaciones por imagen: {NUM_AUMENTACIONES}")
    print(f"Categorías: {len(CATEGORIAS)}")
    for cat in CATEGORIAS:
        print(f"  - {cat}")
    print("="*60)


if __name__ == "__main__":
    mostrar_config()
