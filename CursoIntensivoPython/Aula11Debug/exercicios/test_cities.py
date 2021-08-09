import unittest
from CursoIntensivoPython.Aula11Debug.exercicios.city_functions import city_fuctions

class TestCase(unittest.TestCase):
    def test_city(self):
        '''Santiago, Chile - populacao 500000 funcionam?'''
        nome = city_fuctions('Santiago', 'chile', 500000)
        self.assertEqual(nome, 'Santiago, Chile - populacao 500000')

unittest.main()
