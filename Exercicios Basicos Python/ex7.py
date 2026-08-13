"""

Exercício 7 – Controle de Inscrições
O sistema deverá cadastrar participantes.

Encerrar o cadastro quando o usuário informar idade igual a 0.

Caso a idade seja negativa:

exibir mensagem de erro;
solicitar novamente a idade (utilizando continue).
Ao final informar:

quantidade de participantes válidos.

"""

participantes_validos = 0

while True:
    idade = int(input("Digite sua idade (0 para finalizar): "))
    
    if idade < 0:
        print("\nA idade não pode ser negativa...")
        continue
    
    if idade == 0:
        print("\nFim do cadastro...")
        break
        
    participantes_validos += 1
    
print(f"\nParticipantes validos: {participantes_validos}")