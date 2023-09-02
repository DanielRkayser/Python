import random
import os
import sys
import time
log = False
ln = ["DaniDev"]
ls = ["2808"]
while True:
    while log == False:
        tent = 3
        tmp = 30
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
                ln.append(nc)
                ls.append(sc)
                os.system('cls')
        elif tl == 2:
                nl = input('Informe o nome de usuário:   ')
                sl = input('Informe a senha:   ')
                while sl not in ls or nl not in ln or sl != ls[ln.index(nl)] : 
                    tent -= 1
                    print('Nome de usuário ou senha está incorreto!')
                    print(f'{tent} tentativa(s) restantes(s)')
                    nl = input('Informe o nome de usuário:   ')
                    sl = input('Informe a senha:   ')
                    if tent <= 0:
                        for i in range(tmp, 0, -1):
                            print(i)
                            time.sleep(1)
                            os.system('cls')
                        tmp += 30
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
        elif to == 2:
            op = int(input('''
            QUAL OPERAÇÃO SERÁ USADA?

        |1| ADIÇÃO
        |2| SUBTRAÇÃO
        |3| MULTIPLICAÇÃO
        |4| DIVISÃO
'''))
            if op == 1:
                n1 = int(input('Insira o primeiro número:   '))
                n2 = int(input('Insira o segundo número:    '))
                print(f'RESULTADO:   {n1 + n2}')
            elif op == 2:
                n1 = int(input('Insira o primeiro número:   '))
                n2 = int(input('Insira o segundo número:    '))
                print(f'RESULTADO:   {n1 - n2}')
            elif op == 3:
                n1 = int(input('Insira o primeiro número:   '))
                n2 = int(input('Insira o segundo número:    '))
                print(f'RESULTADO:   {n1 * n2}')
