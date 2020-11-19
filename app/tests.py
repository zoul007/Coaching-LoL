from django.test import TestCase
from unittest
from models import *

# Create your tests here.


class testServer (unittest.TestCase):

    def test_nombre_server(self):
        # Cuando se trata de cargar un archivo que no es formato de imagen
        self.assertAlmostEqual(Server("AMéricA"), "América" )

if __name__ == "__main__":
    unittest.main()
