import unittest
from CursoIntensivoPython.Aula11Debug.exercicios.funcionario import Employee

class TestCase(unittest.TestCase):
    """Teste para classe dicionario"""

    def setUp(self):
        """Cria uma instancia para ser usado nos testes"""
        self.nadir = Employee('Nadir', 'Ilal', 200)

    def test_give_default_raise(self):
        """Testa se o salario anual foi somado com o aumento padrao"""

        self.nadir.giv_raise()
        self.assertEqual(self.nadir.salario, 5200)

    def test_give_custom_raise(self):
        """Testa se o salario anual foi somado com o aumento diferente"""
        self.nadir.giv_raise(100)
        self.assertEqual(self.nadir.salario, 300)


unittest.main()