def greet_users(names):
    """Exibe uma saudação simples a cada usuário da lista."""
    for name in names:
        msg = f'Hello, {name.title()}!'
        print(msg)


usernames = ['hannah', 'try', 'margot']
greet_users(usernames)
