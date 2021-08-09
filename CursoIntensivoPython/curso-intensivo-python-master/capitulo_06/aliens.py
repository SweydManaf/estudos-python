# Cria uma lista vazia para armazenar alienígenas.
aliens = list()

# Cria 30 alienígenas verdes.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Modifica os 3 primeiros alienígenas.
# O alienígena vai ter a cor amarela, a velocidade média e vai valer 10 pts.
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    # Se a cor for amarela, muda a cor do alienígena para vermelho,
    # velocidade para rápido e vai valer 15 pontos.
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Mostra os 5 primeiros alienígenas.
for alien in aliens[:5]:
    print(alien)
print('...')

# Mostra quantos alienígenas foram criados.
print(f'Total number of aliens: {len(aliens)}')
