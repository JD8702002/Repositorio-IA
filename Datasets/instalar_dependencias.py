"""
Archivo de instalación y configuración
Ejecuta este archivo para instalar las dependencias necesarias
"""

import subprocess
import sys


def instalar_paquetes():
    """Instala los paquetes necesarios usando pip"""
    
    paquetes = [
        'opencv-python',
        'numpy',
        'Pillow'
    ]
    
    print("="*60)
    print("📦 INSTALANDO DEPENDENCIAS")
    print("="*60)
    
    for paquete in paquetes:
        print(f"\nInstalando {paquete}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", paquete])
        print(f"✓ {paquete} instalado correctamente")
    
    print("\n" + "="*60)
    print("✓ Todas las dependencias han sido instaladas")
    print("="*60)
    print("\nPuedes ejecutar el procesador con:")
    print("  python procesador_rostros.py")


if __name__ == "__main__":
    instalar_paquetes()
