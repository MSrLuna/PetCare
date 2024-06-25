from Controllers.controlador_login import SessionManager
from Controllers.controlador_menu import MenuVisualizer

def main():
    session_manager = SessionManager()
    if session_manager.iniciar_sesion():
        menu_visualizer = MenuVisualizer(user_rol="Recepcionista")
        menu_visualizer.visualizar_menu()

if __name__ == "__main__":
    main()