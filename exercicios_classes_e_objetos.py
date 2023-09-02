# Exercícios: Exercícios Classes e Objetos

# Exercício 1: ----------------------------------------------------------------------------------

'''
Crie uma classe que modele o objeto "carro".
Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.
Crie uma instância da classe carro.
Faça o carro "andar" utilizando os métodos da sua classe.
Faça o carro "parar" utilizando os métodos da sua classe.
'''

class Carro():
    def __init__(self):
        self.ligado = False
        self.cor = 'prata'
        self.modelo = '2005'
        self.velocidade = 0
        self.velocidade_min = 0
        self.velocidade_max = 140

    def ligar(self):
        
        self.ligado = True

    def deligar(self):
        self.ligado = False
    
    def acelerar(self):
        if not self.ligado:
            return
        if self.velocidade < self.velocidade_max - 5:
            self.velocidade += 5
        
    def desacelerar(self):
        if not self.ligado:
            return
        if self.velocidade > self.velocidade_min + 5:
            self.velocidade -= 5
    
    
meu_carro = Carro()
meu_carro.ligar()
print(meu_carro.ligado)
while meu_carro.velocidade < meu_carro.velocidade_max - 5:
    meu_carro.acelerar()
    print(meu_carro.velocidade)
else:
    if ValueError:
        print('Velocidade máxima atingida')
        print(meu_carro.velocidade)
    while meu_carro.velocidade > meu_carro.velocidade_min + 5:    
        meu_carro.desacelerar()
        print(meu_carro.velocidade)
    else:
        if ValueError:
            print('Parada')
        print(meu_carro.velocidade)
    meu_carro.deligar()
    print(meu_carro.ligado)

