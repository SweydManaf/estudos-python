def tag_html(func):
    def interna(*args, **kwargs):
        return '<html>' + func(*args, **kwargs) + '</html>'
    return interna

@tag_html
def ola_bb():
    return 'Olá BB'

@tag_html
def live():
    return 'Live de Python'

print(ola_bb())
print(live())