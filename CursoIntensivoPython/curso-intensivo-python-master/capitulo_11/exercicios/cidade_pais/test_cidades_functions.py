import unittest

import cidade_pais.cidade_funcoes as cf


class TestesCidadeFuncoes(unittest.TestCase):
    """Testes para 'cidade_funcoes.py'."""

    def test_cidade_pais(self):
        """Resultado esperado: 'Santiago, Chile'."""
        cidade_pais = cf.cidade_pais('santiago', 'chile')

        self.assertEqual(cidade_pais, 'Santiago, Chile')

    def test_cidade_pais_populacao(self):
        """Resultado esperado: 'Santiago, Chile – população 5000000'."""
        cidade_pais_populacao = cf.cidade_pais(
            'santiago', 'chile', populacao=5000000)

        self.assertEqual(
            cidade_pais_populacao,
            'Santiago, Chile - população 5000000'
        )


if __name__ == '__main__':
    unittest.main()
