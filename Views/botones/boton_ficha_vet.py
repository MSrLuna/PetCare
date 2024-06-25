from tkinter import *

class FrameDeleter:
    def __init__(self, ventana_main):
        self.ventana_main = ventana_main

    def delete_frame(self):
        contador_frames = self.ventana_main.winfo_children()
        if len(contador_frames) > 1:
            contador_frames[1].destroy()

class FichaViewer:
    def __init__(self, ventana_main):
        self.ventana_main = ventana_main
        self.frame_deleter = FrameDeleter(ventana_main)

    def mostrar_ficha(self):
        self.frame_deleter.delete_frame()
        frame_ficha = Frame(self.ventana_main)
        frame_ficha.pack(fill="both", expand=True)

        btn_agregar_ficha = Button(frame_ficha, text="Agregar Ficha")
        btn_agregar_ficha.pack(padx=50)
        btn_agregar_ficha.place(x=100, y=20)

        btn_editar_ficha = Button(frame_ficha, text="Editar Ficha")
        btn_editar_ficha.pack(padx=50)
        btn_editar_ficha.place(x=275, y=20)

        btn_visualizar_ficha = Button(frame_ficha, text="Visualizar Ficha")
        btn_visualizar_ficha.pack(padx=50)
        btn_visualizar_ficha.place(x=450, y=20)

        btn_bloquear_ficha = Button(frame_ficha, text="Bloquear Ficha")
        btn_bloquear_ficha.pack(padx=100)
        btn_bloquear_ficha.place(x=650, y=20)

# Ejemplo de uso:
# ventana_main = Tk()
# ficha_viewer = FichaViewer(ventana_main)
# ficha_viewer.mostrar_ficha()
# ventana_main.mainloop()
