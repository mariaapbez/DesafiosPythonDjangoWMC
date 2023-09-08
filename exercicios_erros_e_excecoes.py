# Exercícios: Exercício Erros e Exceções

# Exercício 1: ----------------------------------------------------------------------------------

'''
O programa abaixo deve calcular a média dos valores digitados pelo usuário.
No entanto, ele não está funcionando bem. Você pode consertá-lo?
'''

def calcular_media(valores, media):
    tamanho = 1
    soma = 0.0
    
    for i, valor in enumerate(valores):
        soma += (valor)
        i += 1
        tamanho = i
    media = soma / tamanho
    return media
    

continuar = True
valores = []
while continuar == True:
    valor = (input('Digite um número para entrar na sua média ou "ok" para calcular o valor:'))
    if valor.lower() == 'ok':
        continuar = False
    else:
        valores.append(float(valor)) 
        
media = 0
media_calc = calcular_media(valores, media)
print('\nA média calculada para os valores {} foi de {:.1f}.\n'.format(valores, media_calc))