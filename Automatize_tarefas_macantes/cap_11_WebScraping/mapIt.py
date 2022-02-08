import webbrowser
import sys
import pyperclip as pc


if len(sys.argv) > 1:
    # Obtem o endereco da linha de comando
    address = "".join(sys.argv[1:])
else:
    # Obtem o endereco do clipboard
    address = pc.paste()
    print(address)

webbrowser.open(f"http://maps.google.com/maps/place/{address}")