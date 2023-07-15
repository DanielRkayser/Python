import os
import random
nome = random.randint(-195, 890)
senha = random.randint(-195, 890)
cosenha = random.randint(-195, 890)
log = 0
while True:
    os.system('pause')
    os.system('cls')
    menu = int(input('''
----- MENU -----
 |1| CADASTRAR
 |2| LOGAR
 |3| SAIR
'''))
    if menu == 1:
        nome = input("Insira o nome de usuário:   ")
        senha = input("Insira a senha:   ")
        cosenha = input("Confirme a senha:   ")
        while senha != cosenha:
            senha = input("Insira a senha:   ")
            cosenha = input("Confirme a senha:   ")
        else:
            print("Bem-vindo,",nome)
    elif menu == 2:
        while log == 0:
            tnome = input("Informe o nome de usuário:   ")
            tsenha = input("Informe a senha:   ")
            if tnome == nome and tsenha == senha:
                print("Bem vindo,",nome,)
                log == 1
        while log == 1:
            opc = int(input('''
|1| CONTINUAR LOGADO
|2| DADO
|3| SAIR
'''))
            if opc == 1:
                print("continuou")
            elif opc == 2:
                random.randint(1, 6)
                print(dado)
