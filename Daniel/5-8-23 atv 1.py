palavra = input("Digite uma palavra: ")
frase = input("Digite uma frase: ")
if palavra in frase:
    print(f'A palavra {palavra} foi encontrada na frase {frase}')
else:
    print(f'A palavra {palavra} não foi encontrada na frase {frase}')
