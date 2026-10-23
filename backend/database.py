# database.py
# Aqui esta toda la conexion con PostgreSQL separada del resto del codigo.
# Las credenciales se leen desde el archivo .env para no escribirlas en main.py

import os
import psycopg
from dotenv import load_dotenv

# Carga las variables del archivo .env
load_dotenv()


def get_connection():
    """Devuelve una conexion nueva a PostgreSQL usando los datos del .env."""
    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )
