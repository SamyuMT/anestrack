from mongo.connect import ConnectionMongo

class MongodCrearReporte:
    def __init__(self) -> None:
        self.connect = ConnectionMongo()

    def CrearReporteConnect(self):
        db = self.connect.con  # Asegúrate de que esté accediendo a la conexión correcta
        col = db["reporte"]
        return col
