import os
import sys
import io

# Ruta de la carpeta a escanear
folder_path = r"C:\Users\Downloads"

# Redirigir la salida estándar a un buffer
log_buffer = io.StringIO()
sys.stdout = log_buffer

# Contador de archivos PDF
num = 0

# Verificar si la carpeta existe
if not os.path.exists(folder_path):
    print("❌ Error: La carpeta no existe.")
else:
    print("🔍 Escaneando carpeta...")
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):
            nombre_sin_extension = os.path.splitext(filename)[0]
            print(f"📄 Archivo PDF encontrado: {nombre_sin_extension}")
            num += 1
    print(f"✅ Total de archivos PDF encontrados: {num}")

# Restaurar la salida estándar
sys.stdout = sys.__stdout__

# Guardar el contenido del log en un archivo de texto
with open("log_resultados.csv", "w", encoding="utf-8") as log_file:
    log_file.write(log_buffer.getvalue())

print("📝 Log guardado en 'log_resultados.csv'")
