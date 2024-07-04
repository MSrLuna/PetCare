class FrameDeleter:
    def __init__(self, ventana_main):
        self.ventana_main = ventana_main

    def delete_frame(self):
        contador_frames = self.ventana_main.winfo_children()
        if len(contador_frames) > 1:
            contador_frames[1].destroy()