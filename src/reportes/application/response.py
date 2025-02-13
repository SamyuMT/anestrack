import jwt

SECRET_KEY = "anestrack"

class reportesResponse():

    @staticmethod
    def parsedReportes(reportes_info):
        if reportes_info:
            parsed_reportes = []
            for reporte in reportes_info:
                print(reporte)
                try:
                    decoded_token = jwt.decode(reporte['token'], SECRET_KEY, algorithms=["HS256"])
                    print(decoded_token)
                    parsed_reportes.append({
                        "token": reporte.get("token"),
                        "dia": decoded_token.get("dia"),
                        "mes": decoded_token.get("mes"),
                        "year": decoded_token.get("year"),
                        "id_user": reporte.get("id_user"),
                        "state": True
                    })
                except jwt.DecodeError:
                    raise Exception("Error decoding token")
            print(parsed_reportes)
            return parsed_reportes
            
        else:
            raise Exception("No reportes found")