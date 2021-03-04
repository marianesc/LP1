def forca(palavra, existe):
    maiuscula = str.upper(palavra)
    minuscula = str.lower(palavra)
    forca = ''
    
    for e in existe:
        if str.isupper(e):
            for i in range(len(maiuscula)):
                if maiuscula[i] == e:
                    forca += palavra[i]
                else: 
                    forca += '_'

    
        if str.islower(e):
            for i in range(len(minuscula)):
                if minuscula[i] == e:
                    forca += palavra[i]
                else:
                    forca += '_'

    if existe == []:
        forca = '_' * len(palavra)

    return forca

assert forca('casa', ['a']) == '_a_a'
assert forca('casa', []) == '____'
assert forca('casa', ['A']) == '_a_a'
assert forca('CASA', ['a']) == '_A_A'
