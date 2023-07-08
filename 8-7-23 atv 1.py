nome = ""
senha = ""
dica = ""
while True:
    menu = int(input('''
--------------------
|1 | CADASTRAR      |
|-------------------|
|2 | LOGAR          |
--------------------
'''))
    if menu == 1:
        print("CADASTRO:")
        nome = input("Insira o nome de usuário: ")
        senha = input("Insira senha: ")
        dica = input("Insira a dica para a senha: ")
        print("CADASTRO REALIZADO COM SUCESSO")
    elif menu == 2:
        print("LOGIN:")
        tnome = input("Informe o nome de usuário: ")
        print(dica)
        tsenha = input("Informe a senha: ")
        if tnome == nome and tsenha == senha:
            print("Bem vindo,",nome)
            while True:
                opcao = int(input("Digite 1 para ficar e 2 para sair"))
                if opcao == 1:
                    print("Ficou")
                elif opcao == 2:
                    break
    else:
        print("Acesso negado")
else:
    print("Opção inválida")
