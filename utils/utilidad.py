def DeleteFrame(ventanaMain):
    contadorFrames = ventanaMain.winfo_children()
    if len(contadorFrames) > 1:
        contadorFrames[1].destroy()