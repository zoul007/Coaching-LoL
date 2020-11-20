import unittest
from django.test import TestCase
from views import image_gallery

class testImage (unittest.TestCase):

    def test_nombre_server(self):
        result = Server ('euw')
        self.assertEqual(result, 'euw')
