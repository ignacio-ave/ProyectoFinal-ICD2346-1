
# Dashboard de Visualización de Votaciones 🗳️

Este proyecto, desarrollado por Ignacio Astorga y Vicente Hernández para la asignatura ICD2346-1, implementa un dashboard para la visualización interactiva de datos electorales en Chile. La aplicación se compone de un backend en Python que utiliza Flask para servir una API, y un frontend que está en desarrollo para la interacción del usuario.

## Descripción de la API

La API proporciona un mecanismo para consultar resultados electorales históricos en Chile, entregando la información de manera estructurada y lista para su visualización y análisis.

## Endpoints de la API

La API dispone de dos endpoints principales:

1) /eleccion/presidencial/<int:anio>/<string:instancia>
Descripción: Devuelve los resultados de las elecciones presidenciales para un año específico y su instancia.
Datos: Resultados por región y candidato.

2) /eleccion/presidencial/region/<int:anio>/<int:Id Region>/<string:instancia>
Descripción: Obtiene los resultados presidenciales por región específica, año e instancia.
Datos: Resultados de una sola región y la votación de las provincias asociadas.


### Formato de Respuesta

La API responde con un objeto JSON estructurado que incluye detalles de la elección, así como un listado de candidatos y sus respectivos votos, tanto por región como totales.

## Uso de la API

Para hacer uso de la API, envíe solicitudes GET a los endpoints proporcionados. A continuación, un ejemplo de cómo obtener los datos de la elección presidencial para el año 2000:

```javascript
fetch('http://<tu-servidor>/eleccion/presidencial/2000')
  .then(response => response.json())
  .then(data => console.log(data));
```

## Instalación y Configuración 

Siga estas instrucciones para clonar el repositorio y ejecutar la aplicación en su entorno local.


-git clone https://github.com/tu_usuario/ProyectoFinal-ICD2346-1.git
cd ProyectoFinal-ICD2346-1


### Backend

El backend está diseñado para ser robusto y eficiente, procesando y serializando los datos para su consumo a través de la API RESTful.

### Frontend 

-Para la creación del mapa hicimos uso de un svg de chile sacado de la página www.simplemaps.com, el mapa cuenta con 15 regiones por lo que debido a que en algunas elecciones aún no se contaba con las 15 regiones los datos no se representan.

-Dependiendo de la elección que se elija en el selector se mostrará un gráfico de torta sacado de google Charts que representa la cantidad de votos de los candidatos a nivel nacional.

-Dependiendo de donde se haga click en el mapa de chile se mostraran las estadisticas de los candidatos por region en una tabla.

-También se mostrará al ganador de la elección en cuestión con su nombre y una foto, la fota es sacada de de un url

### Ejecucion del proyecto

Para ejecutar el proyecto solo se necesitan dos pasos, los cuales serian correr api.py que se encuentra dentro de backend y abrir web4.html


-------
Desarrollado por Ignacio Astorga y Vicente Hernández para la asignatura ICD2346-1 en la Pontificia Universidad Católica de Valparaíso
