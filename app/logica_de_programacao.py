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