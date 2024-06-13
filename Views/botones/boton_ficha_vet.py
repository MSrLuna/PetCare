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
    btn_AgregarFicha.pack(padx=50)
    btn_AgregarFicha.place(x=100, y=20)

    btn_EditarFicha = Button(frameFicha, text="Editar Ficha")
    btn_EditarFicha.pack(padx=50)
    btn_EditarFicha.place(x=275, y=20)

    btn_VisualizarFicha = Button(frameFicha, text="Vizualizar Ficha")
    btn_VisualizarFicha.pack(padx=50)
    btn_VisualizarFicha.place(x=450, y=20)

    btn_BloquearFicha = Button(frameFicha, text="Bloquear Ficha")
    btn_BloquearFicha.pack(padx=100)
    btn_BloquearFicha.place(x=650, y=20)
