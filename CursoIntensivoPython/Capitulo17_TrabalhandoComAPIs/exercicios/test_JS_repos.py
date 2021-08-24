import unittest
import JS_repos as jp

class TestCase(unittest.TestCase):
    """Testes para 'JS_repos.py"""
    def setUp(self):
        """Chama todas as funćões para aqui, e testa cada."""
        self.r = jp.callAPI('javascript')
        self.repo_dicts = jp.getData(self.r)
        self.repo_dict = self.repo_dicts[0]
        self.names, self.plot_dicts = jp.getDataToPlot(self.repo_dicts)

    def test_get_response(self):
        """Testa se há uma resposta valida."""
        self.assertEqual(self.r.status_code, 200)

    def test_repo_dict(self):
        """Testa os dados obtidos."""
        # Testa se há 30 repositórios
        self.assertEqual(len(self.repo_dicts), 30)

if __name__ == '__main__':
    unittest.main()