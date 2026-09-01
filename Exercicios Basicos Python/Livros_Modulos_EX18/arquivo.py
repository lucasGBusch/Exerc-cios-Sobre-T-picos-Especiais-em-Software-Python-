from cadastro import livros

# from cadastro import livros -> importa a MESMA lista (não uma cópia), por isso .clear()/.append() aqui afetam o cadastro.py também.

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
