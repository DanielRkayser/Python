print("cadastro")
a = input("Digite o nome de usuário:")
b = input("Digite a senha:")
d = input("Deseja inserir uma dica para a senha?")
if d == "sim" or d == "Sim" or d == "s" or d == "S":
    c = input("Insira uma dica para a senha, para o caso de você se esquecer dela.")
else:
    print("Certo")
print("CADASTRO REALIZADO COM SUCESSO")
print("Olá,",a)
