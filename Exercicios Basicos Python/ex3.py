"""

Exercício 3 – Cadastro de Participantes
Desenvolva um programa que permita cadastrar participantes até que o usuário informe "N".

Para cada participante solicitar:

Nome
Idade
Cidade
Ao final informar:

Quantidade de participantes cadastrados.
Utilize while.


"""

total = 0
value = "S"

while value != "N":
    nome = input("\nQual o seu nome: ")
    idade = int(input("Qual a sua idade: "))
    cidade = input("Qual é a sua cidade: ")
    
    total += 1
    
    value = input("\nDeseja cadastrar outro participante? (S/N): ").upper()
    
print("\n" + "=" * 30)    
print(f"\nO total de participantes é: {total} ")