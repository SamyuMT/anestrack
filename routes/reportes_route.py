from flask import Blueprint, request, jsonify
from src.reportes.infrastructure.controller import reportesController
from include.validators import checkArgs, parsedRespond

# Crear un blueprint para el manejo de rutas de usuario
reportes_bp = Blueprint('reportes', __name__)

# Instanciar el controlador de usuario
reportes_controller = reportesController()

# Función de consulta
def consulta():
    Reportes_info = reportes_controller.authenticate_Reportes()  # Pasar credencial y contraseña
    return parsedRespond(Reportes_info)

# Definir una ruta POST para autenticar usuario (correo o celular + contraseña)
@reportes_bp.route('/info', methods=['GET'])
def auth_Reportes():
    """
    Consulta de información de usuario.
    ---
    tags:
      - Reportes
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
                dia:
                  type: int
                  description: Dia del registro.
                  example: 12
                id_user:
                  type: string
                  description: ID del usuario.
                  example: "67ac0c06038754bbb63722171029192"
                mes:
                  type: int
                  description: Mes del registro.
                  example: 5
                state:
                  type: boolean
                  description: Estado del usuario.
                  example: true
                year: 
                  type: int
                  description: año del registro.
                  example: 2025
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