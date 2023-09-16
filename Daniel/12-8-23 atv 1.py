import random
#Cria uma lista
frutas = ['maçã' , 'banana' , 'pêra']
print(frutas)
#Adiciona um item
frutas.append('abacaxi')
print(frutas)
#Item da posição X
print(frutas[2])
#Remove o último item da lista
frutas.pop()
print(frutas)
frutas.append('uva')
print(frutas)
#remove um item específico
frutas.remove('banana')
print(frutas)
#Mostra a lista de modo bonitinho
for i in frutas:
    print(i)
#Mostra a posição de tal item
for i in range(len(frutas)):
    print(f'Fruta {i}: {frutas[i]}')
print('A fruta pêra está na posição:', frutas.index('pêra'))
frutas.append('abacaxi')
print(frutas)
#Organiza por ordem alfabética
frutas.sort()
print(frutas)
print('A fruta pêra está na posição:', frutas.index('pêra'))
#Sorteia um item
print(f'A fruta sorteada foi: {frutas[random.randint(0, len(frutas)-1)]}')
print(frutas)
#Embaralha a lista
random.shuffle(frutas)
print(frutas)
print('''
    MESMA COISA, SÓ QUE O PROFESSOR QUE FEZ
''')
# Cria uma lista
frutas = ['maçã', 'banana', 'pêra', 'uva']

# Adiciona um item
frutas.append('abacaxi')

# Remove um item
frutas.remove('banana')

# Mostrar a lista
print(frutas)

# Mostra um item
print(frutas[0])

# Lista os nomes dos itens
for x in frutas:
    print(x)

# Lista as posições dos itens
for x in range(len(frutas)):
    print(f'Fruta {x}: {frutas[x]}')

# Ordena a lista
frutas.sort()

# Embaralha a lista
random.shuffle(frutas)

# Encontra a posição de um item
print(frutas.index('pêra'))

# Sorteia um item
print(frutas[random.randint(0,len(frutas)-1)])
print('Outra vez...')

#aplicando os conceitos ensinados aqui:
#http://www.devfuria.com.br/python/listas/
#https://www.programiz.com/python-programming/list

from os import system, name

def clear(ide = "x"):
  '''
  Clear é uma função que limpa o console
  de acordo com a IDE e as biliotecas 
  utilizadas. No google colab ela usa
  a 'IPython.display', mas fora dele
  pode ser usada a 'os' que permite
  acessar os comandos do sistema
  operacional: cls ou clear.

  Abaixo estão os comandos para importar
  as bibliotecas.

  from os import system, name
  from IPython.display import clear_output

  Como parametro informe a IDE que está
  utilizando: 'g' para o Google
  ou 'x' para qualquer outra.
  '''

  if ide != 'g': 
    if name == "nt":
      _ = system('cls')
    else:
      _ = system('clear')

  #Se tiver importado a IPython
  #use o método: clear_output()

def continuar():
  input("\naperte qualquer coisa p/ continuar\n")
  
  
#nomes é uma lista de elementos.
nomes = ['B','A',4] 

'''
  Dentro de nomes a 3 posições ocupadas:
  0: 'B'
  1: 'A'
  2: '4'
  
  Se eu quiser saber a posição de 
  um elemento dentro da lista,
  eu posso usar o comando index.

  lista.index[elemento]

  ex:
  print(nomes.index('A'))
  ele vai me retornar a posição 1.
  
'''

print("Lista Nomes: ",nomes)
print("Indice do elemento 'A':",nomes.index('A'))

continuar()

'''
  Você pode adicionar novos elementos manualmente da
  seguinte forma:

  criando a lista:
  nomeDaLista = [ElementosDaLista]
  ex: odd[2,4,6,8]

  adicionando um item em uma posição especifica:

  nomeDaLista[posicao] = elemento
  ex: odd[0] = 1 

  adcionando diversos itens em posições epecificas:
  nomeDaLista[posicaoInicial:posicaoFinal] = [NovosEle]
  odd[1:4] = [3, 5, 7] << print (odd) = 1,3,5,7

'''

'''
  Para adcionar novos elementos na lista, por um comando, usamos o append ou o extend.
  A diferença é que o append adciona de 1 em 1
  e o extend adciona varios elementos de uma vez só.

'''
nomes.clear() #limpando a lista.
nomes.append(input("Digite seu 1º Nome\n"))
nomes.append(input("Digite seu 2º Nome\n"))

print("\nAtualização da Lista Nomes:",nomes) #exiba a lista nomes.

nomes.extend(["Xuxu","Bola","Lindao"])

print("\nNovos nomes também foram inseridos:\n",nomes)

continuar()
clear()

'''
  Pra verificar se um elemento
  especifo está dentro da lista
  usamos o comando in:

  elemento in lista

  exemplo:
  
    nomes = ['B','A',4]
  
    4 in nomes

    como o 4 está na 2º pos da lista,
    o in vai retonar como True.

'''

nomes = ['B','A',4]
print("\nMudando a lista para:",nomes)

if (4 in nomes) == True:
  print("\nO 4 está dentro da lista")
  
  if (2 in nomes) != True:
    print("Mais o 2, não!")

else:
  print("\nO 4 NÃO está dentro da lista")


continuar()

