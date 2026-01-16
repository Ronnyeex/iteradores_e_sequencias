text = 'Ronnye'

interador = iter(text)

while True:
    try:
        letras = next(interador)
        print(letras)
    except StopIteration:
        break
        