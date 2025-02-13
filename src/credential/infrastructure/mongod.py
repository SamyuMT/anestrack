from mongo.connect import ConnectionMongo

class MongodCredential:
    def __init__(self) -> None:
        self.connect = ConnectionMongo()

    def CredentialConnect(self, credential, pasw):
        print(credential,pasw)
        db = self.connect.con  # Asegúrate de que esté accediendo a la conexión correcta
        col = db["admin"]
        # Verificar si creditial es un email o un número de teléfono
        user = col.find_one({"name": credential, "password": pasw})
        return user
