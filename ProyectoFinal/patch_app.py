from pathlib import Path
p = Path('app.py')
text = p.read_text(encoding='utf-8')
new_text = text.replace(
    'if __name__ == "__main__":\n    app.launch(share=True, server_port=7861)',
    'if __name__ == "__main__":\n    # Lanzar con share=True para generar URL pública temporal y usar puerto 7861\n    app.launch(share=True, server_port=7861, css=CSS)'
)
if new_text == text:
    raise SystemExit('No replacement made')
p.write_text(new_text, encoding='utf-8')
print('patch applied')
