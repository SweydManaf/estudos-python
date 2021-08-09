prompt = '\tÉ múltiplo de 10?'
prompt += '\nDigite um número: '
try:
    numero = int(input(prompt))
except (ValueError, TypeError):
    print('ERRO: digite um número inteiro válido.')
else:
    if numero > 0:
        if numero % 10 == 0:
            print(f'\nO número {numero} é divisível por 10.\n'
                  'Portanto é múltiplo de 10!')
        else:
            print(f'\nO número {numero} não é divisível por 10.\n'
                  'Portanto não é múltiplo de 10!')
    else:
        print('Digite um número positivo maior que 0.')
finally:
    print('\nQue fique claro, um número é múltiplo de outro se o resto da '
          'divisão entre eles for 0.')
