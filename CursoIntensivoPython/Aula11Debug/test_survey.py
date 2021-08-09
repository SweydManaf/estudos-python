import unittest
from CursoIntensivoPython.Aula11Debug.survey import AnonymousSurvey

class TestAnonymouSurvey(unittest.TestCase):
    """Testes para a classe AnonymousSurvey"""

    def setUp(self):
        """Cria uma pesquisa e um conjunto de respostas
        que poderao ser usados em todos os metodos de teste."""

        question = 'What language did you first learn to speak?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """Testa se uma unica resposta e armazenada de forma
         apropriada"""

        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Testa se tres respostas individuais sao armazenadas de
         forma apropriada"""

        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()