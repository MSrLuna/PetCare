from Views.vista_mainmenu import MenuVentana

class MenuVisualizer:
    def __init__(self, user_rol):
        self.user_rol = user_rol

    def visualizar_menu(self):
        menu = MenuVentana(self.user_rol)  # Crear una instancia de MenuVentana

# No es necesario modificar más aquí si no hay otros ajustes específicos.
