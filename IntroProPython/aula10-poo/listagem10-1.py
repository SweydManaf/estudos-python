class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2


tv = Televisao()
tv_sala = Televisao()
tv_sala.ligada = True
tv_sala.canal = 4
print(tv.ligada)
print(tv.canal)
print(tv_sala.ligada)
print(tv_sala.canal)