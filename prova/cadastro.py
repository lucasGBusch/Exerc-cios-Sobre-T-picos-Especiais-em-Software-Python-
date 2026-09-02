'''
1 - Cadastrar participante 
2 - Listar participantes 
3 - Pesquisar participante 
4 - Alterar participante 
5 - Excluir participante 
6 - Exibir estatísticas 
7 - Salvar arquivo 
8 - Carregar arquivo 
0 - Sair

def __init__(self, nome, idade, email, categoria, valor_pago):
    self.nome = nome
    self.idade = idade
    self.email = email
    self.categoria = categoria
    self.valor_pago = valor_pago
'''

from participante import Participante
from dados import participantes

def cadastrar():
    nome = input("Nome: ").strip().title()
    email = input("Email: ").strip().title()
    categoria = input("Categoria(ESTUDANTE/PROFISSIONAL/PALESTRANTE): ").upper()

    try:
        idade = int(input("Idade: ").strip())
        valor_pago = float(input("Valor pago: ").strip())
    except ValueError:
        print("\nIdade ou valor pago inválido.")
        input("Precione ENTER para continuar...")
        return
    
    if idade < 0:
        print("\nIdade inválido.")
        input("Precione ENTER para continuar...")
        return
    
    if valor_pago < 0:
        print("\nValor pago inválido.")
        input("Precione ENTER para continuar...")
        return
    
    if categoria not in ["ESTUDANTE", "PROFISSIONAL", "PALESTRANTE"]:
        print("\nCategoria invalida.")
        input("Precione ENTER para continuar...")
        return
    
    participante = Participante(
        nome,
        idade,
        email,
        categoria,
        valor_pago
    )

    participantes.append(participante)
    print("Cadastro foi um sucesso!")
    input("Precione ENTER para continuar...")



def listar():
    if len(participantes) == 0:
        print("\nNenhum participante cadastrado.")
        return

    print("\n========== PARTICIPANTES ==========")

    for participante in participantes:
        participante.mostrar_dados()
    input("Precione ENTER para continuar...")



def pesquisar():
    if len(participantes) == 0:
        print("\nNenhum participante cadastrado.")
        return
    
    search = input("Qual participante deseja procurar: ").strip().title()
    status = False

    for participante in participantes:
        if participante.nome == search:
            print("\n----- Pessoa encontrada -----\n")
            participante.mostrar_dados()
            status = True
            input("Precione ENTER para continuar...")
            break
        
    if not status:
        print("Pessoa não encontrada.")
        input("Precione ENTER para continuar...")



def alterar():
    if len(participantes) == 0:
        print("\nNenhum participante cadastrado.")
        return
    
    search = input("Qual participante deseja alterar: ").strip().title()
    status = False

    for participante in participantes:
        if participante.nome == search:
            status = True
            print("\n----- Pessoa encontrada -----\n")
            participante.mostrar_dados()

            nova_categoria = input("Categoria(ESTUDANTE/PROFISSIONAL/PALESTRANTE): ").upper()
            try:
                nova_idade = int(input("Idade: ").strip())
                novo_valor_pago = float(input("Valor pago: ").strip())
            except ValueError:
                print("\nIdade ou valor pago inválido.")
                input("Precione ENTER para continuar...")
                return
            
            if nova_idade < 0:
                print("\nIdade inválido.")
                input("Precione ENTER para continuar...")
                return
            
            if novo_valor_pago < 0:
                print("\nValor pago inválido.")
                input("Precione ENTER para continuar...")
                return
            
            if nova_categoria not in ["ESTUDANTE", "PROFISSIONAL", "PALESTRANTE"]:
                print("\nDiga uma categoria valida.")
                return
            
            participante.categoria = nova_categoria
            participante.idade = nova_idade
            participante.valor_pago = novo_valor_pago

            print("Participante alterado com sucesso!")
            input("Precione ENTER para continuar...")


def excluir():
    if len(participantes) == 0:
        print("\nNenhum participante cadastrado.")
        return
    
    search = input("Qual participante deseja excluir(nome): ").strip().title()
    status = False

    for participante in participantes:
        if participante.nome == search:
            participantes.remove(participante)
            status = True
            print("\n----- Pessoa removida -----\n")
            input("Precione ENTER para continuar...")
            break
        
    if not status:
        print("Pessoa não encontrada.")
        input("Precione ENTER para continuar...")

def exibir():
    print("--- ESTATISTICAS ---")
    quantidade_estudantes = 0
    quantidade_profissional = 0
    quantidade_palestrante = 0
    maior_idade = 0
    nome_maior = ""
    menor_idade = -1
    nome_menor = ""
    total_idade = 0
    total_arrecadado = 0.0

    '''
    O sistema deverá calcular e apresentar: 
    Total de participantes: 
    Quantidade de estudantes: 
    Quantidade de profissionais: 
    Quantidade de palestrantes: 
    Média de idade dos participantes: 
    Participante mais velho: 
    Participante mais novo: 
    Total arrecadado: 


    '''

    
    for participante in participantes:
        total_idade += participante.idade
        total_arrecadado += participante.valor_pago
        if menor_idade > participante.idade or menor_idade == -1:
            menor_idade = participante.idade
            nome_menor = participante.nome
        if maior_idade < participante.idade:
            maior_idade = participante.idade
            nome_maior = participante.nome
        if participante.categoria == "ESTUDANTE":
            quantidade_estudantes += 1
        if participante.categoria == "PROFISSIONAL":
            quantidade_profissional += 1
        if participante.categoria == "PALESTRANTE":
            quantidade_palestrante += 1

    print(f"Total de participantes: {len(participantes)}")
    print(f"Quantidade de estudantes: {quantidade_estudantes}")
    print(f"Quantidade de profissionais: {quantidade_profissional}")
    print(f"Quantidade de palestrantes: {quantidade_palestrante}")
    print(f"Média de idade dos participantes: {round(total_idade/len(participantes), 2)}")
    print(f"Participante mais velho: {nome_maior} - {maior_idade} ano{"s" if menor_idade>1 else ""}")
    print(f"Participante mais novo: {nome_menor} - {menor_idade} ano{"s" if menor_idade>1 else ""}")
    print(f"Total arrecadado: R${total_arrecadado}")
    input("Precione ENTER para continuar...")


