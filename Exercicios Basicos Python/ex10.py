"""

Exercício 10 – Sistema de Cadastro de Eventos
Desenvolva um programa que permita cadastrar diversos participantes.

Para cada participante solicitar:

Nome
Idade
Cidade
Categoria
Categorias válidas:

ESTUDANTE
PROFISSIONAL
PALESTRANTE
O sistema deverá:

aceitar letras maiúsculas e minúsculas;
validar se a categoria é válida;
permitir novos cadastros até que o usuário informe "N";
contar quantos participantes existem em cada categoria;
informar:
total de participantes;
média das idades;
participante mais velho;
participante mais novo.

"""

profissional = 0
palestrante = 0
estudante = 0
soma_idade = 0
escolha = "S"
media = 0
velho = 0
novo = 0
total_participantes = 0

while True:
    print("=" * 30 + "\n")
    print("       >>>>>> MENU <<<<<")

    nome = input("\nNome: ").strip()
    idade = int(input("\nIdade: "))
    cidade = input("\nCidade: ").strip()
    categoria = input("\nCategoria validas(Estudante / Profissional / Palestrante): ").strip().upper()

    if categoria not in ["ESTUDANTE", "PROFISSIONAL", "PALESTRANTE"]:
        print("\nDiga uma categoria valida.")
        continue

    total_participantes += 1
    soma_idade += idade

    if categoria == "ESTUDANTE":
        estudante += 1
    elif categoria == "PROFISSIONAL":
        profissional += 1
    elif categoria == "PALESTRANTE":
        palestrante += 1
    
    if total_participantes == 1:
        mais_velho_nome = nome
        mais_velho_idade = idade
        mais_novo_nome = nome
        mais_novo_idade = idade
    else:
        if idade > mais_velho_idade:
            mais_velho_idade = idade
            mais_velho_nome = nome
            
        if idade < mais_novo_idade:
            mais_novo_idade = idade
            mais_novo_nome = nome

    print("\nCadastrado com sucesso!")
        
    escolha = input("\nQuer continuar o cadastro(S/N): ").strip().upper()
    if escolha == "N":
        break
        
    print("\n" + "=" * 30)


print("\n" + "=" * 35)
print("       RESUMO DO EVENTO")
print("=" * 35)

if total_participantes > 0:
    media = soma_idade / total_participantes
    print(f"Total de participantes : {total_participantes}")
    print(f"Estudantes           : {estudante}")
    print(f"Profissionais        : {profissional}")
    print(f"Palestrantes         : {palestrante}")
    print(f"\nMédia das idades       : {media:.1f} anos")
    print(f"Participante mais velho: {mais_velho_nome} ({mais_velho_idade} anos)")
    print(f"Participante mais novo : {mais_novo_nome} ({mais_novo_idade} anos)")
else:
    print("Nenhum participante foi cadastrado.")

print("=" * 35)
