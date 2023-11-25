async function obtenerDatosEleccion(url) {
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error('Error en la solicitud:', error);
    }
}

// Ejemplo de uso
const urlPresidencial2017 = 'http://127.0.0.1:55485/eleccion/presidencial/2017';
obtenerDatosEleccion(urlPresidencial2017).then(datos => {
    console.log('Datos Elección Presidencial 2017:', datos);
});
