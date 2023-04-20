# -*- coding: utf-8 -*-
"""Pruebas calculadora AVANZADA"""

import unittest
from src.proyecto.funciones import hello_world


class TestFunciones(unittest.TestCase):
    """Test Ejemplo TDD"""
    def test_hello_world(self):
        """Test Hello_world"""
        self.assertEqual(hello_world(), 'hello world')


if __name__ == '__main__':
    unittest.main()
