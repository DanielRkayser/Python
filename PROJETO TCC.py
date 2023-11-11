import random, sys, os, time
log = False
rta = False
tjo = False
ln = ["DaniDev"]
ls = ["2808"]
rep = [30]
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
                    nc = input('Insira nome de usuário:   ')
                os.system('cls')
                sc = input('Insira senha:   ')
                os.system('cls')
                ln.append(nc)
                ls.append(sc)
                rep.append(30)
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
                        tent = 0
                        os.system('cls')
                else:
                    nu = nl
                    idu = ln.index(nu)
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
                os.system('cls')
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
                    pre = int(input('''
===============================|PLUS REPUTAÇÃO|===============================
                
                |1| ADIVINHE O NÚMERO
                |2| NÚMERO VENCEDOR
                |3| VOLTAR

==============================================================================
'''))
                    if pre == 1:
                        rta = False
                        tjo = True
                        while tjo == True:
                            dif = int(input('''
                            Escolha a dificuldade:
                    |1| Fácil         • 1-5
                    |2| Médio         • 1-10
                    |3| Normal        • 1-15
                    |4| Difícil       • 1-25
                    |5| Muito difícil • 1-50
                    |6| IMPOSSÍVEL    • 1-100
                    |7| Sair
'''))
                            os.system('cls')
                            if dif == 1:
                                chu = int(input('Escolha um número de 1-5:    '))
                                res = random.randint(1, 5)
                                if  chu == res:
                                    print(f'Parabéns! Você ganhou 15 REP.')
                                    ra += 15
                                else:
                                    print(f'Você perdeu 5 REP')
                                    ra -= 5
                            elif dif == 2:
                                chu = int(input('Escolha um número de 1-10:    '))
                                res = random.randint(1, 10)
                                if  chu == res:
                                    print(f'Parabéns! Você ganhou 25 REP.')
                                    ra += 25
                                else:
                                    print(f'Você perdeu 7 REP')
                                    ra -= 7
                                                
                                chu = int(input('Escolha um número de 1-5:    '))
                                res = random.randint(1, 5)
                                if  chu == res:
                                    print(f'Parabéns! Você ganhou 15 REP.')
                                    ra += 15
                                else:
                                    print(f'Você perdeu 5 REP')
                                    ra -= 5
                            elif dif == 3:
                                chu = int(input('Escolha um número de 1-15:    '))
                                res = random.randint(1, 10)
                                if  chu == res:
                                    print(f'Parabéns! Você ganhou 30 REP.')
                                    ra += 30
                                else:
                                    print(f'Você perdeu 10 REP')
                                    ra -= 10
                                                
                                chu = int(input('Escolha um número de 1-5:    '))
                                res = random.randint(1, 5)
                                if  chu == res:
                                    print(f'Parabéns! Você ganhou 15 REP.')
                                    ra += 15
                                else:
                                    print(f'Você perdeu 5 REP')
                                    ra -= 5
                            elif dif == 4:
                                chu = int(input('Escolha um número de 1-15:    '))
                                res = random.randint(1, 15)
                                if  chu == res:
                                    print(f'Parabéns! Você ganhou 50 REP.')
                                    ra += 50
                                else:
                                    print(f'Você perdeu 15 REP')
                                    ra -= 15
                                                
                            elif dif == 5:
                                chu = int(input('Escolha um número de 1-50:    '))
                                res = random.randint(1, 50)
                                if  chu == res:
                                    print(f'Parabéns! Você ganhou 100 REP.')
                                    ra += 100
                                else:
                                    print(f'Você perdeu 30 REP')
                                    ra -= 30
               
                            elif dif == 6:
                                chu = int(input('Escolha um número de 1-100:    '))
                                res = random.randint(1, 100)
                                if  chu == res:
                                    print(f'Parabéns! Você ganhou 175 REP.')
                                    ra += 175
                                else:
                                    print(f'Você perdeu 50 REP')
                                    ra -= 50
                            elif dif == 7:
                                tjo = False
                                os.system('cls')
                            else:
                                print('vinagre')
                        os.system('cls')
                    elif pre == 2:
                        acn = 0
                        ern = 0
                        nap = int(input('Qual o número que você acha que vai aparecer mais? (1 ou 2) '))
                        while nap != 1 and nap != 2:
                            print('Opção inválida')
                            nap = int(input('Qual o número que você acha que vai aparecer mais? (1 ou 2) '))
                        else:
                            if nap == 1:
                                oap = 2
                            else:
                                oap = 1
                        aqu = int(input('Quantas vezes sortearemos os números?'))
                        for i in range(0, aqu +1):
                            sto = random.randint(1, 2)
                            if sto == 1:
                                acn += 1
                            else:
                                ern += 1
                        if acn > ern:
                            ra += aqu
                            print(f'Você ganhou {aqu} REP')
                        elif ern > acn:
                            ra -= aqu/2
                            print(f'Você perdeu {aqu/2} REP')
                        else:
                            print("Empatou! Nada mudou no seu REP")
                elif ro == 4:
                    rta = False
                    os.system('cls')
        elif to == 5:
            log = False
            os.system('cls')
