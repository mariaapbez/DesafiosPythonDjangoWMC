# Exercícios: Conceitos Básicos em Python

# Exercício 1: ----------------------------------------------------------------------------------
'''
Faça um Programa que peça um número e então mostre a mensagem:
-> O número informado foi [número].
'''

print('\nExercício 1 - Programa 1')

numero = int(input('\nInsira um número: '))
print(f'\nO número informado foi [{numero}].\n\n***')


# Exercício 2: ----------------------------------------------------------------------------------
'''
Faça um Programa que peça dois números e imprima a soma.
'''

print('\nExercício 2 - Programa 2')

numero1 = int(input('\nInsira um número: '))
numero2 = int(input('Insira outro número: '))
soma = numero1+numero2

print(f'\nVocê inseriu os números {numero1} e {numero2}, cuja a soma é {soma}.\n\n***')


# Exercício 3: ----------------------------------------------------------------------------------
'''
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
'''
print('\nExercício 3 - Programa 3')

temp_celsius = int(input('\nInforme a temperatura atual em graus Celsius (°C): '))

temp_fahrenheit = (temp_celsius * 1.8) + 32

print(f'A temperatura informada ({temp_celsius}°C) convertida para Fahrenheit é {temp_fahrenheit:.0f}°F.\n\n***')


# Exercício 4: ----------------------------------------------------------------------------------
'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
'''

print('\nExercício 4 - Programa 4\n')

valor_hora = float(input('Quanto você ganha por hora trabalhada? '))
horas_mes = float(input('Quantas horas você trabalha por mês? (considerar 4 semanas) '))

salario_mes = valor_hora * horas_mes

print(f'\nSeu salário este mês é de R$ {salario_mes:.2f}.\n\n***')