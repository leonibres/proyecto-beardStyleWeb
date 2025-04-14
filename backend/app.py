from flask import Flask, jsonify  # Importa Flask para crear la aplicación y jsonify para devolver respuestas JSON.
from backend.database.connection import init_db  # Importa la función para inicializar la base de datos.
from backend.routes.reservas import reservas_bp  # Importa el blueprint de las rutas de reservas.
from flask_cors import CORS  # Importa CORS para permitir solicitudes desde otros dominios.

app = Flask(__name__)  # Crea una instancia de la aplicación Flask.

# Configurar CORS para permitir solicitudes solo desde el frontend.
CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}}, methods=["GET", "POST", "PUT", "DELETE"])

# Inicializar la base de datos al inicio.
init_db()

# Define la ruta raíz del servidor.
@app.route('/')
def home():
    return jsonify({"message": "Bienvenido a Beard & Style API"})  # Devuelve un mensaje de bienvenida en formato JSON.

# Registrar las rutas de reservas con el prefijo '/reservas'.
app.register_blueprint(reservas_bp, url_prefix='/reservas')

# Manejador global para errores no controlados.
@app.errorhandler(Exception)
def handle_exception(e):
    response = {
        "error": "Ocurrió un error inesperado",  # Mensaje de error genérico.
        "message": str(e)  # Detalles del error.
    }
    return jsonify(response), 500  # Devuelve el error con un código de estado 500.

# Manejador para rutas no encontradas.
@app.errorhandler(404)
def handle_404(e):
    return jsonify({"error": "Ruta no encontrada"}), 404  # Devuelve un mensaje de error con un código de estado 404.

# Manejador para errores de método no permitido.
@app.errorhandler(405)
def handle_405(e):
    return jsonify({"error": "Método no permitido"}), 405  # Devuelve un mensaje de error con un código de estado 405.

if __name__ == '__main__':
    # Ejecutar el servidor en modo de depuración.
    app.run(debug=True)
