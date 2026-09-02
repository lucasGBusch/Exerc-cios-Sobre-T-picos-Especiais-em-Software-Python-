def menu():
    print("=" * 34)
    print("  GERENCIAMENTO DE PARTICIPANTES  ")
    print("=" * 34)
    print("\n")
    print("1 - Cadastrar participante")
    print("2 - Listar participantes ")
    print("3 - Pesquisar participante ")
    print("4 - Alterar participante ")
    print("5 - Excluir participante ")
    print("6 - Exibir estatísticas ")
    print("7 - Salvar arquivo ")
    print("8 - Carregar arquivo ")
    print("0 - Sair")
    
    while True:
        try:
            opcao = int(input("\nFaça a sua escolha (0 para sair): "))
            break
        except ValueError:
            print("\nDigite apenas numeros...")

    return opcao
