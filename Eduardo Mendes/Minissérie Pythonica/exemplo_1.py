# funćão nomeada
def funcao_nomeada():
    return 'Oi'


# funcao anonimas
anonima = lambda: 'Oi'


class FuncaoClasse:
    def __call__(self):
        return 'Oi'

print(type(anonima))
print(type(funcao_nomeada()))
print(type(FuncaoClasse()))