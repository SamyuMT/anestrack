# Clave secreta para firmar el token
SECRET_KEY = "anestrack"


def reestructurar_cadena(diccionario, id):
    # Datos a incluir en el token (día, mes, año)
    datos = {
    "dia": diccionario.get("dia"),
    "mes": diccionario.get("mes"),
    "year": diccionario.get("year")
    }
    # Convertimos los datos en una cadena
    datos_str = f"{datos['dia']:02}{datos['mes']:02}{datos['year']}"
    # Combinamos con la clave secreta
    clave_base = SECRET_KEY + datos_str


    token = "".join(chr(ord(c) + 3) for c in clave_base)
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