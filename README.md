# ProyectoFinal-ICD2346-1

# Dashboard de Visualización de Votaciones 🗳️

Este proyecto es el trabajo final para la asignatura de Paradigma en Computación, donde desarrollamos una aplicación web para visualizar datos de votaciones. Utilizamos técnicas de programación orientada a objetos y funciones de orden superior, con un backend en Python y un frontend en JavaScript.

## Descripción del Proyecto 📜

El objetivo es crear un dashboard interactivo que permita a los usuarios explorar datos de votaciones a través de diferentes visualizaciones gráficas. El backend se encarga de procesar y servir los datos, mientras que el frontend se centra en presentar esta información de manera intuitiva y dinámica.


## Backend 🛠️

El backend está construido con:

- **Flask**: Un micro-framework de Python para servir nuestra API y manejar la lógica del servidor.
- **SQL/NoSQL**: Seleccionaremos la base de datos en función de la estructura de los datos y las necesidades de consulta.

### Funcionalidades Clave:

- `leer_datos()`: Leer archivos de datos y cargarlos en la base de datos.
- `procesar_datos()`: Procesar y organizar los datos para su visualización.
- `api/datos`: Endpoint para servir datos filtrados al frontend.

## Frontend 🎨

El frontend se encargará de:

- **Interactividad**: Permitir a los usuarios seleccionar filtros y ver los resultados actualizados.
- **Visualización de Datos**: Usar Chart.js o Highcharts para mostrar los datos en gráficos interactivos.

### Componentes Principales:

- `FiltroDeVotaciones`: Componente para seleccionar diferentes criterios de votación.
- `VisualizadorDeDatos`: Componente para mostrar los gráficos basados en los datos seleccionados.

## Cómo Iniciar 🚀

Aquí irían las instrucciones para clonar el repositorio, instalar dependencias, configurar la base de datos, y correr la aplicación localmente.

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
# Instrucciones para configurar y ejecutar
