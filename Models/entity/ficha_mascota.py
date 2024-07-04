from Models.conexion import Conexion

host = 'localhost'
user = 'root'
password = 'inacap'
db = 'lotuspet'

class Ficha_Mascota:
    def __init__(self):
        self.nro = None
        self.nombre = None
        self.edad = None
        self.nro_atenciones = None
        self.fecha_atencion = None
        self.sexo = None
        self.id_usuario = None
    
    @staticmethod
    def agregar_ficha_mascota(nombre, edad, nro_atenciones, fecha_atencion, sexo, id_usuario):
        try:
            connection = Conexion(host, user, password, db)
            sql = '''INSERT INTO Ficha_Mascota 
                     (Nombre, Edad, NRO_Atenciones, Fecha_Atencion, Sexo, ID_Usuario) 
                     VALUES (%s, %s, %s, %s, %s, %s)'''
            valores = (nombre, edad, nro_atenciones, fecha_atencion, sexo, id_usuario)
            connection.Ejecutar_Query(sql, valores)
            connection.Commit()
            connection.desconectar()
        except Exception as e:
            print(e)
            connection.Rollback()

    @staticmethod
    def modificar_ficha_mascota(nro, nombre, edad, nro_atenciones, fecha_atencion, sexo, id_usuario):
        try:
            connection = Conexion(host, user, password, db)
            sql = '''UPDATE Ficha_Mascota 
                     SET Nombre=%s, Edad=%s, NRO_Atenciones=%s, Fecha_Atencion=%s, Sexo=%s, ID_Usuario=%s 
                     WHERE NRO=%s'''
            valores = (nombre, edad, nro_atenciones, fecha_atencion, sexo, id_usuario, nro)
            connection.Ejecutar_Query(sql, valores)
            connection.Commit()
            connection.desconectar()
        except Exception as e:
            print(e)
            connection.Rollback()

    @staticmethod
    def eliminar_ficha_mascota(nro):
        try:
            connection = Conexion(host, user, password, db)
            sql = 'DELETE FROM Ficha_Mascota WHERE NRO=%s'
            connection.Ejecutar_Query(sql, (nro,))
            connection.Commit()
            connection.desconectar()
        except Exception as e:
            print(e)
            connection.Rollback()

    @staticmethod
    def mostrar_todo():
        try:
            connection = Conexion(host, user, password, db)
            sql = 'SELECT * FROM Ficha_Mascota'
            cursor = connection.Ejecutar_Query(sql, ())
            datos = cursor.fetchall()
            connection.desconectar()
            return datos
        except Exception as e:
            print(e)
            return []
