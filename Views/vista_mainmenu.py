from tkinter import *
from tkinter import messagebox

class MenuVentana:
    def __init__(self, user_rol):
        self.ventana = Tk()
        self.ventana.geometry("800x600")

        self.mostrar_mensaje_bienvenida(user_rol)

        self.ventana.mainloop()

    def mostrar_mensaje_bienvenida(self, user_rol):
        # if user_rol == 1:
        #     self.ventana.title("Menu Recepcionista")
        #     messagebox.showinfo("Bienvenida", "Bienvenido recepcionista al sistema")
        # elif user_rol == 2:
        #     self.ventana.title("Menu Veterinario")
        #     messagebox.showinfo("Bienvenida", "Bienvenido veterinario al sistema")
        # elif user_rol == 3:
        #     self.ventana.title("Menu Administrador")
        #     messagebox.showinfo("Bienvenida", "Bienvenido administrador al sistema")
        # if:z
        messagebox.showerror("Error de privilegios", "No se ha podido iniciar sesion")