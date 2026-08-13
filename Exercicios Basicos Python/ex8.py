"""
Exercício 8 – Simulador de Caixa
Solicite ao operador que informe o valor das compras.

Quando ele informar 0, significa fechamento do caixa.

Ao final informar:

quantidade de vendas;
valor total vendido;
maior venda;
menor venda;
valor médio das vendas.
Utilize while.

"""
media_venda = 0
menor_venda = 0
maior_venda = 0
quantidade = 0
total_vendido = 0.0


print(">>>>> SIMULADOR DE CAIXA <<<<<")
print("\n>>>>> Digite 0 no valor para sair <<<<<")

while True:
    nome = input("\nQual o nome do produto: ")
    valor = float(input("\nQual o valor do produto: "))
    
    if valor == 0:
        print("Saindo do programa...")
        break

    if valor < 0:
        print("Erro o valor não pode ser negativo")
        continue

    quantidade += 1
    total_vendido += valor

    if quantidade == 1:
        maior_venda = valor
        menor_venda = valor
    else:
        if valor > maior_venda:
            maior_venda = valor
        if valor < menor_venda:
            menor_venda = valor

    print("\nProduto/Venda registrado com sucesso!")

    
print(">>>>> RESULTADOS <<<<<")

media_venda = total_vendido / quantidade
    
print(f"Quantidade de vendas : {quantidade}")
print(f"Valor total vendido  : R$ {total_vendido:.2f}")
print(f"Maior venda          : R$ {maior_venda:.2f}")
print(f"Menor venda          : R$ {menor_venda:.2f}")
print(f"Valor médio por venda: R$ {media_venda:.2f}")