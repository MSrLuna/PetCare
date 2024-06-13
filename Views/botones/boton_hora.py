from tkinter import *
def DeleteFrame(ventanaMain):
        contadorFrames = ventanaMain.winfo_children()
        if len(contadorFrames) > 1:
            contadorFrames[1].destroy()
            
def Mostrar_Hora(ventanaMain):
    DeleteFrame(ventanaMain)
    frameHora = Frame(ventanaMain)
    frameHora.pack(fill="both", expand=True)

    btn_AgregarHora = Button(frameHora, text="Agregar Hora")
    btn_AgregarHora.pack(padx=50)
    btn_AgregarHora.place(x=100, y=20)

    btn_EditarHora = Button(frameHora, text="Editar Hora")
    btn_EditarHora.pack(padx=50)
    btn_EditarHora.place(x=275, y=20)

    btn_VisualizarHora = Button(frameHora, text="Vizualizar Hora")
    btn_VisualizarHora.pack(padx=50)
    btn_VisualizarHora.place(x=450, y=20)

    btn_BloquearHora = Button(frameHora, text="Cancelar Hora")
    btn_BloquearHora.pack(padx=100)
    btn_BloquearHora.place(x=650, y=20)