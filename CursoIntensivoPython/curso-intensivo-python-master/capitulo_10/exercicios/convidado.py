import modulo_arquivos as ma

arquivo = 'arquivos_de_texto/convidado.txt'

convidado = str(input('Seja bem vindo!\nDigite aqui o seu nome: ')).strip()
ma.escrever_nome_do_convidado(arquivo, convidado)

conteudo = ma.ler_arquivo_inteiro(arquivo)

if convidado.title() in conteudo:
    print('\nNome adicionado na lista de convidados com sucesso!')
