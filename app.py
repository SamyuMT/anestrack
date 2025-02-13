from flask import Flask
from flask_cors import CORS
from routes.credential_route import credential_bp
from routes.reportes_route import reportes_bp
from routes.crear_reporte_route import crear_reporte_bp
from routes.registros_route import registros_bp
from routes.crear_registro_route import crear_registro_bp
from routes.token_route import token_bp


from swagger_config import configure_swagger

app = Flask(__name__)
CORS(app)

app.register_blueprint(credential_bp, url_prefix='/get_credential')
app.register_blueprint(reportes_bp, url_prefix='/get_reportes')
app.register_blueprint(crear_reporte_bp, url_prefix='/crear_reporte')
app.register_blueprint(registros_bp, url_prefix='/get_registros')
app.register_blueprint(crear_registro_bp, url_prefix='/crear_registro')
app.register_blueprint(token_bp, url_prefix='/get_token')

# Configurar Swagger
configure_swagger(app)

@app.route('/')
def hello():
    return '''
    hola mundo
    '''


if __name__ == '__main__':
    global model
    app.run(host="0.0.0.0", port=5002, debug=True)