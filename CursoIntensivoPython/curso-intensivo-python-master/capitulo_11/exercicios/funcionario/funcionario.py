from classe_funcionario import Funcionario


while True:
    print("\nDigite 'sair' para interromper o programa.")
    # Pergunta o primeiro nome do funcionário.
    while True:
        nome = str(input('\nPrimeiro nome do funcionário: ')).lower().strip()
        if nome.replace(' ', '').isalpha() and nome != '':
            break
        print('Por favor, digite o nome novamente.')
    if nome == 'sair':
        break

    # Pergunta o sobrenome do funcionário.
    while True:
        sobrenome = str(input('Sobrenome do funcionário: ')).lower().strip()
        if sobrenome.isalpha() and nome != '':
            break
        print('Por favor, digite o sobrenome novamente.\n')
    if sobrenome == 'sair':
        break

    # Pergunta o salário do funcionário.
    while True:
        try:
            salario = float(input('Salário anual do funcionário: R$'))
        except ValueError:
            print('ERRO: digite um valor válido para o salário.\n')
        else:
            break

    funcionario = Funcionario(nome, sobrenome, salario)
    print(f"""\nMENU DE OPÇÕES
    1 - Verificar salário anual de {funcionario.nome_completo}
    2 - Dar aumento para {funcionario.nome_completo}""")

    while True:
        try:
            opcao = int(input('Escolha uma das opções: '))
        except ValueError:
            print('ERRO: digite um valor inteiro válido.\n')
        else:
            if opcao in [1, 2]:
                if opcao == 1:
                    funcionario.mostrar_sal_anual(formatar=True)
                else:
                    while True:
                        try:
                            valor = float(input(
                                '\nDigite o valor do aumento: R$'))
                        except ValueError:
                            print('ERRO: digite um valor '
                                  'válido para o aumento.')
                        else:
                            print('Salário antes do aumento: '
                                  f'R${funcionario.sal_anual:.2f}')
                            funcionario.dar_aumento(valor)
                            print('Salário depois do aumento: '
                                  f'R${funcionario.sal_anual:.2f}')
                            break
            else:
                print('Digite apenas uma das opções do menu.\n')
                continue
            break
