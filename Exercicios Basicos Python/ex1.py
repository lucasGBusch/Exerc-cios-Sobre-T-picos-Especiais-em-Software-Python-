""" 
Exercício 1 – Sistema de Controle de Acesso
Desenvolva um programa que solicite:

Nome do participante
Idade
Tipo de ingresso (VIP ou COMUM)
O sistema deverá:

aceitar "vip", "Vip", "VIP" etc.;
permitir entrada apenas para maiores de 16 anos;
informar se o participante terá acesso à área VIP ou à área comum.
Caso seja menor de 16 anos, informar que a entrada foi negada. 

"""
print("-" * 30)
nome = input("\nQual é o seu nome: ")
idade = int(input("Qual é a sua idade: "))
ingresso = input("Qual o tipo de ingresso (VIP ou COMUM): ")

if idade > 16:
    print(f"\nBem vindo {nome}, pode entrar na area {ingresso.upper()}.")
else:
    print("Acesso negado...")
