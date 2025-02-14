SECRET_KEY = "anestrack"

class reportesResponse():

    @staticmethod
    def parsedReportes(reportes_info):
        if reportes_info:
            parsed_reportes = []
            for reporte in reportes_info:
                print(reporte)
                decoded_token = "".join(chr(ord(c) - 3) for c in reporte['token'])
                datos_extraidos = decoded_token[-8:]  # Últimos 8 caracteres corresponden a los datos
                # Extraer día, mes y año
                dia_extraido = int(datos_extraidos[:2])
                mes_extraido = int(datos_extraidos[2:4])
                year_extraido = int(datos_extraidos[4:])
                parsed_reportes.append({
                    "token": reporte.get("token"),
                    "dia": dia_extraido,
                    "mes": mes_extraido,
                    "year": year_extraido,
                    "id_user": reporte.get("id_user"),
                    "state": True
                })
            print(parsed_reportes)
            return parsed_reportes
            
        else:
            raise Exception("No reportes found")