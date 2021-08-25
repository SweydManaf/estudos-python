from unittest import TestCase
from fila import Fila

class TestFila(TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        self.fila = Fila()
        print('setup')

    def tearDown(self):
        print('teardown')


    def test_quando_5_entrar_na_5_deve_estar_no_final_da_fila(self):
        entrada = 5
        saida_esperada = 5

        # quando 5 entrar na fila
        self.fila.entrar(entrada)
        self.fila.entrar(10)

        # então 5 deve estar na fila
        self.assertEqual(saida_esperada, self.fila[-1])
        print(self.fila)

    def test_quando_10_entrar_na_10_deve_estar_no_final_da_fila(self):
        entrada = 10
        saida_esperada = 10

        # quando 5 entrar na fila
        self.fila.entrar(entrada)
        self.fila.entrar(10)

        # então 5 deve estar na fila
        self.assertEqual(saida_esperada, self.fila[-1])
        print(self.fila)

