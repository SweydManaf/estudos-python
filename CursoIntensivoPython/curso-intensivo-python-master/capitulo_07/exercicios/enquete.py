respostas = dict()

# Flag para manter a enquete ativa.
enquete_ativa = True
while enquete_ativa:
    # Pede o nome do usuário.
    while True:
        nome = str(input('\nQual é o seu nome? ')).strip()
        if nome.isalpha():
            break
        print('Por favor, digite o seu nome novamente.')
    # Pergunta o nome do lugar que o usuário gostaria de visitar.
    while True:
        prompt = 'Se pudesse visitar um lugar do mundo, para onde você iria? '
        resposta = str(input(prompt)).strip()
        if resposta.replace(' ', '').isalpha():
            break
        print('Por favor, digite o lugar novamente.\n')
    # Armazena a resposta no dicionário.
    respostas[nome] = resposta

    # Pergunta se outra pessoa vai responder à enquete.
    while True:
        prompt = 'Gostaria de deixar outra pessoa responder? [S/N] '
        repetir = str(input(prompt)).upper().strip()
        if repetir.isalpha():
            if repetir in 'SN':
                break
        print('Digite apenas "S" ou "N".\n')
    if repetir == 'N':
        enquete_ativa = False

# Mostra os resultados.
print('\n\t=== Resultados da Enquete ===')
for nome, resposta in respostas.items():
    print(f'{nome.title()} gostaria de ir visitar {resposta.title()}.')
