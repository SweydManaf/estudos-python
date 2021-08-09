import unittest

from classe_funcionario import Funcionario


class TestCasosDeAumentosParaFuncionario(unittest.TestCase):
    """Testes para a classe Funcionario."""

    def setUp(self):
        """
        -> Cria uma instância com o nome, sobrenome e um salário
        de um funcionário, para ser usado nos testes.
        """
        self.funcionario = Funcionario('william', 'rodrigues', 27000)

    def test_dar_aumento_default(self):
        """
        -> Testa se o salário anual do funcionário foi somado com
        o valor padrão de aumento, 5000.
        """
        self.funcionario.dar_aumento()
        self.assertEqual(self.funcionario.sal_anual, 32000)

    def test_dar_aumento_customizado(self):
        """
        -> Testa se o salário anual do funcionário foi somado com
        o valor customizado de aumento.
        """
        self.funcionario.dar_aumento(2550)
        self.assertEqual(self.funcionario.sal_anual, 29550)


if __name__ == '__main__':
    unittest.main()
