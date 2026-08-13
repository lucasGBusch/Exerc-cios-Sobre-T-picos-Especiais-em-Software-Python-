"""

Exercício 6 – Login do Sistema

Crie um sistema simples de autenticação.

Usuário:
ADMIN
Senha:
1234
O usuário possui apenas 3 tentativas.

Caso acerte:
Bem-vindo ao sistema.

Caso erre três vezes:
Usuário bloqueado.

Utilize:
while
break

"""

user = ""
password = 0
tentativas = 0

while user != "ADMIN" and password != 1234:
    print("\n>>>> MENU LOGIN <<<<")
    user = input("\nUser name: ")
    password = int(input("\nPassword: "))
    
    if user != "ADMIN" and password != 1234:
        print("\nSenha errada ou Usuario errado...")
        tentativas += 1
        if tentativas == 3:
            print("\nUsuario Bloqueado.")
            break
    else:
        print("=" * 30)
        print("\nBem-vindo ao sistema.")
        print("\n" + "=" * 30)
