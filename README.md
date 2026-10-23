# U2 T3 - API GET de catalogo de videojuegos

Backend en Python con FastAPI que se conecta a la base `game_library` de PostgreSQL (creada en la tarea U2 T2).

## Estructura

```
backend/
├── main.py            # endpoints de la API
├── database.py        # conexion a PostgreSQL
├── .env               # credenciales (no se sube a GitHub)
├── .env.example       # ejemplo de credenciales
└── requirements.txt   # dependencias
```

## Requisitos

- Python 3.10 o mas reciente
- PostgreSQL con la base `game_library` ya creada (tarea U2 T2)

## Como ejecutarlo

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Luego abre http://127.0.0.1:8000/docs para probar los endpoints.

## Endpoints

- `GET /` -> mensaje de bienvenida
- `GET /games` -> todos los videojuegos
- `GET /games/{id}` -> un videojuego por id
- `GET /games/genre/{genre}` -> videojuegos por genero (extra)
- `GET /developers` -> todos los desarrolladores
- `GET /developers/{id}` -> un desarrollador por id

## Nota

El archivo `.env` guarda usuario y contraseña de PostgreSQL. No se sube al repositorio por seguridad (esta en `.gitignore`). Usa `.env.example` como base.
