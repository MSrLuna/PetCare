from src.controllers.controlador_login import Iniciar_Sesion
from src.controllers.controlador_menu import Visualizar_Menu

def main():
    #El if llama iniciar_sesion y toma los valores que este arroje y pregunta si es true
    if Iniciar_Sesion():
        Visualizar_Menu(user_rol="Recepcionista")

if __name__=="__main__":
    main()