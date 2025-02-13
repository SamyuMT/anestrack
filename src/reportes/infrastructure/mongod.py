from mongo.connect import ConnectionMongo

class MongodReportes:
    def __init__(self) -> None:
        self.connect = ConnectionMongo()

    def get_all_reports(self):
        db = self.connect.con  # Asegúrate de que esté accediendo a la conexión correcta
        col = db["reporte"]
        reports = col.find()
        return list(reports)
