"""

Sistema de Cadastro de Participantes com match

"""

choice = -1
cadastrado = 0

while choice != 4:
    print("=" * 30 + "\n")
    print(">>>>> MENU <<<<<")
    
    print("\n1- Nova inscrição")
    print("2- Consultar inscrição")
    print("3- Alterar nome")
    print("4- Sair")

    choice = int(input("\nEscolha: "))

    match choice:
        case 1:
            print("=" * 30 + "\n")
            nome = input("Nome: ").strip().title()
            cidade = input("Cidade: ").strip().title()
            idade = int(input("Idade: "))

            if idade < 16:
                print("Inscrição negada...")
            elif idade == 16 or idade == 17:
                print("Requer autorização...")
            else:
                print("\nCadastrado com sucesso!")
                print("\n" + "=" * 30)
                cadastrado += 1
        case 2:
            if cadastrado == 0:
                print("\nLista vazia...\n")
            else:
                print("=" * 30 + "\n")
                print(">>>>> INSCRITOS <<<<<")
                print(f"Nome: {nome}")
                print(f"Cidade: {cidade}")
                print(f"Idade: {idade}")
                print("\n" + "=" * 30)
        case 3:
            nome = input("Qual o novo nome: ").strip().title()

            print("Novo nome alterado com sucesso!")
        case 4:
            print("Saindo do programa...")
            break
        case _:
            print("Erro...")





