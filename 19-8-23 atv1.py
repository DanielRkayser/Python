import random
import os
import sys
log = False
while log == False:
    tent = 3
    tl = int(input('''
====================================|LOGIN|===================================

                |1| CRIAR CONTA
                |2| ENTRAR NA CONTA
                |3| SAIR DO PROGRAMA

==============================================================================
'''))
    if tl == 1:
            nc = input('Insira nome de usuário:   ')
            sc = input('Insira senha:   ')
            while sc == nc:
                print('A senha não pode ser o nome de usuário!')
                sc = input('Insira senha:   ')
            os.system('cls')
    elif tl == 2:
            nl = input('Informe o nome de usuário:   ')
            sl = input('Informe a senha:   ')
            while sl != sc or nl != nc: 
                tent -= 1
                print('Nome de usuário ou senha está incorreto!')
                print(f'{tent} tentativa(s) restantes(s)')
                nl = input('Informe o nome de usuário:   ')
                sl = input('Informe a senha:   ')
                if tent <= 0:
                    os.system('cls')
                    break
            else:
                print(f'Olá {nc}')
                log = True
    elif tl == 3:
        sys.exit()
    else:
        print('Não é uma opção!')
        os.system('pause')
        os.system('cls')
    
while log == True:
    to = int(input('''
===================================|OPÇÕES|===================================

                |1| JOGAR DADOS
                |2| CALCULADORA
                |3| NÚMEROS PRIMOS
                |4| SAIR DA CONTA

==============================================================================
'''))
    if to == 1:
        ndado = int(input('Quantos lados tem o dado?'))
        dado = random.randint('1, ndado')
        print(dado)
