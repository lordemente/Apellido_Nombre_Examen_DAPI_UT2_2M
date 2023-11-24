def enanosverdes(cancion):
    cancion = 'Tengo un cohete en el pantalon\n'
    'y voz estás tan fria\n'
    
    lineas = cancion.split("\n")
    num_lineas = len(lineas)
    palabras = []
    for linea in lineas:
        palabras.append(len(lineas[linea].split()))
        
        
    for i in range(len(palabras)):
        texto= texto + "En la linea" + i+1 + "tiene" + palabras[i] + "palabras\n"
        return texto
    
    print(enanosverdes("asdwadasd\nasdwadwad"))