# Technical Test: Python/Node
 
# PDF Email API

Esta es una API RESTful para recibir un archivo PDF, extraer las primeras 30 líneas y enviar el contenido extraído a una dirección de correo electrónico proporcionada.

## Instalación

1. Clona el repositorio:
    ```sh
    git clone <repository-url>
    ```

2. Desde la terminal activa el entorno virtual:
    ```sh
    venv/Scripts/activate
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

## Configuración de Correo Electrónico

Para configurar el envío de correos electrónicos desde tu aplicación, necesitarás proporcionar las credenciales de tu cuenta de correo electrónico en el archivo `settings.py` que se encuentra en la carpeta `config`. Sigue estos pasos para configurar tu correo electrónico:

1. Abre el archivo `settings.py` en tu proyecto.

2. Busca las siguientes variables relacionadas con el correo electrónico:

    ```python
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    DEFAULT_FROM_EMAIL = 'tu_correo@example.com'
    ```

3. Completa las siguientes variables con la información de tu cuenta de correo electrónico:

    - `EMAIL_HOST`: El servidor SMTP de tu proveedor de correo electrónico. Por ejemplo, para Gmail, usa `smtp.gmail.com`. Para Hotmail, usa `smtp.live.com`.

    - `EMAIL_HOST_USER`: Tu dirección de correo electrónico completa.

    - `EMAIL_HOST_PASSWORD`: La contraseña de tu cuenta de correo electrónico.


4. Guarda los cambios en el archivo `settings.py`.

Con estos pasos, tu aplicación estará configurada para enviar correos electrónicos utilizando tu cuenta de correo electrónico.


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