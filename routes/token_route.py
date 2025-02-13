from flask import Blueprint, request, jsonify
from src.token.infrastructure.controller import TokenController
from include.validators import checkArgs, parsedRespond

# Crear un blueprint para el manejo de rutas de usuario
token_bp = Blueprint('token', __name__)

# Instanciar el controlador de usuario
token_controller = TokenController()

# Función de consulta
def consulta(token):
    token_info = token_controller.authenticate_token(token)  # Pasar credencial y contraseña
    return parsedRespond(token_info)

# Definir una ruta POST para autenticar usuario (correo o celular + contraseña)
@token_bp.route('/token', methods=['GET'])
def auth_token():
    """
    Autenticación de Token.
    ---
    tags:
      - Token
    parameters:
      - name: token
        in: query
        type: string
        required: true
        description: Credencial del usuario (correo o número de teléfono).
    responses:
      200:
        description: Autenticación exitosa.
        schema:
          type: object
          properties:
            status:
              type: string
              example: success
            data:
              type: object
              properties:
                state:
                  type: boolean
                  description: Estado del usuario.
                  example: true
      400:
        description: Error de autenticación.
        schema:
          type: object
          properties:
            error:
              type: string
              description: Mensaje de error.
              example: "Usuario o contraseña incorrectos"
    """
    if request.method == 'GET':
        # Si los parámetros vienen en la URL
        checkArgs(['token'], request.args)
        token = request.args['token']
        print(token)

    try:
        # Llamar al método de autenticación del controlador
        return jsonify(consulta(token)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400