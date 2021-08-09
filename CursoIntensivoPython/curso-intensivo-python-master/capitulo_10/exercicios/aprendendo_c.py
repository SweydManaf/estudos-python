import modulo_arquivos as ma

arquivo = 'arquivos_de_texto/aprendendo_python.txt'

conteudo = ma.ler_arquivo_inteiro(arquivo)
troca_por_c = conteudo.replace('Python', 'C')

print(troca_por_c.rstrip())
