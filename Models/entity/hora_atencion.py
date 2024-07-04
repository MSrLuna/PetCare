from Models.conexion import Conexion

host = 'localhost'
user = 'root'
password = 'inacap'
db = 'lotuspet'

class Hora_Atencion:
    def __init__(self):
        self.id = None
        self.fecha_hora = None
        self.id_cliente = None
        self.id_recepcionista = None
        self.id_veterinario = None
        self.nro_ficha = None
        self.reservado = None
    
    @staticmethod
    def agregar_hora_atencion(fecha_hora, id_cliente, id_recepcionista, id_veterinario, nro_ficha, reservado):
        try:
            connection = Conexion(host, user, password, db)
            sql = '''INSERT INTO Hora_Atencion 
                     (Fecha_Hora, ID_Cliente, ID_Recepcionista, ID_Veterinario, NRO_Ficha, Reservado) 
                     VALUES (%s, %s, %s, %s, %s, %s)'''
            valores = (fecha_hora, id_cliente, id_recepcionista, id_veterinario, nro_ficha, reservado)
            connection.Ejecutar_Query(sql, valores)
            connection.Commit()
            connection.desconectar()
        except Exception as e:
            print(e)
            connection.Rollback()

    @staticmethod
    def modificar_hora_atencion(id, fecha_hora, id_cliente, id_recepcionista, id_veterinario, nro_ficha, reservado):
        try:
            connection = Conexion(host, user, password, db)
            sql = '''UPDATE Hora_Atencion 
                     SET Fecha_Hora=%s, ID_Cliente=%s, ID_Recepcionista=%s, ID_Veterinario=%s, NRO_Ficha=%s, Reservado=%s 
                     WHERE ID=%s'''
            valores = (fecha_hora, id_cliente, id_recepcionista, id_veterinario, nro_ficha, reservado, id)
            connection.Ejecutar_Query(sql, valores)
            connection.Commit()
            connection.desconectar()
        except Exception as e:
            print(e)
            connection.Rollback()

    @staticmethod
    def eliminar_hora_atencion(id):
        try:
            connection = Conexion(host, user, password, db)
            sql = 'DELETE FROM Hora_Atencion WHERE ID=%s'
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
            sql = 'SELECT * FROM Hora_Atencion'
            cursor = connection.Ejecutar_Query(sql, ())
            datos = cursor.fetchall()
            connection.desconectar()
            return datos
        except Exception as e:
            print(e)
            return []
