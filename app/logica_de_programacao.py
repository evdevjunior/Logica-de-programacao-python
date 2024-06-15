# Matéria de Lógica de programação com Phyton do curso de Análise e Desenvolvimento de Sistemas #

#   VARIÁVEIS, DADOS E SEUS TIPOS   #

nota = 8.5  # Tipo float
disciplina = 'Lógica de Programação e Algoritimos'  # Tipo String

print(nota)
print(disciplina)
print('Disciplina:', disciplina, 'Nota', nota ) # Imprime concatenando Strings e as Variáveis

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

# --------------------------------- #

#   VARIÁVEIS STRING    ( @ , # , $ , % , & , A , B , C ) #

nome = 'Evandro'

print(nome)
print(nome[0])  # Acessando os Caracteres pelo índice
print(nome[1])
print(nome[2])
print(nome[3])
print(nome[4])
print(nome[5])
print(nome[6])

nome = nome + ' Silva'
print(nome)
print(nome, '-'*5) # Multiplica o caracter - em 5 vezes

# Composição por marcador de posição utilizando % #

nota = 8.2
idade = 32
materia = 'Lógica Python'
logica_programacao = 'Nota da Lógica %.2f' %nota
print(logica_programacao)

print('Idade: %i' %idade)
print('Qual a matéria? %s' %materia)

# Composição Moderna utilizando {} e .format()#

print('idade {} '.format(idade))
print('Qual a materia? {}'.format(materia))

# Composicão com f-string #

print(f'idade: {idade}')
print(f'Qual a materia? {materia}')

# Fatiamento de Strings de um Indice ate outro Indice ex: [0:6}#

print(materia[0:1]) # L
print(materia[0:6]) # Lógica

# Tamanho da String com length #

print(len(materia))

linguagem = 'Python'
tamanho = len(linguagem)
print(tamanho)

# --------------------------------- #

#   FUNÇÃO DE ENTRADA E FLUXO DE EXECUÇÃO   utilizando o input() para receber os dados de entrada   #

nome = input("Qual é o seu nome?")
idade = input('Qual é a sua idade?')
instituicao = input('Qual a sua instituição?')

print(f'Seja bem vindo: {nome}', f'Voçê é novo com: {idade} de idade', f'Essa instituição {instituicao} é muito boa ')

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

#   TESTE DE MESA   # observando o fluxo de dados

X = 1 # x = 1
Y = 1 # y = 1
Z = X + Y # z = 2

X = X + 2 # x = 3
Y = Y - 1 # y = 0
Z = X + Y # z = 3

print(Z) # 3

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

# --------------------------------- #

#   ESTRUTURAS DE REPETIÇÃO     #   while (enquanto verdadeiro) 

X = 1
while (X <= 10): # enquanto verdadeiro executa o loop
    print(X)
    X += 1

inicial = int(input("Digite o inicio da iteração: "))
final = int(input("Digite o final do intervalo: "))
count = inicial

while (count <= final):
    if (count % 2 == 0): # loop de iteração dos numeros pares entre os intervalos inicial, final
        print(count)
    count += 1

print("Voçê está no loop até digitar a palavra | sair |")
while True:
    x = input("")
    if (x == "sair"): # encerrando o loop infinito com break ao satisfazer a condição do if
        break
print("Loop incerrado...")

print("Digite os numeros de 1 até 5 sem digitar o numero 3")
while True:
    x = int(input(""))
    if (x != 3):
        print("Digite o 3 para sair")
        continue
    if (x == 3):
        print("Voçê digitou o 3 encerrando o laço!")
        break

# aula 4 estrutura for e repetição aninhadas