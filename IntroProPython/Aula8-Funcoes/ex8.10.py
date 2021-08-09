def fibonaci(limite):
    fim = 0
    primeiro = 0
    segundo = 1
    print(f'{primeiro}; {segundo}', end='; ')
    while fim != limite:
        soma = primeiro + segundo
        print(f'{soma}', end='; ')
        primeiro = segundo
        segundo = soma
        fim += 1

limite = 15
fibonaci(limite)