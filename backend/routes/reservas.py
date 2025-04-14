from flask import Blueprint, request, jsonify
from backend.models.reserva import create_reserva, get_reservas, update_reserva, delete_reserva

reservas_bp = Blueprint('reservas', __name__)

# Ruta para crear una reserva
@reservas_bp.route('', methods=['POST'])
def create_reserva_route():
    try:
        data = request.get_json()
        # Validar que todos los campos requeridos estén presentes
        required_fields = ['nombre', 'fecha', 'servicio']
        missing_fields = [field for field in required_fields if field not in data or not data[field]]
        if missing_fields:
            return jsonify({'error': f'Datos incompletos. Faltan los campos: {", ".join(missing_fields)}'}), 400
        
        reserva = create_reserva(data)
        return jsonify(reserva), 201
    except Exception as e:
        return jsonify({'error': f'Error al crear la reserva: {str(e)}'}), 500

# Ruta para obtener todas las reservas
@reservas_bp.route('', methods=['GET'])
def get_reservas_route():
    try:
        reservas = get_reservas()
        return jsonify(reservas), 200
    except Exception as e:
        return jsonify({'error': f'Error al obtener reservas: {str(e)}'}), 500

# Ruta para actualizar una reserva
@reservas_bp.route('/<int:id>', methods=['PUT'])
def update_reserva_route(id):
    try:
        data = request.get_json()
        required_fields = ['nombre', 'fecha', 'servicio']
        missing_fields = [field for field in required_fields if field not in data or not data[field]]
        if missing_fields:
            return jsonify({'error': f'Datos incompletos. Faltan los campos: {", ".join(missing_fields)}'}), 400
        
        reserva = update_reserva(id, data)
        if reserva:
            return jsonify(reserva), 200
        return jsonify({'error': 'Reserva no encontrada'}), 404
    except Exception as e:
        return jsonify({'error': f'Error al actualizar la reserva: {str(e)}'}), 500

# Ruta para eliminar una reserva
@reservas_bp.route('/<int:id>', methods=['DELETE'])
def delete_reserva_route(id):
    try:
        deleted = delete_reserva(id)
        if deleted:
            return jsonify({'message': 'Reserva eliminada'}), 200
        return jsonify({'error': 'Reserva no encontrada'}), 404
    except Exception as e:
        return jsonify({'error': f'Error al eliminar la reserva: {str(e)}'}), 500