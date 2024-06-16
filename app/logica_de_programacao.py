# Matéria de Lógica de programação com Phyton do curso de Análise e Desenvolvimento de Sistemas #

#   VARIÁVEIS, DADOS E SEUS TIPOS   #

nota = 8.5  # Tipo float
print()

disciplina = 'Lógica de Programação e Algoritimos'  # Tipo String

print(nota)
print(disciplina)
print('Disciplina:', disciplina, 'Nota', nota ) # Imprime concatenando Strings e as Variáveis
print()

# --------------------------------- #

# VARIÁVEIS LÓGICAS ( == , <= , >= , != , ! ) # 

a = 1
b = 3
c = 5

resposta = a == b # false
print(resposta)

maior_igual = c >= b
print(maior_igual)

menor_igual = b <= c
print(menor_igual)

diferente = a != b
print(diferente)
print()

# --------------------------------- #

#   VARIÁVEIS STRING    ( @ , # , $ , % , & , A , B , C ) #

nome = 'Evandro'

print(nome)
print()
print(nome[0])  # Acessando os Caracteres pelo índice
print(nome[1])
print(nome[2])
print(nome[3])
print(nome[4])
print(nome[5])
print(nome[6])
print()

nome = nome + ' Silva'
print(nome)
print(nome, '-'*5) # Multiplica o caracter - em 5 vezes
print()

# Composição por marcador de posição utilizando % #

nota = 8.2
idade = 32
materia = 'Lógica Python'
logica_programacao = 'Nota da Lógica %.2f' %nota
print(logica_programacao)
print()

print('Idade: %i' %idade)
print('Qual a matéria? %s' %materia)
print()

# Composição Moderna utilizando {} e .format()#

print('idade {} '.format(idade))
print('Qual a materia? {}'.format(materia))
print()

# Composicão com f-string #

print(f'idade: {idade}')
print(f'Qual a materia? {materia}')
print()

# Fatiamento de Strings de um Indice ate outro Indice ex: [0:6}#

print(materia[0:1]) # L
print(materia[0:6]) # Lógica
print()

# Tamanho da String com length #

print(len(materia))

linguagem = 'Python'
tamanho = len(linguagem)
print(tamanho)
print()

# --------------------------------- #

#   FUNÇÃO DE ENTRADA E FLUXO DE EXECUÇÃO   utilizando o input() para receber os dados de entrada   #

nome = input("Qual é o seu nome?")
idade = input('Qual é a sua idade?')
instituicao = input('Qual a sua instituição?')

print(f'Seja bem vindo: {nome}', f'Voçê é novo com: {idade} de idade', f'Essa instituição {instituicao} é muito boa ')
print()

# --------------------------------- #

#   UTILIZANDO CASTING PARA CONVERTER TIPOS DE DADOS  # por padrão o input retorna uma String, casting converte em float, double, int etc...

nota_1 = float(input("Digite a primeira nota : "))
nota_2 = float(input("Digite a segunda : "))
nota_3 = float(input("Digite a terceira : "))
nota_4 = float(input("Digite a quarta : "))

media = int((nota_1 + nota_2 + nota_3 + nota_4)/4)
if (media >= 7):
    print(f"A sua média é {media}, meus parabens!")
elif (media < 7):
    print(f"Precisa melhorar essa nota! {media}")
print()

#   TESTE DE MESA   # observando o fluxo de dados

X = 1 # x = 1
Y = 1 # y = 1
Z = X + Y # z = 2

X = X + 2 # x = 3
Y = Y - 1 # y = 0
Z = X + Y # z = 3

print(Z) # 3
print()

# --------------------------------- #

#   CONTROLE DE FLUXO E CONDICIONAIS    # if, else, elif.  boolean portas lógicas multiplas condições ( and , or , not , )

# and é ( E ) , or é ( ou ) , not é ( negação )

numero_1 = int(input("Digite o primeiro numero : "))
numero_2 = int(input("Digite o segundo : "))
numero_3 = int(input("Digite o terceiro : "))
numero_4 = int(input("Digite o quarto : "))

if (numero_1 > numero_2 and numero_1 > numero_3 and numero_1 > numero_4):
    print(f"O primeiro numero {numero_1} é maior.")

