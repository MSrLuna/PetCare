from tkinter import *

class FrameDeleter:
    def __init__(self, ventana_main):
        self.ventana_main = ventana_main

    def delete_frame(self):
        contador_frames = self.ventana_main.winfo_children()
        if len(contador_frames) > 1:
            contador_frames[1].destroy()

class HoraViewer:
    def __init__(self, ventana_main):
        self.ventana_main = ventana_main
        self.frame_deleter = FrameDeleter(ventana_main)

    def mostrar_hora(self):
        self.frame_deleter.delete_frame()
        frame_hora = Frame(self.ventana_main)
        frame_hora.pack(fill="both", expand=True)

        btn_agregar_hora = Button(frame_hora, text="Agregar Hora")
        btn_agregar_hora.pack(padx=50)
        btn_agregar_hora.place(x=100, y=20)

        btn_editar_hora = Button(frame_hora, text="Editar Hora")
        btn_editar_hora.pack(padx=50)
        btn_editar_hora.place(x=275, y=20)

        btn_visualizar_hora = Button(frame_hora, text="Visualizar Hora")
        btn_visualizar_hora.pack(padx=50)
        btn_visualizar_hora.place(x=450, y=20)

        btn_bloquear_hora = Button(frame_hora, text="Cancelar Hora")
        btn_bloquear_hora.pack(padx=100)
        btn_bloquear_hora.place(x=650, y=20)

# Ejemplo de uso:
# ventana_main = Tk()
# hora_viewer = HoraViewer(ventana_main)
# hora_viewer.mostrar_hora()
# ventana_main.mainloop()
