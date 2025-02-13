from mongo.connect import ConnectionMongo

class MongodToken:
    def __init__(self) -> None:
        self.connect = ConnectionMongo()

    def TokenConnect(self, token):
        db = self.connect.con  # Asegúrate de que esté accediendo a la conexión correcta
        col = db["reporte"]
        # Verificar si creditial es un email o un número de teléfono
        token = col.find_one({"token": token})
        return token
