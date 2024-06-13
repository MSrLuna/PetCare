from tkinter import *
def DeleteFrame(ventanaMain):
        contadorFrames = ventanaMain.winfo_children()
        if len(contadorFrames) > 1:
            contadorFrames[1].destroy()
            
def Mostrar_Ficha(ventanaMain):
    DeleteFrame(ventanaMain)
    frameFicha = Frame(ventanaMain)
    frameFicha.pack(fill="both", expand=True)

    btn_AgregarFicha = Button(frameFicha, text="Agregar Ficha")
    btn_AgregarFicha.pack(padx=100)
    btn_AgregarFicha.place(x=225, y=20)

    btn_VisualizarFicha = Button(frameFicha, text="Vizualizar Ficha")
    btn_VisualizarFicha.pack(padx=100)
    btn_VisualizarFicha.place(x=450, y=20)
