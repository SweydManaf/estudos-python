import unittest
from CursoIntensivoPython.Aula11Debug.name_fuction import get_formatted_name

class TestCase(unittest.TestCase):
    """Testes para 'name_fuction.py'"""

    def test_first_last_name(self):
        """Nomes como 'Sweyd Abdul' funcionam? """
        formatted_name = get_formatted_name('Sweyd', 'Abdul')
        self.assertEqual(formatted_name, 'Sweyd Abdul')

    def test_first_last_middle_name(self):
        '''Nome como "Wolfgang Amadeus Mozart" funcionam?'''
        formatted_name = get_formatted_name('wolfgang',
                                            'mozart',
                                            'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()
