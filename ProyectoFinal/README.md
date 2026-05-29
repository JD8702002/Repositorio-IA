# Proyecto IA

Repositorio modular para procesamiento multimodal (visión, NLP, TTS y heurísticas).

## Arquitectura

La arquitectura es intencionalmente modular y organizada en capas: un orquestador y un paquete `core` que contiene los componentes funcionales.

- **Orquestador**: [app.py](app.py) — Punto de entrada; coordina la ejecución del flujo de datos y utiliza los módulos del paquete `core`.
- **Parches / utilidades**: [patch_app.py](patch_app.py) — Scripts auxiliares para aplicar parches o ejecutar tareas ad-hoc.
- **Módulos funcionales**: `core/` — Cada archivo implementa una responsabilidad concreta:
  - [core/capture.py](core/capture.py): Adquisición de datos (audio, vídeo, imágenes, etc.).
  - [core/vision.py](core/vision.py): Procesamiento y análisis de imágenes/visión por computadora.
  - [core/nlp.py](core/nlp.py): Procesamiento de lenguaje natural y análisis de texto.
  - [core/tts.py](core/tts.py): Síntesis de voz / salida de audio.
  - [core/heuristics.py](core/heuristics.py): Lógica de decisión, reglas y heurísticas que integran salidas de otros módulos.

## Flujo de datos (resumen)

1. `capture` recoge y normaliza datos de entrada.
2. Dependiendo del tipo de dato, se llama a `vision` o `nlp` para extraer características.
3. `heuristics` combina resultados y toma decisiones sobre la salida.
4. `tts` genera salida de audio cuando aplica.
5. `app.py` orquesta y gestiona el ciclo completo.

## Cómo ejecutar

1. Instalar dependencias:

```bash
pip install -r requirements.txt
```

2. Ejecutar la aplicación:

```bash
python app.py
```

Si necesitas ejecutar tareas de parcheo o utilidades, revisa [patch_app.py](patch_app.py).

## Extender el proyecto

- Añadir nuevas capacidades: crear un nuevo módulo en `core/` y exponer una interfaz clara (p. ej. `process(data)`).
- Separar configuración sensible en variables de entorno o un archivo `config.py`.
- Añadir pruebas unitarias y de integración para cada módulo.

## Notas de diseño

- Separación de responsabilidades para facilitar pruebas y reemplazo de implementaciones (por ejemplo, cambiar modelo de `vision` sin tocar `nlp`).
- Componentes independientes permiten desplegar o escalar partes del sistema por separado.

---

Si quieres, puedo: añadir un script `run.sh`/`run.ps1`, generar un `requirements.txt` más detallado, o crear pruebas iniciales.
