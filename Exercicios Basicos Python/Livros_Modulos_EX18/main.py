# ordem de import importa: menu -> cadastro -> arquivo, porque arquivo.py depende de livros existir em cadastro.py primeiro.

from menu import menu
from cadastro import cadastrar, listar, pesquisar, excluir, quantidade
from arquivo import carregar, salvar

carregar()

choice = -1

while choice != 0:
    choice = menu()

    match choice:
        case 1:
            cadastrar()
            salvar()
        case 2:
            listar()
        case 3:
            pesquisar()
        case 4:
            excluir()
            salvar()
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