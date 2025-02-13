
def calulo_variables(diccionario):
    capacidades = {
        "desflurano": 240,
        "isoflurano": 100,
        "sevoflurano": 250
    }
    botellas_consumidas = diccionario.get("conMensual") / capacidades[diccionario.get("agenteAne")]
    indice_rotacion_semanal = botellas_consumidas / 4.33
    indice_rotacion_diario = botellas_consumidas / 30.44
    return botellas_consumidas,indice_rotacion_semanal,indice_rotacion_diario

def reestructurar_cadena(diccionario, id):
    numBotellas, indiceSemana, indiceDia = calulo_variables(diccionario)
    transformed_data = {
        "token":  id,
        "clinico":  diccionario.get("clinico"),
        "agenteAne":  diccionario.get("agenteAne"),
        "conMensual":  diccionario.get("conMensual"),
        "numeroBotellas": numBotellas,
        "indiceSemana":  indiceSemana,
        "indiceDia": indiceDia,
    }
    return transformed_data

class CrearRegistroResponse():
    @staticmethod
    def SetCrearRegistro(col, data, id):
        if data:
            newData = reestructurar_cadena(data, id)
            result = col.insert_one(newData)
            print(result)

            return True
        else:
            return False       