'''
  Para inserir elementos em uma posição
  especifica, usamos o comando insert.

  lista.insert(posição,elemento)

  exemplo:
  nomes = ['A','B']
  nomes.insert(1, 'Xuxu')
  resultado = ['A','Xuxu', 'B']

'''
nomes = ['A','B']
print("\nAtualização da Lista Nomes:",nomes)
nomes.insert(1, 'Xuxu')
print("inserindo um xuxu na lista.")
print("\nResultado:",nomes)

continuar()

'''
  E para remove-los basta usarmos o comando remove.
  lista.remove(elemento)

  exemplo:
  nomes = ['A','Xuxu', 'B']
  nomes.remove('Xuxu')
  resultado = ['A','B']

'''
print("\nRemovendo esse elemento...")
nomes.remove("Xuxu")
print("Resultado: ",nomes)

continuar()

'''
  Para exibir um determinado elemento da lista
  basta passar a posição junto com o nome.

  print(lista[posicao])

  exemplo:
  nomes = ['A','B']
  print(nomes[1]) #vai exibir o B

'''
print("\nAgora o 2º Elemento da Lista é:",nomes[1])

'''
  Para remover um item pela posição/indice, usamos o 
  comando pop.
  Exemplo:
  nomes = ['A', 'B']
  nomes.pop(1)
  print(nomes) #agora só existe o A.

  Outra forma de fazer isso é com o comando del:

  Exemplo:
  nomes = ['A', 'B']
  del(nomes[1])
  print(nomes) #agora só existe o A.


'''

print("\nVamos remove-lo também.")
nomes.pop(1)
print("Resultado:",nomes)

continuar()
clear()

'''
  Agora vamos organizar os elementos da lista
  em ordem alfabetica, usando o comando sort
  Exemplo:
  nomes = ["C","D","A","B",] 
  nomes.sort()
  print(nomes) #["A","B","C","D"]

  obs. também funciona com numeros.
  Mas não com os 2 juntos.

  Para exibir a lista organizada usamos o sorted.
  print(sorted(nomes))
  mas ele não atualiza o valor dela, só exibe.

'''
print("Organizando os Elementos da Lista:")
nomes = ["C","D","A","B",]
print("\nNova Lista:",nomes)
nomes.sort()
print("Lista Organizada:",nomes)

print("\nVamos ver se funciona com numeros:")
numeros = [5,0,7,1,2,8]
print("\nLista de Numeros:",numeros)

print("c/ sorted",sorted(numeros))
print("s/ sorted",numeros)

print("\nOHHHH FUNCIONA \o/. ")

continuar()

'''
  Aproveitando que agora temos uma lista de numeros.
  Para pegar o valor max e min de uma lista, basta
  usar esses comandos: max e min.
  
  Exemplo:

  numeros = [5,0,7,1,2,8]
  print(max(numeros)) #8
  print(min(numeros)) #0
'''

print("\nAlias...")
print("O maior numero dessa lista é:",max(numeros))
print("O menor numero dessa lista é:",min(numeros))

continuar()


'''
  Curiosidade, você pode pegar o menor numero acima de 0
  usando um for junto com a função min.

  Exemplo:
  #n = numero;
  menorNumero = min(N for N in lista if N > 0)

  Explicando a Função:
  Pegamos a função min, que retorna o menor valor de uma lista, e demos a ela uma "expressão geradora".
  Essa expressão pode ser lida como: 
  "leia todos os números da lista (N for N in lista)
   que sejam maiores que zero   (if N ! = 0)".

'''
menorNumero = min(N for N in numeros if N > 0)
print("E o menor numero acima de 0 é:",menorNumero)

continuar()
clear()

'''
Para contar a quantidade de elementos
dentro da lista, use o método count()
que funciona também com strings.

Por exemplo:
  lista = ["A", "A", "B"]
  lista.count("A") -> 2
'''
lista = ["A", "A", "B"]
print("Existem ", lista.count("A"), "A's em \n", lista)
continuar()

'''
  Dica use o for e a função enumerate
  para correr a lista e exibir seus 
  elementos ordenadamente.

  nomes = ["A","B","C","D"]
  
  for i, e in enumerate(nomes):
    print (i,e) #indice,elemento.
  
  Resultado:
  0 A
  1 B
  2 C
  3 D

'''
nomes = ["A","C","B","D"]
print("\nNova Lista:",nomes)
print("\nEnumerando a Lista de Nomes....")
print("\nIndice | Elemento:")

for i, e in enumerate(nomes):
  print ("\n ",i,"  |",e)

continuar()
clear()

'''
  Você também pode unir e clonar listas da mesma forma
  que fazemos com uma variavel do tipo string.
  Exemplo:
  letras_A  = ["A","C","B","D"]
  letras_B  = ["E","F","G","H"]
  letras_AB = letras_A+letras_B
  print(letras_AB) = ["A","C","B","D","E","F","G","H"]
  
'''

print("\nSomando Listas:")
letras_A  = ["A","C","B","D"]
print("\nLista 1:",letras_A)
letras_B  = ["E","F","G","H"]
print("\nLista 2:",letras_B)
letras_AB = letras_A+letras_B
print("\nResultado da Soma das Listas: ",letras_AB)

#continuar()
