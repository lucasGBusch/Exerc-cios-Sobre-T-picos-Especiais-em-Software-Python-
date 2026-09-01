"""

Exercicio 17 colocado o uso de try: e except


Alguns exemplos: 

try:
    idade = int(input("Idade: "))
    print(f"Idade: {idade}")
except:
    print("Valor inválido.")

/////////////////////////////////////////////////////////

Erro específico
python
try:
    idade = int(input("Idade: "))
except ValueError:
    print("Digite apenas números.")

else — roda somente quando NÃO ocorre erro
python
try:
    idade = int(input("Idade: "))
except ValueError:
    print("Valor inválido.")
else:
    print("Cadastro realizado.")

///////////////////////////////////////////////////////////////

finally — roda sempre, deu erro ou não
python
try:
    idade = int(input("Idade: "))
except ValueError:
    print("Valor inválido.")
finally:
    print("Fim do programa.")

/////////////////////////////////////////////////////

Múltiplos except (exemplo com divisão)
python
try:
    numero = int(input("Número: "))
    resultado = 100 / numero
    print(resultado)
except ZeroDivisionError:
    print("Não existe divisão por zero.")
except ValueError:
    print("Digite apenas números.")

//////////////////////////////////////////////

Exemplo com arquivos:

try:
    with open("alunos.txt", "r") as arquivo:
        print(arquivo.read())
except FileNotFoundError:
    print("Arquivo não encontrado.")
 
"""

livros = []
choice = -1
encontrado = False


def carregar():
    livros.clear()

    # a(append) garante a existencia do arquivo
    with open("Historico_livros.txt", "a") as arquivo:
        pass
    
    try:
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

        print("Arquivo carregado com sucesso!")
    
    except FileNotFoundError:
        print("\nErro no arquivo.")

def salvar():
    # w(write) reescreve o arquivo inteiro com a lista atual
    with open("Historico_livros.txt", "w") as arquivo:
        for livro in livros:
            arquivo.write(f"{livro['titulo']},{livro['autor']},{livro['ano']},{livro['editora']}\n")

    print("Arquivo salvo com sucesso!")


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
    salvar()

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
            salvar()

            print("\nLivro excluido com sucesso!")
            break

    if not excluido:
        print("\nLivro não encontrado...")


def quantidade():
    print(f"\nQuantidade de livros: {len(livros):<10}")


carregar()

while choice != 0:
    menu()
    while True:
        try:
            choice = int(input("\nFaça a sua escolha (0 para sair): "))
            break
        except ValueError:
            print("\nDigite apenas numeros...")
    
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
        case 6:
            carregar()
        case 7:
            salvar()
        case 0:
            print("\nSaindo do programa...")
        case _:
            print("\nOpção invalida")