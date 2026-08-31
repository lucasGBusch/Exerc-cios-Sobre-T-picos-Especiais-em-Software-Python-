"""
Mesclagem do ex13 (uso de Arquivos) com o ex14 (uso de Funções).

"""

livros = []
choice = -1
encontrado = False

# a(append) garante a existencia do arquivo
with open("Historico_livros.txt", "a") as arquivo:
    pass

# r(read) le os arquivos salvos usando o separador ","
with open("Historico_livros.txt", "r") as arquivo:
    for linha in arquivo:
        dados = linha.strip().split(",")
        if len(dados) == 4:
            livro = {
                "titulo": dados[0],
                "autor": dados[1],
                "ano": int(dados[2]),
                "editora": dados[3]
            }
            livros.append(livro)


def menu():
    print("=" * 20)
    print("MENU")
    print("=" * 20)

    print("\n1 - Cadastrar Livro")
    print("2 - Listar Livros")
    print("3 - Pesquisar Livro")
    print("4 - Excluir")
    print("5 - Quantidade")
    print("0 - Sair")
    print("=" * 20)


def cadastrar():
    novo_livro = {

        "titulo":input("Titulo: "),

        "autor":input("Autor: "),

        "ano":int(input("Ano: ")),
        
        "editora":input("Editora: ")

    }

    livros.append(novo_livro)

    # a(append) adiciona o cadastro
    with open("Historico_livros.txt", "a") as arquivo:
        arquivo.write(f"{novo_livro['titulo']},{novo_livro['autor']},{novo_livro['ano']},{novo_livro['editora']}\n")

    print("Livro cadastrado com sucesso!")


def listar():
    if not livros:
        print("Lista de livros vazia.")
    else:
        print("\n" + "=" * 30)
        print("LISTA LIVROS")
        print("\n" + "=" * 30)
            
        for livro in livros:
            print("-" * 30)
            for key, value in livro.items():
                print(f"{key.title():<10}: {value}")
                        
        print("-" * 30)


def pesquisar():
    busca = input("Qual o Titulo do livro que você está procurando: ")
    encontrado = False
            
    for livro in livros:
        if busca.lower() == livro["titulo"].lower():
            print("\nLivro encontrado...")
            print("\n" + "=" * 30)
                    
            for key, value in livro.items():
                print(f"{key.title():<10}: {value}")

            encontrado = True
            break
            
    if not encontrado:
        print("\nLivro não encontrado...")


def excluir():
    excluir_titulo = input("Qual livro voce deseja alterar (Digite o titulo): ")
    excluido = False
            
    for livro in livros:
        if excluir_titulo.lower() == livro["titulo"].lower():
            livros.remove(livro)
            excluido = True

            # w(write) reescreve a lista
            with open("Historico_livros.txt", "w") as arquivo:
                for livro in livros:
                    arquivo.write(f"{livro['titulo']},{livro['autor']},{livro['ano']},{livro['editora']}\n")

            print("\nLivro excluido com sucesso!")
            break

    if not excluido:
        print("\nLivro não encontrado...")


def quantidade():
    print(f"\nQuantidade de livros: {len(livros):<10}")


while choice != 0:
    menu()

    choice = int(input("\nFaça a sua escolha (0 para sair): "))

    match choice:
        case 1:
            cadastrar()
        case 2:
            listar()
        case 3:
            pesquisar()
        case 4:
            excluir()
        case 5:
            quantidade()
        case 0:
            print("\nSaindo do programa...")
        case _:
            print("\nOpção invalida")