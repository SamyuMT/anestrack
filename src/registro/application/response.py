class registrosResponse():

    @staticmethod
    def parsedRegistro(registro_info):
        if registro_info:
            parsed_registro = []
            for reporte in registro_info:
                parsed_registro.append({
                    "token": reporte.get("token"),
                    "clinico": reporte.get("clinico"),
                    "agenteAne": reporte.get("agenteAne"),
                    "conMensual": reporte.get("conMensual"),
                    "numeroBotellas": reporte.get("numeroBotellas"),
                    "indiceSemana": reporte.get("indiceSemana"),
                    "indiceDia": reporte.get("indiceDia"),
                    "state": True
                })
            return parsed_registro
            
        else:
            raise Exception("No registro found")