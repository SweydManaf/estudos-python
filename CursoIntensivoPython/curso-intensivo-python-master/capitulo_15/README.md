# Referências Rápidas do Capítulo

- ### Utilização do [_matplotlib_](https://matplotlib.org/)
Exemplos simples de gráficos com o [matplotlib.pyplot](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot)
>- [_mpl_squares.py_](https://github.com/willy-r/curso-intensivo-python/blob/master/capitulo_15/mpl_squares.py)

```
import matplotlib.pyplot as plt`

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

# Define o título do gráfico e nomeia os eixos.
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# Define o tamanho dos rótulos das marcações.
plt.tick_params(axis='both', labelsize=14)

plt.show()
```

<img src='https://github.com/willy-r/curso-intensivo-python/blob/master/capitulo_15/imagens/mpl_squares.png' heigth='500' width='500'>

Utilizando o [matplotlib.pyplot.scatter](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter)
>- [_scatter_squares.py_](https://github.com/willy-r/curso-intensivo-python/blob/master/capitulo_15/scatter_squares.py)

```
import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)

# Define o título do gráfico e nomeia os eixos.
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# Define o tamanho dos rótulos das marcações.
plt.tick_params(axis='both', which='major', labelsize=14)

# Define o intervalo para cada eixo.
plt.axis([0, 1100, 0, 1100000])

plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()
```

<img src='https://github.com/willy-r/curso-intensivo-python/blob/master/capitulo_15/imagens/squares_plot.png' heigth='500' width='500'>

Um exemplo mais completo usando uma classe chamada RandomWalk para randomizar pontos que representem passeios aleatórios.
>- [_random_walk.py_](https://github.com/willy-r/curso-intensivo-python/blob/master/capitulo_15/random_walk.py)

```
class RandomWalk:
    """Uma classe para gerar passeios aleatórios."""

    def __init__(self, num_points=5000):
        """Inicializa os atributo de um passeio."""
        self.num_points = num_points
        # Todos os passeios começam em (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Determina a direção e a distância de cada passo."""
        from random import choice

        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance

        return step

    def fill_walk(self):
        """Calcula todos os pontos do passeio."""
        # Continua dando passos até que o passeio alcance o tamanho desejado.
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            # Rejeita movimentos que não vão a lugar nenhum.
            if x_step == 0 and y_step == 0:
                continue

            # Calcula os próximos valores de x e de y.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)
```

>- [_rw_visual.py_](https://github.com/willy-r/curso-intensivo-python/blob/master/capitulo_15/rw_visual.py)

```
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Continua criando novos passeios enquanto o programa estiver ativo.
while True:
    # Cria um passeio aleatório e plota os pontos.
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Define o tamanho da janela de plotagem.
    plt.figure(figsize=(16, 9), dpi=128)

    # Plota os pontos e mostra o gráfico.
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
                cmap=plt.cm.rainbow, edgecolors='none', s=3)

    # Enfatiza o primeiro e o último ponto.
    plt.scatter(0, 0, c='black', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1],
                c='blue', edgecolors='none', s=100)

    # Remove os eixos.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    # Define o nome do título.
    plt.title('Passeios Aleatórios', fontsize=24)

    plt.savefig('rw_visual.png', bbox_inches='tight')
    plt.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break
```

<img src='https://github.com/willy-r/curso-intensivo-python/blob/master/capitulo_15/imagens/rw_visual.png' heigth='830' width='700'>

> _Ponto preto é o início do passeio. | Ponto azul é o final do passeio._

---

- ### Utilização do [_Pygal_](pygal.org)
Exemplo de visualização com o [pygal.Bar](http://pygal.org/en/stable/documentation/types/bar.html) com uma classe que representa um Dado.
>- [_die.py_](https://github.com/willy-r/curso-intensivo-python/blob/master/capitulo_15/mpl_squares.py)

```
class Die:
    """Uma classe que representa um único dado."""

    def __init__(self, num_sides=6):
        """Supõe que seja um dado de seis lados."""
        self.num_sides = num_sides

    def roll(self):
        """Devolve um valor aleatório entre 1 e o número e lados."""
        from random import randint

        return randint(1, self.num_sides)
```

>- [_die_visual.py_](https://github.com/willy-r/curso-intensivo-python/blob/master/capitulo_15/die_visual.py)

```
import pygal
from pygal.style import NeonStyle

from die import Die

# Cria um D6.
die = Die()

# Faz alguns lançamentos e armazena os resultado em uma lista.
results = [die.roll() for roll_num in range(1000)]

# Analisa os resultados.
frequencies = [results.count(value) for value in range(1, die.num_sides + 1)]

# Visualiza os resultados.
hist = pygal.Bar(style=NeonStyle)
hist.title = 'Results of rolling one D6 1000 times.'
hist.x_labels = [x for x in range(1, die.num_sides + 1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'
hist.add('D6', frequencies)

hist.render_to_file('die_visual.svg')
```

<img src='https://user-images.githubusercontent.com/47596121/65642796-77ec3c00-dfc6-11e9-9f81-ed24ab817fd3.png' heigth='830' width='700'>

> [_NeonStyle_](http://pygal.org/en/stable/documentation/builtin_styles.html#neon) do Pygal.

---
