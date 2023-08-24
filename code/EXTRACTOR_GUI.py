# 1-Se procede con importar las librerías necesarias para que el programa funcione adecuadamente
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract

# 2-Se procede con configurar la ubicación de Tesseract OCR (asegúrate de que esté instalado en tu sistema)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#3-Se definen las variables globales para almacenar la imagen y el texto extraído
image_path = None
extracted_text = ""

# 4-Se crea una función para cargar la imagen y mostrarla en la interfaz gráfica - (para saber que es lo que se está mostrando)
def load_image():
    global image_path
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])#formatos admitidos para extraer imágenes que contengan texto
    if file_path:
        image_path = file_path
        image = Image.open(file_path)
        image.thumbnail((300, 300))  # Se redimensiona la imagen para mostrarla en la interfaz del programa
        img = ImageTk.PhotoImage(image)
        image_label.config(image=img)
        image_label.image = img

# 5-Se diseña una función para extraer el texto de la imagen cargada en el programa
def extract_text():
    global extracted_text
    if image_path:
        image = Image.open(image_path)
        extracted_text = pytesseract.image_to_string(image)
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, extracted_text)


# 6-Se elabora una función para exportar el texto a un archivo .txt o texto plano
def export_text():
    if extracted_text:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(extracted_text)

# 7-Se documenta una función para borrar la imagen cargada y restablecer el cuadro de texto
def clear_image():
    global image_path, extracted_text
    image_path = None
    extracted_text = ""
    image_label.config(image="")
    text_box.delete("1.0", tk.END)

# 8-Se estipulan parámetros para establecer la configuración de la interfaz gráfica
root = tk.Tk()
root.title("Data Extractor System - DES")

# 8.1 - Se desarrolla una función donde muestre el nombre del diseñador o desarrollador del programa
designer_name = "Wagner Fernandez V. - (c) 2023 v0.1"  

designer_label = tk.Label(root, text=f"Designed by {designer_name}")
designer_label.pack(pady=5)

load_button = tk.Button(root, text="1-Load image / Cargar imagen", command=load_image)
load_button.pack(pady=10)

extract_button = tk.Button(root, text="2-Extract text / Extraer texto", command=extract_text)
extract_button.pack(pady=5)

export_button = tk.Button(root, text="3-Export to .TXT / Exportar a .TXT", command=export_text)
export_button.pack(pady=5)

clear_button = tk.Button(root, text="Delete image / Borrar imagen", command=clear_image)
clear_button.pack(pady=5)

image_label = tk.Label(root)
image_label.pack(padx=10, pady=5)

text_box = tk.Text(root, wrap=tk.WORD, width=40, height=10)
text_box.pack(padx=10, pady=5)

root.mainloop()
