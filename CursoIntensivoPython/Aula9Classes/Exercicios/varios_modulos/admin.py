from CursoIntensivoPython.Aula9Classes.Exercicios.varios_modulos.usuario import User


class Privileges():
    def __init__(self):

        self.privilegios = ['Pode acessar informacaoes dos usarios',
                            'Pode adicionar um post',
                            'Pode banir um usuario.',
                            'Pode deletar um post.',
                            'Pode desbanir um usuario.']

    def mostra_previlegios(self):
        print('\nPrivilegios do Admin:')
        for vantagem in self.privilegios:
            print(f'\t- {vantagem}')

class Admin(User):
    def __init__(self, nome, apelido, nome_do_usuario, email,
                 localidade, idade, sexo):
        super().__init__(nome, apelido, nome_do_usuario, email,
                 localidade, idade, sexo)
        self.privilegios = Privileges()