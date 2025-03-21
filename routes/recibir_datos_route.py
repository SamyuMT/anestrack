from flask import Blueprint, request, jsonify
from mongo.connect import ConnectionMongo  # Importar la conexión a MongoDB

# Crear un Blueprint para la ruta
recibir_datos_bp = Blueprint('recibir_datos', __name__)

# Instanciar la conexión a MongoDB
mongo_connection = ConnectionMongo()

@recibir_datos_bp.route('/recibir_datos', methods=['POST'])
def recibir_datos():
    """
    Recibir datos de sensores enviados por el ESP32.
    ---
    tags:
      - Sensores
    parameters:
      - in: body
        name: body
        required: true
        description: Datos enviados por el ESP32.
        schema:
          type: object
          properties:
            date:
              type: string
              description: Identificador del dispositivo.
              example: "2021-09-15T12:00:00"
            humedad:
              type: number
              description: Nivel de humedad.
              example: 45.5
            temperatura:
              type: number
              description: Temperatura medida.
              example: 22.3
            distancia:
              type: number
              description: Distancia medida.
              example: 150.0
            luz:
              type: number
              description: Nivel de luz.
              example: 300
    responses:
      200:
        description: Datos recibidos correctamente.
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Datos recibidos correctamente"
      400:
        description: Error en los datos enviados.
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Datos incompletos"
      500:
        description: Error interno del servidor.
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Error interno del servidor"
    """
    try:
        # Obtener los datos JSON enviados por el ESP32
        datos = request.get_json()

        # Validar que los datos necesarios están presentes
        if not datos or 'date' not in datos or 'humedad' not in datos or 'temperatura' not in datos or 'distancia' not in datos or 'luz' not in datos:
            return jsonify({"error": "Datos incompletos"}), 400

        # Extraer los datos
        date = datos['date']
        humedad = datos['humedad']
        temperatura = datos['temperatura']
        distancia = datos['distancia']
        luz = datos['luz']

        # Guardar los datos en la colección "sensores"
        sensores_collection = mongo_connection.con['sensores']
        sensores_collection.insert_one({
            "date": date,
            "humedad": humedad,
            "temperatura": temperatura,
            "distancia": distancia,
            "luz": luz
        })

        # Responder al ESP32 con un mensaje de éxito
        return jsonify({"message": "Datos recibidos correctamente"}), 200

    except Exception as e:
        # Manejar errores
        print(f"Error al procesar los datos: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500