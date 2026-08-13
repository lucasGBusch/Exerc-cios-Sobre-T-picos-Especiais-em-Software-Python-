"""
Exercício 2 – Calculadora de Mensalidade
Uma academia cobra mensalidades conforme a idade do aluno.

Solicite:

nome
idade
Apresente uma ficha contendo:

Nome
Idade
Valor da mensalidade

"""


nome = input("Qual é o seu nome: ")
idade = int (input("Qual é a sua idade: "))

if idade <= 17:
    print(" = " * 10)
    print("Ficha gerada com sucesso!")
    print("\n" + nome.capitalize())
    print(idade)
    print("Valor da mensalidade é R$70,00")
    print(" = " * 10)
elif idade >= 18 and idade <= 39:
        print(" = " * 10)
        print("Ficha gerada com sucesso!")
        print("\n" + nome.capitalize())
        print(idade)
        print("Valor da mensalidade é R$120,00")
        print(" = " * 10)
elif idade >= 40 and idade <= 59:
        print(" = " * 10)
        print("Ficha gerada com sucesso!")
        print("\n" + nome.capitalize())
        print(idade)
        print("Valor da mensalidade é R$90,00")
        print(" = " * 10)
else:
        print(" = " * 10)
        print("Ficha gerada com sucesso!")
        print("\n" + nome.capitalize())
        print(idade)
        print("Valor da mensalidade é R$60,00")
        print(" = " * 10)
        