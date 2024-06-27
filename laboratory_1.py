import os
import shutil
from datetime import datetime

# Ruta absoluta del fichero
file_path = os.path.abspath(__file__)

# Ruta absoluta del directorio
dir_path = os.path.dirname(file_path)

# Ruta del directorio destino
dest_dir_path = f"{dir_path}/destination"

# Contenido del directorio
content = os.listdir(dest_dir_path)

# Validar si existe un directorio en /destination
if len(content) > 0:
  # print("Existe un directorio, se procede a eliminarlo")
  dir_del = content[0]
  dir_path_del = f"{dest_dir_path}/{dir_del}"
  shutil.rmtree(dir_path_del)

# Crear el directorio (falta el nombre dinámico)
new_folder_path = f"{dest_dir_path}/some_folder"
os.mkdir(new_folder_path)

# Crear archivos
for i in range(0, 10):
  file_name = f"file_{i}.txt"
  file_path = f"{new_folder_path}/{file_name}"
  with open(file_path, "w") as file:
    content_file = f"File created at {datetime.now()}"
    file.write(content_file)