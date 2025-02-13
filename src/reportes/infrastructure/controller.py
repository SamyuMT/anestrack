from src.reportes.infrastructure.mongod import MongodReportes
from ..application.response import reportesResponse

class reportesController:

    def __init__(self):
        self.mongo_Reportes = MongodReportes()
        self.response = reportesResponse()

    def authenticate_Reportes(self):
        Reportes_info = self.mongo_Reportes.get_all_reports()
        parsed = self.response.parsedReportes(Reportes_info)
        return parsed


