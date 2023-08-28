# Exercícios: Tomada de Decisão e Estruturas de Repetição

# Exercício 1: ----------------------------------------------------------------------------------
'''
Faça um Programa que peça dois números e imprima o maior deles.
'''

print('\nExercício 1 - Programa 1')

numero1_inserido = float(input('\nDigite um número: '))
numero2_inserido = float(input('\nDigite outro número: '))

if numero1_inserido > numero2_inserido:
    print('\n',numero1_inserido,'é o número maior.\n')
else:
    print(f'\n {numero2_inserido} é o número maior.\n') # outra forma escrever o código para chamar a função


# Exercício 2: ----------------------------------------------------------------------------------
'''
Faça um programa que pergunte em que turno você estuda. Peça para digitar M-Matutino, V-Vespertino ou N-Noturno. Imprima a mensagem "Bom Dia!", "Boa tarde!", "Boa Noite!" ou "Valor Inválido", conforme o caso.'''

print('\nExercício 2 - Programa 2')

turno1 = 'M'
turno2 = 'V'
turno3 = 'N'

turno = input('Em qual turno você estuda? (Digite M (Manhã), V (Vespertino) ou N (Noturno): \n')
turno = turno.upper()
while turno != 0:
    if turno == turno1:
        print('\nBoa Dia! \n')
        break

    elif turno == turno2:
        print('\nBoa Tarde! \n')
        break

    elif turno == turno3:
        print('\nBoa Noite! \n')
        break

    else:
        print('\nValor inválido! \n')
        #turno = input('Em qual turno você estuda? (Digite M (Manhã), V (Vespertino) ou N (Noturno): \n')
        break
            
# Exercício 3: ----------------------------------------------------------------------------------
'''
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''

print('\nExercício 3 - Programa 3')

nota = float(input('Insira uma nota entre 0 e 10: \n'))

while nota > 10 or nota < 0:
    nota = float(input('\nA nota inserida não é válida. Por favor insira um valor entre 0 e 10: \n'))

print(f'\nNota {nota} registrada.\n')
