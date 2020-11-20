import unittest
from django.test import TestCase
from models import Server



class testServer (unittest.TestCase):

    def test_nombre_server(self):
        result = Server ('euw')
        self.assertEqual(result, 'euw')
