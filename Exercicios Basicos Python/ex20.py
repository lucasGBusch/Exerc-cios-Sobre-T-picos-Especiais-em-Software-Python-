"""

3. Leia 10 números, armazene-os em uma lista e utilize um conjunto
para mostrar apenas os valores diferentes.

"""

rep = 0
numeros = []

while rep < 10:
    num = int(input("Digite o numero: "))
    numeros.append(num)
    rep = rep + 1

diferentes = set(numeros)

print("Valores diferentes:", diferentes)
    
