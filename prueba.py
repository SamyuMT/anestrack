import jwt

# Clave secreta para firmar el token
SECRET_KEY = "anestrack"

# Datos a incluir en el token (día, mes, año)
datos = {
    "dia": 12,
    "mes": 5,
    "year": 2022
}

# Crear el token
token = jwt.encode(datos, SECRET_KEY, algorithm="HS256")
print("Token JWT generado:", token)

# Decodificar el token
try:
    decoded_data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    print("Datos decodificados:", decoded_data)
except jwt.ExpiredSignatureError:
    print("El token ha expirado.")
except jwt.InvalidTokenError:
    print("El token no es válido.")
