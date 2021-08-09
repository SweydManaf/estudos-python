def describe_pet(pet_name, animal_type='dog'):
    """Exibe informações sobre um animal de estimação."""
    print(f'\nI have a {animal_type}.'
          f"\nMy {animal_type}'s name is {pet_name.title()}.")


# Um cachorro chamado Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# Um hamster chamado Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
