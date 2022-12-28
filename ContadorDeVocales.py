frase = input("Ingrese una frase: ")

contadorA = 0
contadorE = 0
contadorI = 0
contadorO = 0
contadorU = 0


for i in frase:
    if i == "a":
        contadorA += 1
    elif i == "e":
        contadorE += 1
    elif i == "i":
        contadorI += 1
    elif i == "o":
        contadorO += 1
    elif i == "u":
        contadorU += 1

print("La vocal A se encuentra ",contadorA," veces en la frase: ", frase,)
print("La vocal E se encuentra ",contadorE," veces en la frase: ", frase,)
print("La vocal I se encuentra ",contadorI," veces en la frase: ", frase,)
print("La vocal O se encuentra ",contadorO," veces en la frase: ", frase,)
print("La vocal U se encuentra ",contadorU," veces en la frase: ", frase,)

