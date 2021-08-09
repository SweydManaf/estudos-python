class Televisao:
    def __init__(self, min, max):
        self.ligada = False
        self.canal = 2
        self.cmin = min
        self.cmax = max

    def muda_canal_para_baixo(self):
        if self.canal-1 >= self.cmin:
            self.canal -= 1
        else:
            self.canal = self.cmax

    def muda_canal_para_cima(self):
        if self.canal+1 <= self.cmax:
            self.canal += 1
        else:
            self.canal = self.cmin

print('=== TV DA SALA ===')
tv1 = Televisao(2, 10)
tv1.muda_canal_para_baixo()
print(f'Chanel: {tv1.canal}')
tv1.muda_canal_para_cima()
print(f'Chanel: {tv1.canal}')
print('=== TV DO QUARTO ===')
tv2 = Televisao(min=55, max=60)
tv2.muda_canal_para_baixo()
print(f'Chanel: {tv2.canal}')
tv2.muda_canal_para_cima()
print(f'Chanel: {tv2.canal}')