from flask import Blueprint, request, jsonify
from src.credential.infrastructure.controller import CredentialController
from include.validators import checkArgs, parsedRespond

# Crear un blueprint para el manejo de rutas de usuario
credential_bp = Blueprint('credential', __name__)

# Instanciar el controlador de usuario
credential_controller = CredentialController()

# Función de consulta
def consulta(credential, pasw):
    credential_info = credential_controller.authenticate_credential(credential, pasw)  # Pasar credencial y contraseña
    return parsedRespond(credential_info)

# Definir una ruta POST para autenticar usuario (correo o celular + contraseña)
@credential_bp.route('/login', methods=['GET'])
def auth_credential():
    """
    Autenticación de usuario por credenciales.
    ---
    tags:
      - Credenciales
    parameters:
      - name: credential
        in: query
        type: string
        required: true
        description: Credencial del usuario (correo o número de teléfono).
      - name: pass
        in: query
        type: string
        required: true
        description: Contraseña del usuario.
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
                id:
                  type: string
                  description: ID del usuario autenticado.
                  example: "12345"
                name:
                  type: string
                  description: Correo electrónico del usuario.
                  example: "admin"
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
        checkArgs(['credential', 'pass'], request.args)
        credential = request.args['credential']
        pasw = request.args['pass']
        print(credential, pasw)

    try:
        # Llamar al método de autenticación del controlador
        return jsonify(consulta(credential, pasw)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400