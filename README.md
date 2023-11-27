
# Dashboard de Visualización de Votaciones 🗳️

Este proyecto, desarrollado por Ignacio Astorga y Vicente Hernández para la asignatura ICD2346-1, implementa un dashboard para la visualización interactiva de datos electorales en Chile. La aplicación se compone de un backend en Python que utiliza Flask para servir una API, y un frontend que está en desarrollo para la interacción del usuario.

## Descripción de la API

La API proporciona un mecanismo para consultar resultados electorales históricos en Chile, entregando la información de manera estructurada y lista para su visualización y análisis.

## Endpoints de la API

La API dispone de dos endpoints principales:

1. `/eleccion/presidencial/<int:anio>`:
   - Descripción: Devuelve los resultados de las elecciones presidenciales para un año específico.
   - Datos: Resultados por región y candidato.

2. `/eleccion/presidencial/segunda_instancia/<int:anio>`:
   - Descripción: Verifica si hubo una segunda vuelta en las elecciones presidenciales de un año dado.
   - Datos: Valor booleano dependiendo si hubo o no segunda instancia de votación.

3. `/eleccion/presidencial/region/<int:anio>/<region>`:
   - Descripción: Obtiene los resultados presidenciales por región específica y año.
   - Datos: Resultados de una sola región y la votación de las provincias asociadas.

4. `/eleccion/presidencial/detalle/<int:anio>`:
   - Descripción: Devuelve los resultados de las elecciones presidenciales para un año específico incluyendo provincias y regiones.
   - Datos: Resultados de todas las regiones, con sus provincias y las instancias de votación.


### Formato de Respuesta

La API responde con un objeto JSON estructurado que incluye detalles de la elección, así como un listado de candidatos y sus respectivos votos, tanto por región como totales.

## Uso de la API

Para hacer uso de la API, envíe solicitudes GET a los endpoints proporcionados. A continuación, un ejemplo de cómo obtener los datos de la elección presidencial para el año 2000:

```javascript
fetch('http://<tu-servidor>/eleccion/presidencial/2000')
  .then(response => response.json())
  .then(data => console.log(data));
```

## Instalación y Configuración (No terminado)

Siga estas instrucciones para clonar el repositorio y ejecutar la aplicación en su entorno local.

```bash
git clone https://github.com/tu_usuario/ProyectoFinal-ICD2346-1.git
cd ProyectoFinal-ICD2346-1
# Instalar dependencias (omitido)
# Iniciar el servidor
python api.py
```

## Desarrollo

### Backend

El backend está diseñado para ser robusto y eficiente, procesando y serializando los datos para su consumo a través de la API RESTful.

### Frontend (No terminado)

[Instrucciones y descripción del frontend en desarrollo]


---

Desarrollado por Ignacio Astorga y Vicente Hernández para la asignatura ICD2346-1 en la Pontificia Universidad Católica de Valparaíso
