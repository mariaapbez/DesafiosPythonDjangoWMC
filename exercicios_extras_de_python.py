# Exercícios: Exercícos Extras de Python

# Exercício 1: ----------------------------------------------------------------------------------
'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e calcule quanto poderia comprar de cada moeda estrangeira. Considere a tabela de conversão abaixo:
Dólar Americano: R$4,91
Peso Argentino: R$0,02
Dólar Australiano: R$3,18
Dólar Canadense: R$3,64
Franco Suiço: R$0,42
Euro: R$5,36
Libra Esterlina: R$6,21
'''
print('\nExercício 1 - Programa 1')
def mudar_carteira():
    moedas = {'Dólares Americanos':'4.91',
              'Pesos Argentinos':'0.02',
              'Dólares Australianos':'3.18',
              'Dólares Canadenses':'3.64',
              'Francos Suiços':'0.42',
              'Euros':'5.36',
              'Libras Esterlinas':'6.21'}
    
    print('\n***Saiba a quanto que equivale o dinheiro (R$) que você tem na carteira, na moeda selecionada***\n')
    
    carteira = float(input('Informe o valor que você tem em sua carteira: '))
    
    moeda = input('\nPara qual moeda deseja fazer a conversão? \n\nDólar Americano - Digite [DA]\nPeso Argentino - Digite [PA]\nDólar Australiano - Digite [DU]\nDólar Canadense - Digite [DC]\nFranco Suiço - Digite [FS]\nEuro - Digite [EU]\nLibra Esterlina - Digite [LE] ')
    
    moeda = moeda.upper()
    if moeda == 'DA':
        moeda = [k for k, v in moedas.items() if v == '4.91'][0]
    if moeda == 'PA':
        moeda = [k for k, v in moedas.items() if v == '0.02'][0]
    if moeda == 'DU':
        moeda = [k for k, v in moedas.items() if v == '3.18'][0]
    if moeda == 'DC':
        moeda = [k for k, v in moedas.items() if v == '3.64'][0]
    if moeda == 'FS':
        moeda = [k for k, v in moedas.items() if v == '0.42'][0]
    if moeda == 'EU':
        moeda = [k for k, v in moedas.items() if v == '5.36'][0]
    if moeda == 'LE':
        moeda = [k for k, v in moedas.items() if v == '6.21'][0]
    
    moeda_valor = float(moedas[moeda])
    conversao = float(carteira) / moeda_valor        
    carteira_conv = input(f'\nR$ {carteira:.2f} equivale a {conversao:.2f} {moeda}.\n')
    print(carteira_conv)
    print('********************************************')

#mudar_carteira()


# Exercício 2: ----------------------------------------------------------------------------------
'''
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço apagar, sabendo que o carro custa R$80,00 por dia e R$0,20 por km rodado.
'''

print('\nExercício 2 - Programa 2')
def locacao(dias, kilometragem):
    total_fatura = (diaria * dias) + (kilometragem * valor_km)
    print(f'\n***O total da fatura da Locação do Veículo é R$ {total_fatura:.2f}.\n')
    print('********************************************')

print('\n***Checando a Fatura da Locação de Veículo***\n\nResponda às perguntas e confira o valor.')
valor_km = float(0.20) 
diaria = float(80.00)    
kilometragem = int(input('\nQual a kilometragem rodada no período da locação? '))
dias = int(input('\nInforme o total de diárias inclusas: '))
    
#locacao(dias, kilometragem)


# Exercício 3: ----------------------------------------------------------------------------------
'''
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário.
Se o salário for até R$ 1000,00 o funcionário terá 20% de aumento.
Entre R$ 1001,00 até R$ 2800,00 o funcionário terá 10% de aumento.
Acima de R$ 2801,00 o funcionário terá 5% de aumento.
'''

print('\nExercício 3 - Programa 3')
def ajuste_salarial():
    salario_atual = float(input('\nQual o seu salário atual? '))
    if salario_atual <= 1000:
        novo_salario = salario_atual + (salario_atual * reajuste_1 / 100) 
        print(f'\nSeu novo salário é {novo_salario:.2f}, com reajuste de 20%.\n')
    elif salario_atual >= 1001 and salario_atual <= 2800:
        novo_salario = salario_atual + (salario_atual * reajuste_2 / 100)
        print(f'\nSeu novo salário é {novo_salario:.2f}, com reajuste de 10%.\n')
    else:
        salario_atual > 2800
        novo_salario = salario_atual + (salario_atual * reajuste_3 / 100)
        print(f'\nSeu novo salário é {novo_salario:.2f}, com reajuste de 5%.\n')
    print('********************************************')
reajuste_1 = 20
reajuste_2 = 10
reajuste_3 = 5
print('\n***Previsão de ajuste salarial***\n\nAté R$ 1.000,00 - reajuste de 20%\nEntre R$ 1.001,00 e R$ 2.800,00 - reajuste de 10%\nAcima de R$ 2.801,00 - reajuste de 5%')
    
#ajuste_salarial()


# Exercício 4: ----------------------------------------------------------------------------------
'''
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor númerico. Ex:n = leiaInt('Digite um n).
'''

print('\nExercício 4 - Programa 4')
def leiaInt(num):
    ok = False
    valor = 0
    while True:
        num = str(input('Digite um número: '))
        if num.isnumeric():
            valor = int(num)
            ok = True
            print(f'Você acabou de digitar o número {num}')

        else:
            print('ERRO! Digite um número inteiro válido!')
        if ok:
            break
        break
   
num = leiaInt('Digite um número: ')

leiaInt(num)   