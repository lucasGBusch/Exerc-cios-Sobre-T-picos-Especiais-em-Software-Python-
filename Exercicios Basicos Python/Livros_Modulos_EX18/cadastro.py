# salvar() NÃO é chamado aqui dentro (evita import circular com arquivo.py) -> quem chama salvar() é o main.py, de fora. 

livros = []
encontrado = False

def cadastrar():
    titulo = input("Titulo: ")
    autor = input("Autor: ")

    while True:
        try:
            ano = int(input("Ano: "))
            break  # só sai do loop se o int() não der erro
        except ValueError:
            print("\nDigite apenas numeros...")
    
    editora = input("Editora: ")

    novo_livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "editora": editora
    }

    livros.append(novo_livro)
    

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
    excluir_titulo = input("Qual livro voce deseja excluir (Digite o titulo): ")
    excluido = False
            
    for livro in livros:
        if excluir_titulo.lower() == livro["titulo"].lower():
            livros.remove(livro)
            excluido = True
            

            print("\nLivro excluido com sucesso!")
            break

    if not excluido:
        print("\nLivro não encontrado...")


def quantidade():
    print(f"\nQuantidade de livros: {len(livros):<10}")