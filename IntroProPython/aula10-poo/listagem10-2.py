class Televisao:
    def __init__(self):
        self.ligada = True
        self.canal = 2

    def muda_canal_para_baixo(self):
        self.canal -= 1

    def muda_canal_para_cima(self):
        self.canal += 1

tv = Televisao()
tv.muda_canal_para_cima()
tv.muda_canal_para_cima()
print(f'Chanel: {tv.canal}')
tv.muda_canal_para_baixo()
print(f'Chanel: {tv.canal}')