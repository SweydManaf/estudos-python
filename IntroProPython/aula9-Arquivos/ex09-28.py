# Nilo Soluction
import pickle

agenda = []
alterada = False
tipos_de_telefone = ['celular', 'fixo', 'residencia', 'trabalho', 'fax']


def pede_nome(padrao=''):
    nome = str(input('Nome: ')).replace('#', '').strip()
    if nome == '':
        nome = padrao
    return nome


def pede_telefone(padrao=''):
    telefone =  str(input('Telefone: ')).replace('#', '').strip()
    if telefone == '':
        telefone = padrao
    return telefone


def pede_tipo_telefone(padrao=''):
    while True:
        tipo = input(f'Tipo de telefone [{",".join(tipos_de_telefone)}]')
        if tipo == '':
            tipo = padrao
        for t in tipos_de_telefone:
            if t.startswith(tipo):
                return t
        else:
            print('Tipo de telefone invalido!')


def pede_email():
    return input('Email: ')


def pede_aniversario():
    return input('Aniversario: ')


def mostra_dados(nome, telefones, email, aniversario):
    print(f'\nNome: {nome.capitalize()}'
          f'\nTelefone(s):')
    for telefone in telefones:
        print(f'\tNumero: {telefone[0]:>15} Tipo: {telefone[1].capitalize()}')
    print(f'Email: {email}\nAniversario: {aniversario}\n')


def pede_nome_arquivo():
    return(input('Nome do arquivo: '))


def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None


def novo():
    global agenda, alterada
    nome = pede_nome()
    for dado in agenda:
        if nome in dado:
            print('Nome ja existe!')
            return
    telefones = []
    while True:
        numero = pede_telefone()
        tipo = pede_tipo_telefone()
        telefones.append( [numero, tipo] )
        if confirma('Confirma que deseja cadastrar outro telefone (S/N): ') is False:
            break
    email = pede_email()
    aniversario = pede_aniversario()
    agenda.append([nome, telefones, email, aniversario])
    alterada = True


def apaga():
    global agenda
    nome = pede_nome()
    p = pesquisa(nome)
    if p != None:
        if confirma('Confirma alteracao (S/N)? '):
            del agenda[p]
            alterada = True
    else:
        print('Nome nao encontrado.')


def altera():
    global alterada
    p = pesquisa(pede_nome())
    if p != None:
        nome, telefones, email, aniversario = agenda[p]
        print('Encotrado: ')
        mostra_dados(nome, telefones, email, aniversario)
        nome = pede_nome(nome)
        for telefone in telefones:
            numero, tipo = telefone
            telefone[0] = pede_telefone(numero)
            telefone[1] = pede_tipo_telefone(tipo)
        email = pede_email()
        aniversario = pede_aniversario()
        if confirma('Confirma alteracao (S/N)? '):
            agenda[p] = [nome, telefones, email,aniversario]
            alterada = True
    else:
        print('Nome nao encontrado.')


def lista():
    print('\nAgenda\n\n------')
    for e in agenda:  # Tambem podia usar o enumerate
        print(f'Posicao: {agenda.index(e)} ', end='')
        mostra_dados(e[0], e[1], e[2], e[3])
    print('------\n')


def le_ultima_agenda_gravada():
    ultima = ultima_agenda()
    if ultima != None:
        leia_arquivo(ultima)


def ultima_agenda():
    try:
        arquivo = open('ultima agenda picke.dat', 'r', encoding='utf-8')
        ultima = arquivo.readline()[:-1]
        arquivo.close()
    except FileNotFoundError:
        return None
    return ultima


def atualiza_ultima(nome):
    arquivo = open('ultima agenda picke.dat', 'w', encoding = "utf-8")
    arquivo.write(f'{nome}\n')
    arquivo.close()


def leia_arquivo(nome_arquivo):
    global agenda, alterada
    arquivo = open(nome_arquivo, 'rb')
    agenda = pickle.load(arquivo)
    arquivo.close()
    alterada = False


def ordena():
    global alterada
    i = 0
    fim = len(agenda)
    while True:
        if i < (fim - 1):
            if agenda[i] > agenda[i + 1]:
                temp = agenda[i + 1]
                agenda[i + 1] = agenda[i]
                agenda[i] = temp
        i += 1
        if i >= fim:
            break
    alterada = True


def le():
    global alterada
    if alterada:
        print('Voce nao salvou a ultima alteracao. Deseja grava-la agora? ')
        if confirma('Confrima garavacao (S/N)? '):
            grava()
    print('Ler\n------')
    nome_arquivo = pede_nome_arquivo()
    leia_arquivo(nome_arquivo)
    atualiza_ultima(nome_arquivo)


def grava():
    global alterada
    if alterada is False:
        print('Voce nao alterou a lista. Deseja grava-la mesmo assim?')
        if confirma('Confirma gravacao (S/N)? '):
            return
    print('Gravar\n------')
    nome_arquivo = pede_nome_arquivo()
    arquivo = open(nome_arquivo, 'wb')
    pickle.dump(agenda, arquivo)
    arquivo.close()
    atualiza_ultima(nome_arquivo)
    alterada = False


def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f'Valor invalido, favor digitar {inicio} e {fim}')


def confirma(msg):
    while True:
        confirmacao = str(input(msg)).upper()
        if confirmacao != '':
            if confirmacao[0] == 'N':
                return False
            else:
                return True
        else:
            print('Resposta invalida. Escolha S ou N.')


def menu():
    print('''
    1 - Novo
    2 - Altera
    3 - Apaga
    4 - Lista
    5 - Grava
    6 - Le 
    7 - Ordena    
    0 - Sai
''')
    print(f'Nomes na agenda: {len(agenda)} Alterada : {alterada}')
    return valida_faixa_inteiro('Escolha uma opccao: ', 0, 7)

le_ultima_agenda_gravada()

while True:
    opcao = menu()
    if opcao == 0:
        break
    elif opcao == 1:
        novo()
    elif opcao == 2:
        altera()
    elif opcao == 3:
        apaga()
    elif opcao == 4:
        lista()
    elif opcao == 5:
        grava()
    elif opcao == 6:
        le()
    elif opcao == 7:
        ordena()
