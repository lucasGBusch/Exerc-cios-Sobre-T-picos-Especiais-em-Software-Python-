"""

Exercício 4 – Estatísticas do Evento
Amplie o exercício anterior.

Além do cadastro, informe ao final:

quantidade total de participantes;
quantidade de maiores de idade;
quantidade de menores de idade;
média das idades.

"""

total = 0
value = "S"
maior = 0
menor = 0
soma_idades = 0

while value != "N":
    nome = input("\nQual o seu nome: ")
    idade = int(input("Qual a sua idade: "))
    cidade = input("Qual é a sua cidade: ")
    
    total += 1
    soma_idades += idade
    
    if idade >= 18:
        maior += 1
    else:
        menor +=1
    
    value = input("\nDeseja cadastrar outro participante? (S/N): ").upper()
    
if idade > 0:
    media = soma_idades / total
else:
    media = 0

print("=" * 30 + "\n")    
print(f"O total de participantes é: {total} ")
print(f"O total de maiores de idade é: {maior}")
print(f"O total de menores de idade é: {menor}")
print(f"A media das idade é : {media:.1f}")
print("\n" + "=" * 30)    








    
    


