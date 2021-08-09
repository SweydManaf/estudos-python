import name_function as nf

print("Enter 'q' at any time to quit.")

while True:
    first = input('\nPlease give me a first name: ')
    if first == 'q':
        break

    last = input('Please give me a last name: ')
    if last == 'q':
        break

    formatted_name = nf.get_formatted_name(first, last)
    print(f'\tNeatly formatted name: {formatted_name}')