elif (numero_2 > numero_3 and numero_2 > numero_4 and numero_2 > numero_1):# elif é o mesmo que else if
    print(f"O segundo numero {numero_2} é maior.")

elif (numero_3 > numero_1 and numero_3 > numero_2 and numero_3 > numero_4):
    print(f"O terceiro {numero_3} é maior.")

elif (numero_4 > numero_1 and numero_4 > numero_2 and numero_4 > numero_3):
    print(f"O quarto {numero_4} é maior.")

else :
    print("Numero nùmero inválido!")
print()

# --------------------------------- #

#   ESTRUTURAS DE REPETIÇÃO     #   while (enquanto verdadeiro) 

X = 1
while (X <= 10): # enquanto verdadeiro executa o loop
    print(X)
    X += 1
print()

inicial = int(input("Digite o inicio da iteração: "))
final = int(input("Digite o final do intervalo: "))
count = inicial

while (count <= final):
    if (count % 2 == 0): # loop de iteração dos numeros pares entre os intervalos inicial, final
        print(count)
    count += 1
print()

print("Voçê está no loop até digitar a palavra | sair |")
while True:
    x = input("")
    if (x == "sair"): # encerrando o loop infinito com break ao satisfazer a condição do if
        break
print("Loop incerrado...")

print("Pode digitar qualquer numero que voçê quiser porem, somente o numero 3 para o loop")
while True:
    x = int(input(""))
    if (x != 3):
        print("Digite o 3 para sair")
        continue
    if (x == 3):
        print("Voçê digitou o 3 encerrando o laço!")
        break
print()

# --------------------------------- #

#   ESTRUTURA DE REPETIÇÃO FOR (PARA)   #

for i in range(10): # iterando de 1 a 9
    print(i)
print()

for i in range(1,20,2): # iterando de 1 até 19 no intervalo de 2 em 2
    print(i)
print()

for i in range(20, 0, -1): # print a variável i dcrementando de 1 em 1 até 1
    print(i)
print()

materia = "Lógica"
for i in range(0, len(materia)): # iteração de caracter a caracter, varrendo a string e imprimindo
    print(materia[i])
print()

for i in range(0, len(materia)):
    print(materia[i], end="") # utilizando end="", ignora-se a quebra de linha
print()

for tabuada in range(1, 11):  # usando o for in range para criar a tabuada
    print(f"Tabuada do número: {tabuada}")
    print()
    for i in range(1, 11):
        print(f"{tabuada} x {i} = {i * tabuada}")
        print()
print()

# --------------------------------- #

#   FUNÇÕES parâmetros, escopo e retorno    #

def realce ():
    print('|' * 2, '-' * 10, '|' * 2)

realce()
print("     MENU")
realce()

def media ():   # função media retorna a media entre x, y e z.
    x = 10
    y = 20
    z = 30
    calculo = (x + y + z)/3
    return calculo

print("")

print(media())

print("")
realce()
print("")
def soma (num_1, num_2):    # função soma com passagem de parametros
    x = num_1 + num_2
    return x

print(f"A soma é {soma(10, 10)}.")  # impressão da soma formatado com f-string

# --------------------------------- #

# APLICADO A LÓGIDA APREDIDA NAS AULAS DE "LÓGICA E ALGORITIMOS COM PYTHON  # criado uma tabuada completa até o numero 10

def soma1 ():
    for i in range(1, 11):
        print("")
        print(f"Soma do número: {i}")
        print("")
        for x in range(1, 11):
            print(f"{i} + {x} = {i + x}")

def subtracao ():
    for i in range(1, 11):
        print("")
        print(f"Subtração do número: {i}")
        print("")
        for x in range(1, 11):
            print(f"{i} - {x} = {i - x}")
def multiplica ():
    for i in range(1, 11):
        print("")
        print(f"Multiplicação do número: {i}")
        print("")
        for x in range(1, 11):
            print(f"{i} x {x} = {i * x}")

def divisao ():
    for i in range(1, 11):
        print("")
        print(f"Divisão do número: {i}")
        print("")
        for x in range(1, 11):
            res = i / x
            print(i, "/", x, " = %.2f" % res)

print(soma1())
print(subtracao())
print(multiplica())
print(divisao())
print()

# --------------------------------- #

#   ESTRUTURAS DE DADOS , TUPLAS(), LISTAS[], DICIONÁRIOS {} E CONCEITOS DE MÉTODOS PARA STRINGS    #

