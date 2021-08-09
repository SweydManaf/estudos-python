numeros = {
    'william': [16, 7],
    'igor': [9, 1, 5],
    'milly': [4, 8, 6],
    'iago': [10, 15, 18],
    'kelly': [25],
    }

for nome, nums in numeros.items():
    if len(nums) != 1:
        print(f'\nOs números favoritos de {nome.title()} são ', end='')
        for n in nums:
            print(f'{n}', end=', ' if n != nums[-1] else '.\n')
    else:
        print(f'\nO número favorito de {nome.title()} é {nums[0]}.')
