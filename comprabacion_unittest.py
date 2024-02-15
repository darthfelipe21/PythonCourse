"""Las pruebas se realizan en archivos independientes,
y debe importarse tanto el módulo que se desea evaluar
como el paquete incorporado de unittest."""


import unittest
import pylint_unittest


class ProbarUnittest(unittest.TestCase):

    def test_mayusculas(self):   # El metodo debe empezar con "test" para que unittest lo reconozca
        palabra = "buen dia"
        result = pylint_unittest.todo_mayusculas(palabra)
        self.assertEqual(result, "Buen Dia")  # Segundo parametro es el resultado esperado


if __name__ == '__main__':
    unittest.main()
