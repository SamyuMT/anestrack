from flask import Blueprint, request, abort
from src.crear_reporte.infrastructure.controller import CrearReporteController
from include.validators import checkArgs

# Crear un blueprint para el manejo de rutas de usuario
crear_reporte_bp = Blueprint('crear_reporte', __name__)
reporte_crear_controller = CrearReporteController()

# Función de consulta
def consulta(info, id):
    reporte_info = reporte_crear_controller.crear_reporte(info, id)  # Pasar información del usuario y ID

# Definir una ruta POST para crear un usuario
@crear_reporte_bp.route('/create', methods=['POST'])
def set_crear_user():
    """
    Crear un nuevo reporte.
    ---
    tags:
      - Crear Reporte
    consumes:
      - application/json
    produces:
      - application/json
    parameters:
      - in: body
        name: body
        description: Datos necesarios para crear el reporte
        required: true
        schema:
          type: object
          properties:
            id:
              type: string
              example: "67ac0c06038754bbb63722171029192"
            data:
              type: object
              properties:
                dia:
                  type: int
                  example: 12
                mes:
                  type: int
                  example: 5
                year: 
                  type: int
                  example: 2025
    responses:
      200:
        description: Usuario creado correctamente
      404:
        description: Error al crear
    """
    json_data = request.get_json()
    id = json_data.get('id')
    data = json_data.get('data')
    if not data or not id:
        return abort(400, description="Datos no proporcionados")
    try:
        consulta(data, id)
        return f"Reporte creado correctamente {data}"
    except FileNotFoundError:
        return abort(404, description="Error al crear")