*FORMAS DE INICIARLO:
COMENZAR EJECUTANDO EL QUERY DEL SQL
DESPUES EJECUTAR EL APP.PY DE LA CARPETA "Tienda"
DESPUES EJECUTAR LA AUTOMATIZACION.PY DE LA CARPETA AUTOMATIZACION


TiendaAxM: Automatización de Compras en Línea (HU)

Como usuario, quiero recibir alertas por correo electrónico cuando los precios de los productos bajen en la tienda en línea, para aprovechar 
las mejores ofertas y ahorrar dinero.

Solución Proporcionada
Para abordar esta necesidad, creamos un proyecto de automatización utilizando Python y Selenium. El proyecto consta de los 
siguientes componentes principales:

Página Web Simulada de Tienda en Línea:

Utilizamos HTML, CSS y Flask para crear una página web simulada de una tienda en línea, denominada "TiendaAxM". La página web muestra 
una lista de productos con sus precios, descripciones y otras características.

Script de Automatización de Python:

Implementamos un script en Python utilizando la biblioteca Selenium para automatizar la tarea de verificar los precios de los productos en la tienda en línea.
El script extrae los precios de los productos y los compara con precios anteriores almacenados en un archivo JSON.
Configuramos el script para enviar alertas por correo electrónico cuando se detectan cambios significativos en los precios.
Detalles de Implementación
Creación de la Página Web:

Diseñamos y creamos la página web simulada de la tienda en línea utilizando HTML y CSS.
Utilizamos el framework Flask para desarrollar la lógica del servidor y manejar las solicitudes HTTP.
Automatización con Selenium:

Implementamos un script en Python para la automatización de la verificación de precios.
Utilizamos Selenium para interactuar con el navegador web, extraer datos de la página web y enviar correos electrónicos.
Gestión de Datos con JSON:

Utilizamos archivos JSON para almacenar y recuperar datos, como precios anteriores de productos, de manera eficiente.
Herramientas Utilizadas
HTML, CSS y Flask: Para la creación de la página web simulada de la tienda en línea y la lógica del servidor.
Python y Selenium: Para la automatización de la verificación de precios en la tienda en línea.
JSON: Para la gestión eficiente de datos, como precios anteriores de productos.
SMTP: Para el envío de alertas por correo electrónico cuando se detectan cambios significativos en los precios.