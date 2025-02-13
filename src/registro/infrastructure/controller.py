from src.registro.infrastructure.mongod import MongodRegistros
from ..application.response import registrosResponse

class registrosController:

    def __init__(self):
        self.mongo_Registros = MongodRegistros()
        self.response = registrosResponse()

    def authenticate_Registros(self):
        Registros_info = self.mongo_Registros.get_all_reports()
        parsed = self.response.parsedRegistro(Registros_info)
        return parsed


