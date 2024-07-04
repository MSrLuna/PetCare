from Controllers.controlador_login import SessionManager
from Controllers.controlador_menu import MenuVisualizer

def main():
    session_manager = SessionManager()
    if session_manager.iniciar_sesion():
        user_rol = session_manager.obtener_rol_usuario()
        if user_rol is not None:
            menu_visualizer = MenuVisualizer(user_rol)
            menu_visualizer.visualizar_menu()
        else:
            print("No se pudo obtener el rol del usuario.")

if __name__ == "__main__":
    main()
