from tkinter import *
from botones.boton_ficha_vet import Mostrar_Ficha

def Mostrar_Menu():
    def DeleteFrame(ventanaMain):
        contadorFrames = ventanaMain.winfo_children()
        if len(contadorFrames) > 1:
            contadorFrames[1].destroy()

    ventanaMain = Tk()
    ventanaMain.geometry("1024x768")
    font_p = ("Segoe UI", 12)

    frameMain = Frame(ventanaMain, width=200, height=768) 
    frameMain.pack(fill="both", expand=False, side="left")
    frameMain.pack_propagate(False)

    btnFicha = Button(frameMain, text="Modulo de Fichas", command=lambda:Mostrar_Ficha(ventanaMain))
    btnFicha.pack(pady=10)
    btnFicha.place(x=40, y=75)

    def ContentMain():
        DeleteFrame(ventanaMain)

        ContentFrame = Frame(ventanaMain)
        ContentFrame.pack(side="right", fill="both", expand=True)

        lbl_Entrada = Label(ContentFrame, text="LotusPet", font=font_p).pack(pady=15)
        lbl_Entrada = Label(ContentFrame, text="Para acceder a las funciones utilice los botones laterales", font=font_p).pack()

    ContentMain()
    ventanaMain.mainloop()

Mostrar_Menu()