# Proyecto Django API de Silabuz Unidad 5

[![N|Solid](https://www.django-rest-framework.org/img/logo.png)](https://django-api-private-production.up.railway.app/)

## Descripcíon
- El Proyecto de Django API tiene un Register y Login.
- El Proyecto de Django API tiene CRUD en Servios, Pago del Servicio y Expiracion de Pago.
- Tiene que estar Autenticado(Logeao) para listar o crear Servios, Pago del Servicio y Expiracion de Pago.
- Solo los Administradores tienen acceso a editar o elimnar Servios y Pago del Servicio.
- La Lista de Servicios, Pago del Servicio y Expiracion de Pago tiene una paginacion de 100.
- La Lista de Pago de Servicio tiene filtro fecha de pago y fecha de expiración.
- EL usuario tendra acceso a 3 request a la vista de Pago del Servicio, y 7 request en Servicios y Expiracion de Pago.
- Para visualizar la Documentacion esta en http://127.0.0.1:8000/swagger/ o http://127.0.0.1:8000/redoc/ 
- Para poder Registrarse esta en http://127.0.0.1:8000/users/signup/
- Para poder Logearte esta en http://127.0.0.1:8000/users/login/

## Requisitos
- Python 3.10

## Instalacion
#### Crear entorno Virtual
```bash
python3 -m venv env
```
#### Activar el entorno Virtual (Windows)
```bash
env\Scripts\activate.bat
```
#### Instalar los Requisitos
```bash
pip install -r requirements.txt
```
#### Migrar Base de Datos
La base esta en SQLite
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
#### Iniciar Proyecto
```bash
python manage.py runserver
```
