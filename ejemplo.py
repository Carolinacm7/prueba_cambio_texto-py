import tkinter as tk 

def cambiar_texto():
    label.config(text="texto cambiado")

root = tk.Tk()

root.title ("ventana con boton")

root.geometry("300x200")

label = tk.Label(root, text="texto inicial")
label.pack(pady=20)

boton = tk.Button(root, text="haz click para cambiar texto", command=cambiar_texto)

boton.pack(pady=20)

root.mainloop()