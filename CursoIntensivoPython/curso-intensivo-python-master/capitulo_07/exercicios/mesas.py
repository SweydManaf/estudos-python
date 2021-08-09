try:
    pessoas = int(input('Quantas pessoas estão em seu grupo para jantar? '))
except (ValueError, TypeError):
    print('ERRO: digite um número inteiro válido.')
else:
    if pessoas > 8:
        print('\nEstamos cheios, por favor esperem um pouco a mesa de vocês.')
    else:
        print('\nA mesa de vocês já está pronta!')
finally:
    print('Obrigado pela preferência!')
