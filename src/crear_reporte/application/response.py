import jwt

# Clave secreta para firmar el token
SECRET_KEY = "anestrack"


def reestructurar_cadena(diccionario, id):
    # Datos a incluir en el token (día, mes, año)
    datos = {
    "dia": diccionario.get("dia"),
    "mes": diccionario.get("mes"),
    "year": diccionario.get("year")
    }
    token = jwt.encode(datos, SECRET_KEY, algorithm="HS256")
    print("Token JWT generado:", token)
    transformed_data = {
        "token": token,
        "id_user": id,
    }
    return transformed_data

class CrearReporteResponse():

    @staticmethod
    def SetCrearReporte(col, data, id):
        if data:
            newData = reestructurar_cadena(data, id)
            result = col.insert_one(newData)
            print(result)

            return True
        else:
            return False       