from tkinter import *
from tkinter import messagebox
# from vista_recepcionista import Mostrar_Menu

def Mostrar_Menu(user_rol):
    ventana = Tk()
    ventana.geometry("800x600")

    messagebox.showinfo("Bienvenida", "Sistema sin rol")
    if user_rol == "Recepcionista":
        ventana.title("Menu Recepcionista")
        messagebox.showinfo("Bienvenida", "Bienvenido recepcionista {} al sistema")
    elif user_rol == "Veterinario":
        ventana.title("Menu Veterinario")
        messagebox.showinfo("Bienvenida", "Bienvenido veterinario {} al sistema")
    
    ventana.mainloop()