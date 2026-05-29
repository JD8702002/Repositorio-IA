# Dataset Híbrido de Reconocimiento Facial

## 📋 Descripción General

Proyecto de construcción de un dataset robusto de rostros para el entrenamiento y validación de modelos de reconocimiento facial. Combina imágenes de entorno controlado (alumnos y familiares) con imágenes de entornos silvestres (figuras públicas).

**Vencimiento del proyecto:** 5 de abril de 2026 23:59

## 🎯 Objetivos

- Crear una estructura de dataset con al menos 10 categorías distintas
- Detectar, recortar y alinear rostros automáticamente
- Aumentar el dataset mediante técnicas de transformación
- Generar un dataset listo para entrenamiento de modelos de clasificación multiclase

## 📁 Estructura del Proyecto

```
Dataset/
├── Alumno1/                    # Imágenes originales del Alumno 1
├── Alumno2/
├── Alumno3/
├── Famoso1/                    # Imágenes de referencias/famosos
├── Famoso2/
├── Famoso3/
├── procesadas/                 # Imágenes detectadas, recortadas y alineadas
│   ├── Alumno1/
│   ├── Alumno2/
│   └── ...
├── aumentadas/                 # Dataset aumentado
│   ├── Alumno1/
│   ├── Alumno2/
│   └── ...
├── procesador_rostros.py       # Script principal
├── instalar_dependencias.py    # Script de instalación
└── README.md                   # Este archivo
```

## 🚀 Instalación y Ejecución

### 1. Instalación de Dependencias

Ejecuta el script de instalación:

```bash
python instalar_dependencias.py
```

O instala manualmente:

```bash
pip install opencv-python numpy Pillow
```

### 2. Preparación de Imágenes

1. Crea una carpeta para cada categoría dentro de `Dataset/`
2. Coloca imágenes en las carpetas correspondientes:
   - `Dataset/Alumno1/foto1.jpg`, `foto2.jpg`, etc.
   - `Dataset/Alumno2/...`
   - `Dataset/Famoso1/...`

Formatos soportados: JPG, JPEG, PNG, BMP

### 3. Ejecución del Procesador

```bash
python procesador_rostros.py
```

El script realizará automáticamente:
- ✓ Detección de rostros usando Haar Cascades
- ✓ Recorte y alineación a 160x160 píxeles
- ✓ Aumentación de datos (rotación, brillo, espejo, desenfoque)
- ✓ Generación de reporte del dataset

## 📊 Procesamiento Aplicado

### 1. Detección de Rostros
- Algoritmo: Haar Cascades (OpenCV)
- Parámetros: scaleFactor=1.1, minNeighbors=5
- Tamaño mínimo: 30x30 píxeles

### 2. Recorte y Alineación
- Extrae el rostro más grande detectado
- Agrega margen del 10% alrededor del rostro
- Redimensiona a 160x160 píxeles (tamaño estándar)

### 3. Aumentación de Datos
Se aplican 4 tipos de aumentación:

| Tipo | Descripción |
|------|-------------|
| **Rotación** | Rotación aleatoria entre -15° y +15° |
| **Brillo** | Ajuste de brillo entre 0.7x y 1.3x |
| **Espejo** | Volteo horizontal para simular reflexión |
| **Desenfoque** | Desenfoque gaussiano leve |

### 4. Multiplicidad de Datos
Por cada imagen original procesada, se generan 3 versiones aumentadas, multiplicando efectivamente el dataset.

## 📈 Metodología de Adquisición

### Fase 1: Captura y Curación
- Fotografías con diversidad de expresiones
- Diferentes ángulos: frontal, 45°, perfil
- Variedad de accesorios: lentes, mascarillas, sombreros
- Condiciones de iluminación: natural, artificial, mixta

### Fase 2: Preprocesamiento
- Detección de rostros automática
- Recorte a región de interés
- Alineación a tamaño uniforme (160x160)

### Fase 3: Aumentación
- Técnicas de transformación sin captura adicional
- Multiplicación efectiva del dataset
- Mejora de robustez del modelo

### Fase 4: Salida
- Dataset estructurado listo para entrenamiento
- Imágenes procesadas normalizadas
- Versiones aumentadas disponibles

