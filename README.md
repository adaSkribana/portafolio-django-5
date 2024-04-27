# PortafolioDjangoAutenticacion

# Proyecto de Autenticación Django

Este proyecto es una aplicación Django que incluye un sistema de autenticación con diferentes roles de usuario y permisos.

## Clonar el Proyecto

Sigue estos pasos para clonar el proyecto en tu máquina local:

1. Abre una terminal o línea de comandos en tu computadora.
2. Navega hasta el directorio donde deseas clonar el proyecto.
3. Ejecuta el siguiente comando para clonar el repositorio:

   ```
   git clone <URL del repositorio>
   ```

   Reemplaza `<URL del repositorio>` con la URL real del repositorio de Git.

## Configuración del Entorno Virtual

Una vez que hayas clonado el proyecto, es una buena práctica configurar un entorno virtual para instalar las dependencias del proyecto de manera aislada. Sigue estos pasos para configurar y activar un entorno virtual:

1. Navega hasta el directorio raíz del proyecto clonado en tu terminal.
2. Ejecuta el siguiente comando para crear un entorno virtual:

   ```
   python -m venv venv
   ```

3. Activa el entorno virtual con el siguiente comando:

   - En Windows:

     ```
     venv\Scripts\activate
     ```

   - En macOS y Linux:

     ```
     source venv/bin/activate
     ```

## Instalación de Dependencias

Después de activar el entorno virtual, instala las dependencias del proyecto ejecutando el siguiente comando:

```
pip install -r requirements.txt
```

## Ejecutar la Aplicación

Una vez instaladas las dependencias, puedes ejecutar la aplicación Django localmente. Asegúrate de estar en el directorio raíz del proyecto y ejecuta el siguiente comando:

```
python manage.py runserver
```

Esto iniciará el servidor de desarrollo de Django. Abre tu navegador web y navega a la dirección `http://127.0.0.1:8000/` para ver la aplicación en funcionamiento.

