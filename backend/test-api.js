async function obtenerDatosEleccionPresidencial(anio) {
    try {
        const response = await fetch(`http://127.0.0.1:5000/eleccion/presidencial/${anio}`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log('Datos de la Elección Presidencial:', data);
    } catch (e) {
        console.error('Error al obtener datos de la elección presidencial:', e);
    }
}

async function obtenerDatosEleccionSenadores(anio) {
    try {
        const response = await fetch(`http://127.0.0.1:5000/eleccion/senadores/${anio}`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log('Datos de la Elección de Senadores:', data);
    } catch (e) {
        console.error('Error al obtener datos de la elección de senadores:', e);
    }
}

// Ejecutar las funciones de prueba
obtenerDatosEleccionPresidencial(1989);
obtenerDatosEleccionSenadores(2017);
