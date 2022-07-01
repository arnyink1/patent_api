# Kibernum API

Kibernum API Service

## Características

* API REST en FastAPI.
* Autentificación simple con variables definidas a traves de JSON Web Token (JWT). Usuario y contraseña = "username" , "password".
* Integración para obtener identificador de placas vehiculares de cliente propio, instanciado desde la identity del JWT.
* http://127.0.0.1:8000/docs#

## Routes

* **login**: Maneja autentificación (JWT).
* **patent**: Maneja recursos API REST de placas patentes.

## Entorno de desarrollo

Para desarrollar:

```bash
cd patent_api-main
python3 -m venv venv
source venv/bin/activate
pip install -r requirements/dev.txt
python main.py
```

## Pytest & Coverage

Testing con reporte en consola y html:

```bash
pytest
coverage run -m pytest
coverage html
```

## Deployment

Deployment mínimo.

```bash
pip install -r requirements.txt
python main.py
```