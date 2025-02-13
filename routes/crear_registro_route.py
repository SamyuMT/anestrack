from flask import Blueprint, request, abort
from src.crear_registro.infrastructure.controller import CrearRegistroController
from include.validators import checkArgs

# Crear un blueprint para el manejo de rutas de usuario
crear_registro_bp = Blueprint('crear_registro', __name__)
registro_crear_controller = CrearRegistroController()

# Función de consulta
def consulta(info, id):
    registro_info = registro_crear_controller.crear_registro(info, id)  # Pasar información del usuario y ID

# Definir una ruta POST para crear un usuario
@crear_registro_bp.route('/create', methods=['POST'])
def set_crear_user():
    """
    Crear un nuevo registro.
    ---
    tags:
      - Crear Registro
    consumes:
      - application/json
    produces:
      - application/json
    parameters:
      - in: body
        name: body
        description: Datos necesarios para crear el registro
        required: true
        schema:
          type: object
          properties:
            token:
              type: string
              example: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkaWEiOiJKb2huIERvZSIsIm1lcyI6MTUxNjIzOTAyMiwieWVhciI6MjAyNX0.ET5VOyR6lBde88UQCv_ItEy8pHwfUxUmLWcx9mflNZ4"
            data:
              type: object
              properties:
                clinico:
                  type: string
                  example: "clinico1"
                agenteAne:
                  type: string
                  example: "sevoflurano"
                conMensual: 
                  type: int
                  example: 1000.12
    responses:
      200:
        description: Usuario creado correctamente
      404:
        description: Error al crear
    """
    json_data = request.get_json()
    id = json_data.get('token')
    data = json_data.get('data')
    if not data or not id:
        return abort(400, description="Datos no proporcionados")
    try:
        consulta(data, id)
        return f"Registro creado correctamente {data}"
    except FileNotFoundError:
        return abort(404, description="Error al crear")