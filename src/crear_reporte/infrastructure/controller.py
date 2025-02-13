from src.crear_reporte.infrastructure.mongod import MongodCrearReporte
from ..application.response import CrearReporteResponse

class CrearReporteController:

    def __init__(self):
        self.mongo_number_validar = MongodCrearReporte()
        self.response = CrearReporteResponse()

    def crear_reporte(self, data, id):
        col = self.mongo_number_validar.CrearReporteConnect()
        parsed = self.response.SetCrearReporte(col, data, id)
        return parsed


