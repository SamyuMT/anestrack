# Clave secreta
SECRET_KEY = "anestrack"

# Datos a incluir en el token
datos = {
    "dia": 12,
    "mes": 5,
    "year": 2022
}

# Convertimos los datos en una cadena
datos_str = f"{datos['dia']:02}{datos['mes']:02}{datos['year']}"

# Combinamos con la clave secreta
clave_base = SECRET_KEY + datos_str

# Codificamos sumando valores ASCII
clave_codificada = "".join(chr(ord(c) + 3) for c in clave_base)

# Decodificamos restando valores ASCII
clave_decodificada = "".join(chr(ord(c) - 3) for c in clave_codificada)

# Separar la clave secreta y los datos
clave_decodificada_sin_datos = clave_decodificada[:-8]  # Extraer clave sin los últimos 8 caracteres (los datos)
datos_extraidos = clave_decodificada[-8:]  # Últimos 8 caracteres corresponden a los datos

# Extraer día, mes y año
dia_extraido = int(datos_extraidos[:2])
mes_extraido = int(datos_extraidos[2:4])
year_extraido = int(datos_extraidos[4:])

# Mostramos los resultados
print("Clave Codificada:", clave_codificada)
print("Clave Decodificada:", clave_decodificada)
print("Clave Secreta Extraída:", clave_decodificada_sin_datos)
print(f"Día: {dia_extraido}, Mes: {mes_extraido}, Año: {year_extraido}")
