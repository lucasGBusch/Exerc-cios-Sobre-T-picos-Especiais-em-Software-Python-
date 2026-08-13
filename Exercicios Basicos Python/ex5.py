"""
Exercício 5 – Pesquisa de Satisfação
Uma empresa realizou uma pesquisa.

Cadastrar exatamente 10 clientes.

Para cada cliente informar:

Nome
Nota de satisfação (0 a 10)
Ao final informar:

maior nota;
menor nota;
média das notas;
quantidade de clientes com nota maior ou igual a 8.
Utilize for.

"""

maior = 0
menor = 0
soma_nota = 0
oito = 0

for i in range (1, 11):
    print("=" * 40 + "\n")
    print(f">>>> Cadastro de cliente numero {i} <<<<")
    nome = input("\nQual o seu nome: ")
    nota = int(input("Qual a sua nota de satisfação de 0 a 10: "))
    
   
    soma_nota += nota
    
    if nota >= 8:
        oito += 1
        
    
    if i == 1:
        maior = nota
        menor = nota
    else:
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota
        
media = soma_nota / 10

print("=" * 30 + "\n")    
print(f"A maior nota é: {maior}")
print(f"Menor nota é: {menor}")
print(f"A media das nota é : {media:.1f}")
print(f"A quantidade de clientes com nota maior ou igual a 8 foi: {oito}")
print("\n" + "=" * 30)