# Technical Test: Python/Node
 
# PDF Email API

Esta es una API RESTful para recibir un archivo PDF, extraer las primeras 30 líneas y enviar el contenido extraído a una dirección de correo electrónico proporcionada.

## Instalación

1. Clona el repositorio:
    ```sh
    git clone <repository-url>
    cd pdf_email_api
    ```

2. Crea y activa un entorno virtual:
    ```sh
    python3 -m venv venv
    source venv/Scripts/activate
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```


## Ejecución

1. Inicia el servidor de desarrollo:
    ```sh
    python manage.py runserver
    ```

## Uso

Envía una solicitud POST a `http://localhost:8000/` con el archivo PDF y la dirección de correo electrónico en el cuerpo de la solicitud.

Ejemplo usando `curl`:
```sh
curl -X POST http://localhost:8000/ -F 'file=@path/to/your/file.pdf' -F 'email=example@example.com'