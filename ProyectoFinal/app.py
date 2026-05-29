import gradio as gr
import socket
from core.capture import extract_frames
from core.vision import VisionModule
from core.nlp import NLPModule
from core.tts import TTSModule
from core.heuristics import HeuristicController

print("==== INSTANCIANDO SISTEMA COMENTARISTA IA ====")
vision_system = VisionModule()
nlp_system = NLPModule()
tts_system = TTSModule()
print("==============================================")

def process_video_pipeline(video_path, seconds_per_frame, enable_tts):
    if not video_path:
        yield "Error: Por favor carga un archivo de video válido.", None, "Error: no hay video cargado"
        return
        
    frames_data = extract_frames(video_path, seconds_per_frame=seconds_per_frame)
    controller = HeuristicController()
    narrative_logs = []
    comment_history = set()
    last_generated_audio = None
    total_frames = len(frames_data)

    if total_frames == 0:
        yield "No se pudo extraer ningún frame del video. Usa un clip corto y con un códec compatible.", None, "Error: no se extrajeron frames"
        return
    
    for index, (pil_img, timestamp) in enumerate(frames_data, start=1):
        raw_caption = vision_system.analyze_frame(pil_img)
        
        if controller.should_comment(raw_caption):
            spanish_commentary = nlp_system.generate_commentary(raw_caption)
            
            if spanish_commentary and spanish_commentary not in comment_history:
                comment_history.add(spanish_commentary)
                minutes = int(timestamp // 60)
                seconds = int(timestamp % 60)
                time_tag = f"[{minutes:02d}:{seconds:02d}]"
                
                narrative_logs.append(f"{time_tag} Evento detectado: {raw_caption}\n   IA: \"{spanish_commentary}\"\n")
                if enable_tts:
                    last_generated_audio = tts_system.text_to_speech(spanish_commentary)

        percentage = int((index / total_frames) * 100)
        status_message = f"Procesando frame {index}/{total_frames} ({percentage}%)"
        progress_text = f"{status_message}\n\n" + "\n".join(narrative_logs)
        yield progress_text, None, status_message
            
    if not narrative_logs:
        yield "El video se analizó, pero la lógica heurística determinó que no hubo cambios visuales suficientes para comentar.", None, "Análisis completado"
        return
        
    full_output_log = "\n".join(narrative_logs)
    yield full_output_log, last_generated_audio, "Análisis completado"

with gr.Blocks(title="Game AI Commentator") as app:
    with gr.Row(elem_id="top-row", variant="panel"):
        with gr.Column(scale=3):
            with gr.Column(elem_classes="card main"):
                gr.Markdown("# 🎮 Narrador IA", elem_classes="title")
                gr.Markdown("Genera reacciones en base a lo que sucede en pantalla — no interpreta audio.", elem_classes="subtitle")
                with gr.Row():
                    with gr.Column(scale=1):
                        video_input = gr.Video(label="Clip del Juego (.mp4)", sources=["upload"])
                        seconds_slider = gr.Slider(1, 10, value=6, step=1, label="Segundos por frame (mayor = menos frames y más rápido)")
                        enable_tts_checkbox = gr.Checkbox(label="Generar audio con síntesis de voz", value=False)
                        generate_btn = gr.Button("Analizar Gameplay y Narrar", elem_classes="btn-primary")
                        gr.Markdown("<div class='small'>Consejo: prueba con clips cortos (5-20s) para iterar rápido.</div>", elem_classes="small")
                    with gr.Column(scale=1):
                        # Preview area
                        preview_md = gr.Markdown("**Vista previa del clip**")
                        video_preview = gr.Video(label="Preview", interactive=False, visible=False)
                        # Status and controls
                        status_html = gr.HTML("<div class='small'>Estado: esperando</div>")

        with gr.Column(scale=2):
            with gr.Column(elem_classes="card sidebar"):
                gr.Markdown("## Resultados", elem_classes="title")
                log_output = gr.Textbox(label="Logs de Análisis y Guión de Locución", lines=18, interactive=False, elem_classes="logbox")
                audio_output = gr.Audio(label="Reproductor de Voz de la IA", type="filepath")

    # Wire actions
    def _on_upload(video):
        if video:
            return gr.update(value=video), gr.update(visible=True), gr.update(value="<div class='small'>Estado: archivo cargado</div>")
        return gr.update(), gr.update(visible=False), gr.update(value="<div class='small'>Estado: esperando</div>")

    video_input.upload(fn=_on_upload, inputs=[video_input], outputs=[video_input, video_preview, status_html])

    generate_btn.click(
        fn=process_video_pipeline,
        inputs=[video_input, seconds_slider, enable_tts_checkbox],
        outputs=[log_output, audio_output, status_html]
    )


def find_free_port(start_port=7861, end_port=7880):
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                sock.bind(("127.0.0.1", port))
                return port
            except OSError:
                continue
    raise OSError(f"No se encontró puerto libre en el rango {start_port}-{end_port}.")

if __name__ == "__main__":
    start_port = 7900
    end_port = 7920
    for port in range(start_port, end_port + 1):
        try:
            print(f"Intentando iniciar servidor en puerto {port}...")
            print(f"Si se inicia correctamente, abre http://127.0.0.1:{port} en tu navegador.")
            app.launch(share=False, server_name="0.0.0.0", server_port=port)
            # Si app.launch no levanta excepción, el servidor está corriendo hasta que se cierre.
            break
        except OSError as e:
            print(f"Puerto {port} no disponible: {e}. Probando siguiente puerto...")
            continue
    else:
        raise OSError(f"No se encontró puerto libre en el rango {start_port}-{end_port}.")