import random, sys, os, time
log = False
rta = False
ln = ["DaniDev"]
ls = ["2808"]
rep = [0]
nc = "DaniDev"
sc = "2808"
nu = "DaniDev"
ra = rep[ln.index(nc)]
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
        os.system('cls')
        if tl == 1:
                nc = input('Insira nome de usuário:   ')
                os.system('cls')
                sc = input('Insira senha:   ')
                os.system('cls')
                while sc == nc:
                    print('A senha não pode ser o nome de usuário!')
                    sc = input('Insira senha:   ')
                while nc in ln:
                    print('Nome de usuário já está em uso!')
                ln.append(nc)
                ls.append(sc)
                rep.append(0)
                os.system('cls')
        elif tl == 2:
                nl = input('Informe o nome de usuário:   ')
                os.system('cls')
                sl = input('Informe a senha:   ')
                os.system('cls')
                while sl not in ls or nl not in ln or sl != ls[ln.index(nl)] : 
                    tent -= 1
                    print('Nome de usuário ou senha está incorreto!')
                    print(f'{tent} tentativa(s) restantes(s)')
                    os.system('pause')
                    os.system('cls')
                    nl = input('Informe o nome de usuário:   ')
                    os.system('cls')
                    sl = input('Informe a senha:   ')
                    os.system('cls')
                    if tent <= 0:
                        for i in range(tmp, 0, -1):
                            print(i)
                            time.sleep(1)
                            os.system('cls')
                        tmp += 30
                        break
                        os.system('cls')
                else:
                    nu = nc
                    print(f'Olá {nu}')
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
                |4| REPUTAÇÃO
                |5| SAIR DA CONTA

==============================================================================
'''))
        os.system('cls')
        if to == 1:
            ndado = int(input('Quantos lados tem o dado?'))
            os.system('cls')
            dado = random.randint(1, ndado)
            print(dado)
            os.system('pause')
            os.system('cls')
        elif to == 2:
            op = int(input('''
            QUAL OPERAÇÃO SERÁ USADA?

        |1| ADIÇÃO
        |2| SUBTRAÇÃO
        |3| MULTIPLICAÇÃO
        |4| DIVISÃO
'''))
            os.system('pause')
            os.system('cls')
            if op == 1:
                n1 = int(input('Insira o primeiro número:   '))
                n2 = int(input('Insira o segundo número:    '))
                print(f'RESULTADO:   {n1 + n2}')
                os.system('pause')
                os.system('cls')
            elif op == 2:
                n1 = int(input('Insira o primeiro número:   '))
                n2 = int(input('Insira o segundo número:    '))
                print(f'RESULTADO:   {n1 - n2}')
                os.system('pause')
                os.system('cls')
            elif op == 3:
                n1 = int(input('Insira o primeiro número:   '))
                n2 = int(input('Insira o segundo número:    '))
                print(f'RESULTADO:   {n1 * n2}')
                os.system('pause')
                os.system('cls')
            elif op == 4:
                n1 = int(input('Insira o primeiro número:   '))
                n2 = int(input('Insira o segundo número:    '))
                print(f'RESULTADO:   {n1 / n2}')
                os.system('pause')
                os.system('cls')
        elif  to == 3:
            mult = 0
            npon = int(input('Insira número:   '))
            for i in range(2, npon):
                if npon % i == 0:
                    print(f'Múltiplo de {i}')
                    mult += 1
            if mult == 0:
                print(f'{npon} é primo!')
                os.system('pause')
                os.system('cls')
            else:
                print(f'{npon} tem {mult} múltiplos maiores que 2 e menores que ele mesmo.')
                os.system('pause')
                os.system('cls')
        elif to == 4:
            rta = True
            while rta == True:
                ro = int(input('''
=================================|REPUTAÇÃO|==================================

                |1| SALA DA FAMA
                |2| SUA REPUTAÇÃO
                |3| PLUS REPUTAÇÃO
                |4| VOLTAR
                
==============================================================================
'''))
                if ro == 1:
                    x = max(rep)
                    print(f'''
================================|SALA DA FAMA|================================

                |1| {ln[rep.index(x)]} - {x}
                
==============================================================================
''')
                    os.system('pause')
                    os.system('cls')
                elif ro == 2:
                    print(f'Sua reputação atual é: {ra}')
                    os.system('pause')
                    os.system('cls')
                elif ro == 3:
                    print('Em desenvolvimento!')
                    os.system('pause')
                    os.system('cls')
                elif ro == 4:
                    rta = False
                    os.system('cls')
                