## 🎓 Composición Recomendada

|Categoría | Cantidad Mínima | Descripción |
|----------|-----------------|------------|
|Alumno1 | 10-20 | Integrante del equipo |
|Alumno2 | 10-20 | Integrante del equipo |
|Alumno3 | 10-20 | Integrante del equipo |
|Familiar1| 5-10 | Familiares (si trabajo individual)|
|Familiar2| 5-10 | Familiares (si trabajo individual)|
|Famoso1 | 20-30 | VGGFace2, LFW, CelebA, etc.|
|Famoso2 | 20-30 | Diferentes celebridades |
|Famoso3 | 20-30 | Diferentes celebridades |
|... | ... | Hasta 10+ categorías |

**Recomendación:** Mínimo 100-150 imágenes por categoría original para obtener dataset robusto después de aumentación.

## 📊 Ejemplos de Salida

Después de ejecutar el procesador:

```
============================================================
🎯 PROCESADOR DE DATASET DE RECONOCIMIENTO FACIAL
============================================================
Creando estructura del dataset...
✓ Carpeta creada: Dataset\Alumno1
✓ Carpeta creada: Dataset\Alumno2
...

📁 Procesando: Alumno1
✓ Procesada: DSC_0001.jpg
✓ Procesada: DSC_0002.jpg
   2 imagen(s) procesada(s)

🔄 Aumentando dataset (3 versiones por imagen)...
✓ 6 imagen(s) aumentada(s) creada(s)

============================================================
📊 REPORTE DEL DATASET
============================================================
Categorías: 6
Imágenes originales: 50
Imágenes procesadas: 47
Imágenes aumentadas: 141
Total de imágenes: 238
Tamaño de rostro: 160x160 píxeles
Fecha de generación: 2026-04-10 14:30:25
============================================================
```

## 🔧 Personalización

### Cambiar tamaño de rostro
Edita en `procesador_rostros.py`:
```python
procesador = ProcesadorRostros(
    ruta_dataset='Dataset',
    tamaño_rostro=(128, 128)  # Cambiar aquí
)
```

### Cambiar número de aumentaciones
```python
procesador.aumentar_dataset(num_aumentaciones=5)  # 5 versiones por imagen
```

### Agregar más categorías
```python
categorias = [
    'Alumno1', 'Alumno2', 'Alumno3',
    'Familiar1', 'Familiar2',
    'Famoso1', 'Famoso2', 'Famoso3',
    'Famoso4', 'Famoso5'
]
```

## ⚠️ Consideraciones Importantes

1. **Derechos de Imagen:** Asegúrate de tener autorización para usar todas las imágenes
2. **Privacidad:** Cumple con regulaciones de protección de datos (GDPR, CCPA, etc.)
3. **Calidad:** Imágenes de baja resolución pueden afectar la detección
4. **Diversidad:** Incluye diferentes etnias, géneros y edades
5. **Accesorios:** Varía el uso de lentes, mascarillas y sombreros

## 🐛 Solución de Problemas

### Problema: "No se detectaron rostros"
**Soluciones:**
- Verificar que la imagen sea clara y nítida
- Aumentar la resolución de la imagen
- Variar el ángulo de la foto (más frontal)
- Mejorar la iluminación

### Problema: ImportError con opencv
**Solución:**
```bash
pip install opencv-python --upgrade
```

### Problema: Carpetas no creadas
**Solución:**
- Verificar permisos de escritura en el directorio
- Crear manualmente las carpetas de categorías

## 📚 Referencias

- **OpenCV Documentation:** https://docs.opencv.org/
- **Haar Cascades:** https://github.com/opencv/opencv/tree/master/data/haarcascades
- **VGGFace2 Dataset:** https://www.robots.ox.ac.uk/~vgg/data/vgg_face2/
- **LFW Dataset:** http://vis-www.cs.umass.edu/lfw/
- **CelebA Dataset:** http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html

## 👥 Integrantes del Proyecto

Equipo: Universidad/Instituto
Proyecto: Dataset Híbrido de Reconocimiento Facial
Fecha de Vencimiento: 5 de abril de 2026 23:59

## 📝 Licencia

Este proyecto es para fines educativos.

---

**Última actualización:** 10 de abril de 2026
