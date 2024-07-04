from Views.vista_mainmenu import MenuVentana
from Views.vista_recepcionista import MenuPrincipalR
from Views.vista_veterinario import MenuPrincipalV

class MenuVisualizer:
    def __init__(self, user_rol):
        self.user_rol = user_rol

    def visualizar_menu(self):
        if self.user_rol == 1:
            menu = MenuPrincipalR()
        elif self.user_rol == 2:
            menu = MenuPrincipalV()
        else:
            menu = MenuVentana(self.user_rol)
