from tkinter import messagebox
from Views.vista_login import Login  # Importar la clase Login

class LogInViewer:
    def mostrar_login(self):
        login = Login()
        user, password = login.get_credentials()
        return user, password

class SessionManager:
    def iniciar_sesion(self):
        viewer = LogInViewer()
        user, password = viewer.mostrar_login()
        
        # Aquí puedes poner la lógica de autenticación real, por ejemplo:
        if user == "a" and password == "a":
            return True
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")
            return False
