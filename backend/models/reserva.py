from backend.database.connection import get_db  # Importa la función para obtener la conexión a la base de datos.

# Función para crear una nueva reserva.
def create_reserva(data):
    try:
        conn = get_db()  # Obtiene la conexión a la base de datos.
        cursor = conn.cursor()  # Crea un cursor para ejecutar comandos SQL.
        # Inserta una nueva reserva en la tabla.
        cursor.execute('''
            INSERT INTO reservas (nombre, fecha, servicio)
            VALUES (?, ?, ?)
        ''', (data['nombre'], data['fecha'], data['servicio']))
        conn.commit()  # Guarda los cambios.
        reserva_id = cursor.lastrowid  # Obtiene el ID de la reserva recién creada.
        conn.close()  # Cierra la conexión.
        return {**data, 'id': reserva_id}  # Devuelve los datos de la reserva con el ID.
    except Exception as e:
        raise Exception(f"Error al crear la reserva: {str(e)}")  # Maneja errores.

# Función para obtener todas las reservas.
def get_reservas():
    try:
        conn = get_db()  # Obtiene la conexión a la base de datos.
        cursor = conn.cursor()  # Crea un cursor para ejecutar comandos SQL.
        cursor.execute('SELECT * FROM reservas')  # Obtiene todas las reservas.
        rows = cursor.fetchall()  # Recupera todas las filas.
        conn.close()  # Cierra la conexión.
        return [dict(row) for row in rows]  # Devuelve las reservas como una lista de diccionarios.
    except Exception as e:
        raise Exception(f"Error al obtener reservas: {str(e)}")  # Maneja errores.

# Función para actualizar una reserva existente.
def update_reserva(id, data):
    try:
        conn = get_db()  # Obtiene la conexión a la base de datos.
        cursor = conn.cursor()  # Crea un cursor para ejecutar comandos SQL.
        # Actualiza los datos de una reserva específica.
        cursor.execute('''
            UPDATE reservas
            SET nombre = ?, fecha = ?, servicio = ?
            WHERE id = ?
        ''', (data['nombre'], data['fecha'], data['servicio'], id))
        conn.commit()  # Guarda los cambios.
        updated = cursor.rowcount > 0  # Verifica si se actualizó alguna fila.
        conn.close()  # Cierra la conexión.
        return {**data, 'id': id} if updated else None  # Devuelve los datos actualizados o None si no se encontró.
    except Exception as e:
        raise Exception(f"Error al actualizar la reserva: {str(e)}")  # Maneja errores.

# Función para eliminar una reserva.
def delete_reserva(id):
    try:
        conn = get_db()  # Obtiene la conexión a la base de datos.
        cursor = conn.cursor()  # Crea un cursor para ejecutar comandos SQL.
        cursor.execute('DELETE FROM reservas WHERE id = ?', (id,))  # Elimina una reserva específica.
        conn.commit()  # Guarda los cambios.
        deleted = cursor.rowcount > 0  # Verifica si se eliminó alguna fila.
        conn.close()  # Cierra la conexión.
        return deleted  # Devuelve True si se eliminó, False si no.
    except Exception as e:
        raise Exception(f"Error al eliminar la reserva: {str(e)}")  # Maneja errores.