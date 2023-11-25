import requests
import json
import unittest

class TestEleccionAPI(unittest.TestCase):

    def setUp(self):
        self.base_url = f"http://127.0.0.1:{input('Ingrese el puerto en el que se ejecuta la API: ')}"
        self.años_para_testear = [2017, 2020]  # Aquí puedes añadir más años

    def test_eleccion_presidencial(self):
        for año in self.años_para_testear:
            with self.subTest(año=año):
                response = requests.get(f"{self.base_url}/eleccion/presidencial/{año}")
                self.assertEqual(response.status_code, 200)
                with open(f'presidencial_{año}.json', 'w') as file:
                    json.dump(response.json(), file)

    def test_eleccion_senadores(self):
        for año in self.años_para_testear:
            with self.subTest(año=año):
                response = requests.get(f"{self.base_url}/eleccion/senadores/{año}")
                self.assertEqual(response.status_code, 200)
                with open(f'senadores_{año}.json', 'w') as file:
                    json.dump(response.json(), file)

if __name__ == '__main__':
    unittest.main()
