import os

folder_path = r"C:\Users\Downloads"
num = 1

for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        num += 1

print(f'Total PDF: {num}')