import unittest
from api import app  # Importa la aplicación Flask que quieres probar

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()  # Crea un cliente de prueba para interactuar con la aplicación

    def test_get_eleccion_presidencial(self):
        response = self.app.get('/eleccion/presidencial/2017')  # Realiza una solicitud GET a la ruta /eleccion/presidencial/2017
        self.assertEqual(response.status_code, 200)  # Verifica que la respuesta sea 200 (éxito)
        # También puedes verificar el contenido de la respuesta si es necesario

    def test_get_eleccion_senadores(self):
        response = self.app.get('/eleccion/senadores/2017')  # Realiza una solicitud GET a la ruta /eleccion/senadores/2017
        self.assertEqual(response.status_code, 200)  # Verifica que la respuesta sea 200 (éxito)
        # También puedes verificar el contenido de la respuesta si es necesario

    def test_get_segunda_instancia(self):
        response = self.app.get('/eleccion/presidencial/segunda_instancia/2017')  # Realiza una solicitud GET a la ruta /eleccion/presidencial/segunda_instancia/2017
        self.assertEqual(response.status_code, 200)  # Verifica que la respuesta sea 200 (éxito)
        # También puedes verificar el contenido de la respuesta si es necesario

    # Agrega más pruebas para otras rutas si es necesario

if __name__ == '__main__':
    unittest.main()
