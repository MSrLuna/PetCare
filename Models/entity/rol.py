from Models.conexion import Conexion

host = 'localhost'
user = 'root'
password = 'inacap'
db = 'LotusPet'

class Rol:
    def __init__(self):
        self.id = None
        self.nombre = None
    
    @staticmethod
    def agregar_rol(nombre):
        try:
            connection = Conexion(host, user, password, db)
            sql = '''INSERT INTO Rol (Nombre) VALUES (%s)'''
            valores = (nombre,)
            connection.Ejecutar_Query(sql, valores)
            connection.Commit()
            connection.desconectar()
        except Exception as e:
            print(e)
            connection.Rollback()

    @staticmethod
    def modificar_rol(id, nombre):
        try:
            connection = Conexion(host, user, password, db)
            sql = '''UPDATE Rol SET Nombre=%s WHERE ID=%s'''
            valores = (nombre, id)
            connection.Ejecutar_Query(sql, valores)
            connection.Commit()
            connection.desconectar()
        except Exception as e:
            print(e)
            connection.Rollback()

    @staticmethod
    def eliminar_rol(id):
        try:
            connection = Conexion(host, user, password, db)
            sql = 'DELETE FROM Rol WHERE ID=%s'
            connection.Ejecutar_Query(sql, (id,))
            connection.Commit()
            connection.desconectar()
        except Exception as e:
            print(e)
            connection.Rollback()

    @staticmethod
    def mostrar_todo():
        try:
            connection = Conexion(host, user, password, db)
            sql = 'SELECT * FROM Rol'
            cursor = connection.Ejecutar_Query(sql, ())
            datos = cursor.fetchall()
            connection.desconectar()
            return datos
        except Exception as e:
            print(e)
            return []
