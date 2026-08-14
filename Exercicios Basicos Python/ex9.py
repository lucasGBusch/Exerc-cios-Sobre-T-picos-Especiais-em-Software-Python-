"""

Exercício 9 – Sistema de Bolsas

Solicite:

Nome
Média
Frequência
Informe o resultado.

Utilize operadores lógicos.

"""

print(">>>>> CADASTRO DE BOLSAS <<<<<")
nome = input("\nDigite o nome: ")
media = float(input("Digite a média: "))
frequencia = float(input("Digite a frequencia: "))

if media >= 9 and frequencia >= 90:
    print(f"\nO aluno {nome} tem direito a uma bolsa integral!")
elif media >= 7 and frequencia >= 75:
    print(f"\nO aluno {nome} tem direito a uma bolsa parcial!")
else:
    print("\nSem bolsa...")


