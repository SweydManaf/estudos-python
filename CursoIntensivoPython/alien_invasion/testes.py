def load_max_point():
    """Carrega os pontos maximos."""
    while True:
        try:
            file = open('max_points.txt', 'r')
        except:
            print('Nao consegui carregar...')
            file = open('max_points.txt', 'w')
            print('Criei novo arquivo.')
        else:
            return file.readline()

def update_points(points):
    """Atualiza os pontos maximos."""
    file = open('max_points.txt', 'w')
    file.write(str(points))

print(load_max_point())
update_points(555)
print(load_max_point())