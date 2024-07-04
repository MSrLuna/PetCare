from tkinter import messagebox
from Views.vista_login import Login
from Models.entity.usuario import Usuario
from Controllers.controlador_menu import MenuVisualizer

class LogInViewer:
    def mostrar_login(self):
        login = Login()
        user, password = login.get_credentials()
        return user, password

class SessionManager:
    def iniciar_sesion(self):
        viewer = LogInViewer()
        user, password = viewer.mostrar_login()

        if user == "" or password == "":
            messagebox.showerror("Credenciales", "Credenciales vacías")
            return False

        # Aquí deberías realizar la validación de las credenciales en la base de datos
        # Este es un ejemplo de cómo se podría validar, ajusta según tu implementación real
        menu_user = Usuario.mostrar_usuario_por_cred(user, password)
        if menu_user:
            self.usuario = menu_user
            return True
        else:
            messagebox.showerror("Error de inicio de sesión", "Usuario o contraseña incorrectos.")
            return False

    def obtener_rol_usuario(self):
        if hasattr(self, 'usuario'):
            return self.usuario.rol_id
        return None
