from tkinter import *
from botones.boton_ficha_vet import Mostrar_Ficha

class MenuPrincipal:
    def __init__(self):
        self.ventanaMain = Tk()
        self.ventanaMain.geometry("1024x768")
        self.font_p = ("Segoe UI", 12)

        self.frameMain = Frame(self.ventanaMain, width=200, height=768) 
        self.frameMain.pack(fill="both", expand=False, side="left")
        self.frameMain.pack_propagate(False)

        self.btnFicha = Button(self.frameMain, text="Modulo de Fichas", command=self.mostrar_modulo_fichas)
        self.btnFicha.pack(pady=10)
        self.btnFicha.place(x=40, y=75)

        self.content_frame = Frame(self.ventanaMain)
        self.content_frame.pack(side="right", fill="both", expand=True)

        self.mostrar_bienvenida()

        self.ventanaMain.mainloop()

    def mostrar_bienvenida(self):
        self.delete_frame(self.content_frame)

        lbl_Entrada = Label(self.content_frame, text="LotusPet", font=self.font_p)
        lbl_Entrada.pack(pady=15)
        
        lbl_Entrada = Label(self.content_frame, text="Para acceder a las funciones utilice los botones laterales", font=self.font_p)
        lbl_Entrada.pack()

    def mostrar_modulo_fichas(self):
        self.delete_frame(self.content_frame)
        Mostrar_Ficha(self.ventanaMain)

    def delete_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    menu = MenuPrincipal()
