from admin import Admin

admin = Admin(
    'william', 'rodrigues', 'Admin',
    'will@example.com', 'ceará', 19, 'M'
    )
admin.descrever_usuario()
admin.saudar_usuario()
admin.privilegios.mostrar_privilegios()
