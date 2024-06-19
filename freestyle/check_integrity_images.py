from PIL import Image
import os

def check_images(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                Image.open(file_path)
            except (IOError, SyntaxError):
                print(f"Arquivo inválido: {file_path}")

folder_path = "caminho/para/suas/pastas"
check_images(folder_path)