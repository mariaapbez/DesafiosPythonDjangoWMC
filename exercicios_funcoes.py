# Exercícios: Funções

# Exercício 1: ----------------------------------------------------------------------------------
'''
Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
'''

print('\nExercício 1 - Programa 1')
def producao(cliente1, cliente2, cliente3):
    total_assar = cliente1 + cliente2 + cliente3
    print(f'\nQuantidade de pães para assar: {total_assar}\n')
    
nome = input('Qual o seu nome? ')
cliente1 = int(input('insira a quantidade de pães desejada: '))
nome = input('Qual o seu nome? ')
cliente2 = int(input('insira a quantidade de pães desejada: '))
nome = input('Qual o seu nome? ')
cliente3 = int(input('insira a quantidade de pães desejada: '))

producao(cliente1, cliente2, cliente3)


# Exercício 2: ----------------------------------------------------------------------------------
'''Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
'''

print('\nExercício 2 - Programa 2')
def reverso_numero():
    numero_inserido = input('\nDigite um número: ')     # solicita inserção do numero
    algarismos_do_numero = list(numero_inserido)        # coloca itens da numero em uma lista
    algarismos_do_numero.reverse()                            # inverte ordem dos itens na lista
    numero_invertido = ''.join(algarismos_do_numero)            # junta itens da lista em novo numero, neste caso, sem separações, pois não é informado nenhum separador entre as ''.
    print(f'\nO inverso do número digitado é: {numero_invertido}.\n')
    
reverso_numero()


# Exercício 3: ----------------------------------------------------------------------------------
'''
Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para cada opção, crie uma função. Crie uma terceira, que é um menu para o usuário escolher a opção desejada, onde esse menu chama a função de conversão correta.
'''

print('\nExercício 3 - Programa 3')
def seletor():
    if selecao == True:
        conversor_celsius()
    else:
        conversor_fahrenheit()

def conversor_celsius():
    temp_celsius1 = int(input('\nInforme a temperatura em graus Celsius (°C) que deseja converter: '))
    temp_fahrenheit1 = (temp_celsius1 * 1.8) + 32
    print(f'\nA temperatura informada ({temp_celsius1}°C) convertida para Fahrenheit é {temp_fahrenheit1:.0f}°F.\n\n***')

def conversor_fahrenheit():
    temp_fahrenheit2 = int(input('\nInforme a temperatura em graus Fahrenheit (°F) que deseja converter: '))
    temp_celsius2 = (temp_fahrenheit2 - 32) / 1.8 
    print(f'\nA temperatura informada ({temp_fahrenheit2}°F) convertida para Celsius é {temp_celsius2:.0f}°C.\n\n***')

seleciona_conversor = int(input('\nVocê deseja converter grau:\nOPÇÃO 1 - Celsius (°C) para Fahrenheit (°F) -> [Digite 1] ou\nOPÇÃO 2 - Fahrenheit (°F) para Celsius (°C) -> [Digite 2]? '))
if seleciona_conversor > 1:
    selecao = False
else:
    selecao = True


seletor()