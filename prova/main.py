import menu
import cadastro
import arquivo

while True:
    choice = menu.menu()

    match choice:
        case 1:
            cadastro.cadastrar()
            arquivo.salvar()
        case 2:
            cadastro.listar()
        case 3:
            cadastro.pesquisar()
        case 4:
            cadastro.alterar()
        case 5:
            cadastro.excluir()
            arquivo.salvar()
        case 6:
            cadastro.exibir()
        case 7:
            arquivo.salvar()
        case 8:
            arquivo.carregar()
        case 0:
            print("\nSaindo do programa...")
        case _:
            print("\nOpção invalida")