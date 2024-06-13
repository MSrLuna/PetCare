from tkinter import messagebox
from src.views.vista_login import Credenciales

def Mostrar_LogIn():
    Credenciales()

def Iniciar_Sesion():
    user, password = Credenciales()
    
    if user == "a" and password == "a":
        return True
    else:
        messagebox.showerror("Error", "Credenciales incorrectas")
        Mostrar_LogIn()
        return False