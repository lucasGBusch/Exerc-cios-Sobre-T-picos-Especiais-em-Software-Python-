#menu() só pergunta e devolve a opção (return opcao) -> quem decide o que fazer é o main.py. 

def menu():
    print("=" * 20)
    print("MENU")
    print("=" * 20)
    print("\n1 - Cadastrar Livro")
    print("2 - Listar Livros")
    print("3 - Pesquisar Livro")
    print("4 - Excluir")
    print("5 - Quantidade")
    print("6 - Carregar")
    print("7 - Salvar")
    print("0 - Sair")
    print("=" * 20)

    while True:
        try:
            opcao = int(input("\nFaça a sua escolha (0 para sair): "))
            break
        except ValueError:
            print("\nDigite apenas numeros...")

    return opcao