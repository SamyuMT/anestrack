from flask import Blueprint, request, jsonify
from src.registro.infrastructure.controller import registrosController
from include.validators import checkArgs, parsedRespond

# Crear un blueprint para el manejo de rutas de usuario
registros_bp = Blueprint('registros', __name__)

# Instanciar el controlador de usuario
registro_controller = registrosController()

# Función de consulta
def consulta():
    Registro_info = registro_controller.authenticate_Registros()  # Pasar credencial y contraseña
    return parsedRespond(Registro_info)

# Definir una ruta POST para autenticar usuario (correo o celular + contraseña)
@registros_bp.route('/info', methods=['GET'])
def auth_Registro():
    """
    Consulta de información de usuario.
    ---
    tags:
      - Registros
    responses:
      200:
        description: Consulta exitosa.
        schema:
          type: object
          properties:
            status:
              type: string
              example: success
            data:
              type: object
              properties:
                agenteAne:
                  type: string
                  description: Tipo de agente anestesico.
                  example: "four"
                clinico:
                  type: string
                  description: Tipo de operacion clinica.
                  example: "clinica1"
                conMensual:
                  type: int
                  description: Consumo total.
                  example: 1000
                indiceSemana:
                  type: int
                  description: indicador semanal.
                  example: 12
                numeroBotellas: 
                  type: int
                  description: año del registro.
                  example: 25
                state:
                  type: boolean
                  description: Estado del usuario.
                  example: true
                token:
                  type: string
                  description: Tipo de operacion clinica.
                  example: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkaWEiOiJKb2huIERvZSIsIm1lcyI6MTUxNjIzOTAyMiwieWVhciI6MjAyNX0.ET5VOyR6lBde88UQCv_ItEy8pHwfUxUmLWcx9mflNZ4"
                
      400:
        description: Error en la consulta.
        schema:
          type: object
          properties:
            error:
              type: string
              description: Mensaje de error.
              example: "Usuario no encontrado"
    """
    try:
        # Llamar al método de autenticación del controlador
        return jsonify(consulta()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400