import pymysql

class Conexion:
    def __init__(self, host, user, contrasena, db):
        self.db = pymysql.connect(
            host= host,
            user= user,
            password= contrasena,
            db= db
        )
        self.cursor = self.db.cursor()
    
    def conectar(self):
        # Aquí va la lógica para la conexión a la base de datos
        # Por ejemplo:
        # return conectar_a_base_de_datos(self.user, self.password)
        pass

    def Ejecutar_Query(self, sql, valores):
        self.cursor.execute(sql, valores)
        return self.cursor
    
    def desconectar(self):
        self.db.close()

    def Commit(self):
        self.db.commit()
    
    def Rollback(self):
        self.db.rollback()