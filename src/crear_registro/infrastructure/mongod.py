from mongo.connect import ConnectionMongo

class MongodCrearRegistro:
    def __init__(self) -> None:
        self.connect = ConnectionMongo()

    def CrearRegistroConnect(self):
        db = self.connect.con  # Asegúrate de que esté accediendo a la conexión correcta
        col = db["registro"]
        return col
