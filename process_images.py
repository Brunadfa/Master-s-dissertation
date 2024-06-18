import os
import shutil

base_dir = r"C:/Users/bruna/OneDrive - Universidade do Minho/images"
folder_num = 0  # Pasta específica que queremos iterar
folder_path = os.path.join(base_dir, str(folder_num))

if os.path.exists(folder_path):
    # Criar o diretório 'class_0' se não existir
    class_0_dir = os.path.join(folder_path, 'class_0')
    if not os.path.exists(class_0_dir):
        os.makedirs(class_0_dir)

    for filename in os.listdir(folder_path):
        # Verificar se o arquivo é uma imagem PNG
        if filename.endswith(".png"):
            # Construir o caminho completo do arquivo de origem
            src_path = os.path.join(folder_path, filename)
            # Construir o caminho completo do arquivo de destino
            dest_path = os.path.join(class_0_dir, filename)
            # Mover o arquivo para a pasta 'class_1'
            shutil.move(src_path, dest_path)
            print(f"Arquivo movido para 'class_0': {filename}")
else:
    print(f"A pasta {folder_path} não existe.")
