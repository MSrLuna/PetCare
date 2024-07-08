from Models.conexion import Conexion

host = 'localhost'
user = 'root'
password = 'inacap'
db = 'LotusPet'

class Usuario:
    def __init__(self):
        self.id = None
        self.rut = None
        self.nombre = None
        self.apellido = None
        self.rol_id = None
        self.fecha_contrato = None
        self.turno = None
        self.contraseña = None
    
    @staticmethod
    def agregar_usuario(rut, nombre, apellido, rol_id, fecha_contrato, turno, contraseña):
        try:
            connection = Conexion(host, user, password, db)
            sql = '''INSERT INTO Usuario 
                     (RUT, Nombre, Apellido, Rol_ID, Fecha_Contrato, Turno, Contraseña) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s)'''
            valores = (rut, nombre, apellido, rol_id, fecha_contrato, turno, contraseña)
            connection.Ejecutar_Query(sql, valores)
            connection.Commit()
            connection.desconectar()
        except Exception as e:
            print(e)
            connection.Rollback()

    @staticmethod
    def modificar_usuario(id, rut, nombre, apellido, rol_id, fecha_contrato, turno, contraseña):
        try:
            connection = Conexion(host, user, password, db)
            sql = '''UPDATE Usuario 
                     SET RUT=%s, Nombre=%s, Apellido=%s, Rol_ID=%s, Fecha_Contrato=%s, Turno=%s, Contraseña=%s 
                     WHERE ID=%s'''
            valores = (rut, nombre, apellido, rol_id, fecha_contrato, turno, contraseña, id)
            connection.Ejecutar_Query(sql, valores)
            connection.Commit()
            connection.desconectar()
        except Exception as e:
            print(e)
            connection.Rollback()

    @staticmethod
    def eliminar_usuario(id):
        try:
            connection = Conexion(host, user, password, db)
            sql = 'DELETE FROM Usuario WHERE ID=%s'
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
            sql = 'SELECT * FROM Usuario'
            cursor = connection.Ejecutar_Query(sql, ())
            datos = cursor.fetchall()
            connection.desconectar()
            return datos
        except Exception as e:
            print(e)
            return []
    
    # HACER METODO QUE RETORNE AL USUARIO COMPLETO POR EL RUT Y CONTRASEÑA
    @staticmethod
    def mostrar_usuario_por_cred(rut, contraseña):
        try:
            connection = Conexion(host, user, password, db)
            sql = 'SELECT * FROM Usuario WHERE RUT=%s AND Contraseña=%s'
            cursor = connection.Ejecutar_Query(sql, (rut, contraseña))
            datos = cursor.fetchone()
            if datos:
                usuario = Usuario()
                usuario.id = datos[0]
                usuario.rut = datos[1]
                usuario.nombre = datos[2]
                usuario.apellido = datos[3]
                usuario.rol_id = datos[4]
                usuario.fecha_contrato = datos[5]
                usuario.turno = datos[6]
                usuario.contraseña = datos[7]
                return usuario
            else:
                connection.desconectar()
        except:
            return []
    # PARA LUEGO PREGUNTAR EN EL MENU EL ROL DEL USUARIO QUE SE TRAJO 
    # Y ENVIARLO A LA VISTA QUE CORRESPONDE

    #HACER UN METODO PARA ELEGIR UN USUARIO POR ID, PARA VERLO EN LA TABLA