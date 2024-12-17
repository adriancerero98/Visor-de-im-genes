import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Visor de Imágenes")
        self.root.geometry("600x400")

        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.btn_open = tk.Button(self.root, text="Abrir Imagen", command=self.open_image)
        self.btn_open.pack(pady=10)

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            img = Image.open(file_path)
            img.thumbnail((600, 400))  # Redimensiona la imagen
            self.img = ImageTk.PhotoImage(img)

            self.canvas.delete("all")  # Borra la imagen anterior
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageViewer(root)
    root.mainloop()
 
