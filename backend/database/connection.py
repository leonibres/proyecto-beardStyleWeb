import sqlite3  # Importa SQLite para manejar la base de datos.
import os  # Importa os para verificar la existencia del archivo de la base de datos.

DATABASE = 'reservas.db'  # Nombre del archivo de la base de datos.

# Función para obtener una conexión a la base de datos.
def get_db():
    try:
        # Si la base de datos no existe, inicializarla.
        if not os.path.exists(DATABASE):
            init_db()
        conn = sqlite3.connect(DATABASE)  # Conecta a la base de datos.
        conn.row_factory = sqlite3.Row  # Configura para devolver filas como diccionarios.
        return conn
    except sqlite3.Error as e:
        raise Exception(f"Error al conectar con la base de datos: {str(e)}")  # Maneja errores de conexión.

# Función para inicializar la base de datos.
def init_db():
    try:
        conn = sqlite3.connect(DATABASE)  # Conecta a la base de datos.
        cursor = conn.cursor()  # Crea un cursor para ejecutar comandos SQL.
        # Crea la tabla 'reservas' si no existe.
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS reservas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                fecha TEXT NOT NULL,
                servicio TEXT NOT NULL
            )
        ''')
        conn.commit()  # Guarda los cambios.
    except sqlite3.Error as e:
        raise Exception(f"Error al inicializar la base de datos: {str(e)}")  # Maneja errores de inicialización.
    finally:
        if 'conn' in locals():
            conn.close()  # Cierra la conexión.
