from src.crear_registro.infrastructure.mongod import MongodCrearRegistro
from ..application.response import CrearRegistroResponse

class CrearRegistroController:

    def __init__(self):
        self.mongo_number_validar = MongodCrearRegistro()
        self.response = CrearRegistroResponse()

    def crear_registro(self, data, id):
        col = self.mongo_number_validar.CrearRegistroConnect()
        parsed = self.response.SetCrearRegistro(col, data, id)
        return parsed


