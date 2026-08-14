"""
Criar um sistema de cadastro de
livros.
 Cada livro possui:
 título
 autor
 ano
 editora
 Menu:

"""

livros = []
choice = -1

while choice != 0:
    print("=" * 20)
    print("    MENU")
    print("=" * 20)

    print("\n1 - Cadastrar Livro")
    print("2 - Listar Livros")
    print("3 - Pesquisar Livro")
    print("4 - Excluir")
    print("5 - Quantidade")
    print("0 - Sair")

    choice = int(input("\nFaça a sua escolha (0 para sair): "))

    match choice:
        case 1:
            novo_livro = {

                "titulo":input("Titulo: "),

                "autor":input("Autor: "),

                "ano":int(input("Ano: ")),
                
                "editora":input("Editora: ")

            }
            
            livros.append(novo_livro)
            
            print("Livro Cadastrado com sucesso!")
            
        case 2:
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
        case 3:
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
                print("Livro não encontrado...")
        case 4:
            excluir = input("Qual livro voce deseja alterar (Digite o titulo): ")
            excluido = False
            
            for livro in livros:
                if alterar.lower() == livro["titulo"].lower():
                    livros.remove(livro)
                    excluido = True
                    print("\nLivro excluido com sucesso!")
                    break
                
            if not excluido:
                print("Livro não encontrado...")
                
        case 5:
            print(f"\nQuantidade de livros: {len(livros):<10}")
        
        case 0:
            print("\nSaindo do programa...")
            
        case _:
            print("\nOpção invalida")
                    