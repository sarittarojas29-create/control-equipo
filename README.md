# Control de Equipo

Aplicación web para llevar el control de equipo y material asignado a personas: quién lo tiene, desde cuándo y si ya fue devuelto. Está inspirada en mi experiencia como encargada de depósito de equipo y vestuario. 

## Funciones

- Alta de equipo con su responsable
- Fecha de entrega registrada automáticamente
- Estado del equipo: entregado o devuelto
- Botón para marcar una devolución
- Borrado de registro
- Resaltado de los equipos que llevan 7 días o más sin devolverse

## Tecnologías

- Python
- Flask (servidor web y plantillas Jinja2)
- SQLite (base de datos)
- HTML

## Cómo ejecutarlo

1.- Clonar el repositorio y entrar a la carpeta. 
2.- Crear y activar un entorno virtual: 'python -m venv venv'
3.- Instalar las dependencias: 'pip install -r requeriment.txt'
4.- Ejecutar la app: 'python app.py'
5.- Abrir 'http://127.0.0.1:5000' en el navegador.

La base de datos se crea sola la primera vez que se ejecuta. 

## Capturas


## Qué aprendí

Construir una aplicación completa con backend, base de datos y formulario. Practiqué rutas, consultas SQL (SELECT, INSERT, UPDATE, DELETE), plantilla, uso de entornos visuales y control de versiones con Git. 