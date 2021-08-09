my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')

print(f'As minhas comidas favoritas são:')
for food in my_foods:
    print(f'\t{food.title()}')

print(f'\nAs comidas favoritas de meu amigo são:')
for food in friend_foods:
    print(f'\t{food.title()}')
