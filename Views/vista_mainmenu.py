from tkinter import *
from tkinter import messagebox

class MenuVentana:
    def __init__(self, user_rol):
        self.ventana = Tk()
        self.ventana.geometry("800x600")

        self.mostrar_mensaje_bienvenida(user_rol)

        self.ventana.mainloop()

    def mostrar_mensaje_bienvenida(self, user_rol):
        messagebox.showinfo("Bienvenida", "Sistema sin rol")
        
        if user_rol == "Recepcionista":
            self.ventana.title("Menu Recepcionista")
            messagebox.showinfo("Bienvenida", "Bienvenido recepcionista {} al sistema".format(user_rol))
        elif user_rol == "Veterinario":
            self.ventana.title("Menu Veterinario")
            messagebox.showinfo("Bienvenida", "Bienvenido veterinario {} al sistema".format(user_rol))

# Ejemplo de uso:
if __name__ == "__main__":
    user_rol = "Recepcionista"  # Cambiar al rol deseado: "Recepcionista" o "Veterinario"
    menu = MenuVentana(user_rol)
