mensaje = input("Ingresa el mensaje: ")
veces = int(input("Cuántas veces quieres mover la letra: "))

mensajeCifrado = ""

for i in range(0, len(mensaje), 1):
    letra = mensaje[i]
    minuscula = (letra >= 'a' and letra <= 'z')
    mayuscula = (letra >= 'A' and letra <= 'Z')
    if not(minuscula or mayuscula):
        mensajeCifrado += letra
    else:
        ascii = ord(letra)
        baseAscii = ord('a')
        if mayuscula:
            baseAscii = ord('A')
        nuevoAscii = (ascii - baseAscii - veces) % 26 + baseAscii #Se cambio el signo + a - para que en lugar de sumar las veces se resten para volver al codigo original#
        nuevaLetra = chr(nuevoAscii)
        mensajeCifrado += nuevaLetra

print(mensajeCifrado)