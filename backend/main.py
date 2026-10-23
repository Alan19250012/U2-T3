# main.py
# Backend del catalogo de videojuegos. Solo tiene endpoints de tipo GET.

from fastapi import FastAPI, HTTPException
from database import get_connection

app = FastAPI(
    title="Catalogo de videojuegos",
    description="API para consultar la base game_library de la tarea U2 T2.",
    version="1.0",
)


def filas_como_diccionarios(cursor, filas):
    """Convierte el resultado de una consulta en una lista de diccionarios."""
    columnas = [desc.name for desc in cursor.description]
    return [dict(zip(columnas, fila)) for fila in filas]


@app.get("/")
def inicio():
    """Mensaje de bienvenida con los endpoints disponibles."""
    return {
        "mensaje": "Bienvenido a la API del catalogo de videojuegos",
        "endpoints": [
            "/games",
            "/games/{id}",
            "/games/genre/{genre}",
            "/developers",
            "/developers/{id}",
        ],
        "documentacion": "/docs",
    }


@app.get("/games")
def listar_videojuegos():
    """Devuelve todos los videojuegos registrados en PostgreSQL."""
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, title, genre, price, release_year, developer_id "
                "FROM games ORDER BY id"
            )
            return filas_como_diccionarios(cur, cur.fetchall())


@app.get("/games/genre/{genre}")
def videojuegos_por_genero(genre: str):
    """Devuelve los videojuegos que coinciden con un genero."""
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, title, genre, price, release_year, developer_id "
                "FROM games WHERE genre = %s ORDER BY title",
                (genre,),
            )
            return filas_como_diccionarios(cur, cur.fetchall())


@app.get("/games/{game_id}")
def obtener_videojuego(game_id: int):
    """Devuelve un solo videojuego segun su id, o un error 404 si no existe."""
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, title, genre, price, release_year, developer_id "
                "FROM games WHERE id = %s",
                (game_id,),
            )
            fila = cur.fetchone()
            if fila is None:
                raise HTTPException(status_code=404, detail="Videojuego no encontrado")
            columnas = [desc.name for desc in cur.description]
            return dict(zip(columnas, fila))


@app.get("/developers")
def listar_desarrolladores():
    """Devuelve todos los desarrolladores registrados."""
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, name, country, foundation_year FROM developers ORDER BY id"
            )
            return filas_como_diccionarios(cur, cur.fetchall())


@app.get("/developers/{developer_id}")
def obtener_desarrollador(developer_id: int):
    """Devuelve un solo desarrollador segun su id, o un error 404 si no existe."""
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, name, country, foundation_year "
                "FROM developers WHERE id = %s",
                (developer_id,),
            )
            fila = cur.fetchone()
            if fila is None:
                raise HTTPException(status_code=404, detail="Desarrollador no encontrado")
            columnas = [desc.name for desc in cur.description]
            return dict(zip(columnas, fila))