dias_semana = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado", "Domindo") # Tupla: os dados não podem ser alterados é uma estrutura de dados estatica

print(dias_semana[0]) # acessando os indices da tupla
print(dias_semana[1])
print(dias_semana[2])
print(dias_semana[3])
print(dias_semana[4])
print(dias_semana[5])
print(dias_semana[6])

for iten in dias_semana: # iterando os itens da tupla e imprimindo os dias da semana
    print(f"Dias da semana: {iten}")
print()
def soma (*num): # variavel com * cria uma tupla
    acumulador = 0
    print(f"Tupla: {num}")
    for i in num:
        acumulador += i
    return acumulador

print(f"Resultado: {soma(1, 2, 3, 4, 5)}") #adiciona parametros na tupla para efetuar a soma


mochila = ['Notebook', 'pasta de dente', 'presto barba'] # lista estrutura de dados mutaveis onde pode ser alterado, removido, trocado, totalmente manipulado
print(mochila)
print()

mochila.append('espelho') # adiciona no final da lista append()

mochila.insert(1, 'fone de ouvido') # inseri em um determinado indice insert()

del mochila[3] # deleta um determinado indice del

mochila.remove('pasta de dente') # deleta o dado informado remove()

for iten in mochila:
    print(iten)
print()

lista_referenciada = mochila #lista referenciada aponatndo para os dados da mochila
print(lista_referenciada)

mochila_2 = mochila[:] # criado mochila2 sendo uma cópia da mochila utilizando [:]
print(mochila_2)

lista_dentro_de_lista = mochila_2[0][0:8] # acessa a string Notebook pelo indice 0 e os caracteres de 0 a 8
print(lista_dentro_de_lista)

lista_dentro_de_lista = mochila_2[1][0:14] # acessa a string fone de ouvido no indice 1 e os caracter 0 a 14
print(lista_dentro_de_lista)

lista_dentro_de_lista = mochila_2[2][0:7] # acessa a string espelho no indice 2 e os caracteres de 0 a 7
print(lista_dentro_de_lista)

print()
realce()
print()

quarto = ["Guarda roupa", "Cama", "Comoda", "Tv"] # iterando os itens do quarto e pegando de letra em letra no for dentro do for
for item in quarto:
    for letra in item:
        print(letra, end='')
print()

compras = []

for i in range(3): # lista de compras adiciona os itens, quantidades e valor
    nome = input("Digite o produto: ")
    qtd = int(input("Digite a quantidade: "))
    valor = float(input("Digite o valor: "))
    compras.append([nome, qtd, valor])

print(compras)
print()

game = {'nome':'God of War', 'tipo':'Ação e aventura', 'console':'multiplataforma'} # dicionário estutura de dados com chave e valor

print(game['nome'])
print(game['tipo'])
print(game['console'])

print()
realce()
print()

for values in game.values(): # retorna os valores do dicionario
    print(values)
print()

for keys in game.keys(): # retorna as chaves do dicionario
    print(keys)
print()

for items in game.items(): # retorna os itens do dicionario
    print(items)
print()

games = []  # dicionarios com cahves e valor dentro da lista games

game1 = {'genero':'mudo aberto', 'nome':'gta', 'preço':190}

game2 = {'genero':'simulação', 'nome':'euro truck', 'preço':60}

game3 = {'genero':'fps', 'nome':'counter strike', 'preço':59}

games = [game1, game2, game3]

print(games)
print()

for game in games:  # itera na lista games
    for chave, valor in game.items():   # retorna a iteração pegando as chaves e os valores com .items()
        print(f"Chave: {chave}, Valor: {valor}")
print()

# MÉTODOS COM STRINGS   #

aula = list("Lógica e Algoritimos") # cria uma lista de caracteres da string separadamente
print(aula)
print()

print(''.join(aula)) # agrupa os caracteres da string com o metodo .join()
print()
print(''.join(aula).lower()) # converte a string em letra minuscula com .lower()
print()
print(''.join(aula).upper()) # converte a string em letra maiuscula com .upper()
print()

nome = "Evandro Silva do Nascimento"
print(nome.split(' ')) # divide a string com .split()
print()
print(nome.replace("Silva", "S")) # substituição da string Silva por S com .replace()



