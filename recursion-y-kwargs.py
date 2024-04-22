def escribir_el_nombre(*args,**kwargs):
    print("      Inicio")
    print(kwargs)
    for arg in args:
        print(arg)
    for keys,values in kwargs.items():
        print("key",keys,'value',values)


escribir_el_nombre(
    primer_nombre='Alma',
    segundo_nombre='Estefania',
    primer_apellido='Quinteros',
    segundo_apellido='Quiroga'
)

escribir_el_nombre(
    primer_nombre='Santiago',
    primer_apellido='Escudero',
    segundo_apellido='Bernal'
)

escribir_el_nombre(
    primer_nombre='Maria',
    segundo_nombre='Victoria',
    primer_apellido='Torres Burgos'
)