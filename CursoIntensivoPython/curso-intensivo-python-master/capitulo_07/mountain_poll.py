responses = dict()

# Define uma flag para indicar que a enquete esta ativa.
polling_active = True
while polling_active:
    # Pede o nome da pessoa e a resposta.
    name = input('\nWhat is your name? ')
    response = input('Which mountain would you like to climb someday? ')
    # Armazena a resposta no dicionário.
    responses[name] = response

    # Descobre se outra pessoa vai responder à enquete.
    repeat = input('Would you like to let another person responde? (yes/no) ')
    if repeat == 'no':
        polling_active = False

# A enquete foi concluída. Mostra os resultados.
print('\n--- Poll Results ---')
for name, response in responses.items():
    print(f'{name} would like to climb {response}.')
