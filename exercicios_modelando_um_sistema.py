# Exercícios: Exercício Modelando um Sistema

# Exercício 2: ----------------------------------------------------------------------------------

'''
O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres.
Modele um sistema orientado a objetos para representar contas correntes do Banco Delas seguindo os requisitos abaixo.

1. Cada 'conta corrente' pode ter um ou mais 'clientes' como titular.
2. O banco controla apenas o nome, o telefone e a renda mensal de cada cliente. (PROTEGIDOS)
3. A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos. Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela fizer um depósito, aumentaremos o saldo.
4. Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda
mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até -renda_mensal.
5. Clientes homens por enquanto não têm direito a cheque especial.

Para modelar seu sistema, utilize obrigatoriamente os conceitos "classe", "herança", "propriedades", "encapsulamento" e "classe abstrata".
'''
from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self, nome, telefone: float, renda: float):
        self._nome = nome
        self._telefone = telefone
        self.__renda = renda

    @property
    def nome(self):
            print('getter de nome')
            return self._nome
    @nome.setter
    def nome(self, novo_nome):
            print('setter de nome')
            if type(novo_nome) != str:
                raise TypeError('O nome deve conter apenas letras')
            self._nome = novo_nome

    @property
    def telefone(self):
            print('getter de telefone')
            return self._telefone
    @telefone.setter
    def telefone(self, novo_telefone:float):
            print('setter de telefone')
            if not novo_telefone.is_integer():
                raise TypeError('Digitar apenas números!')
            self._telefone = novo_telefone

    @property
    def renda(self):
            print('getter de nome')
            return self.__renda

    abstractmethod    
    def cheque_especial(self):
        pass

class ClienteMulher(Cliente):
    def __init__(self, nome, telefone, renda):
            super().__init__(nome, telefone, renda)

    def cheque_especial(self):
        return True
    
    def __str__(self):
        cheque = "Disponível" if self.cheque_especial == True else "Indisponível"
        return f'Cheque Especial está {cheque}.'
    
class ClienteHomem(Cliente):
    def __init__(self, nome, telefone, renda):
            super().__init__(nome, telefone, renda)

    def cheque_especial(self):
        return False
    
    
                  
class Conta(Cliente):
    def __init__(self, titular):
            self.__saldo = 0.0
            self.__operacoes = []
            self.__titulares = [1]
            self.titular = 1
            self.add_titular(titular)
            self.__renda = 0
            
    def __str__(self):
        cheque = "Disponível" if self.cheque_especial == True else "Indisponível"
        return f'Cheque Especial está {cheque}.'

    def add_titular(self, titular):
            self.titular += 1
            self.__titulares.append(titular)

    def sacar(self, valor_operacao: float, renda):
        if self.cheque_especial == True:
            if valor_operacao > (self.__saldo + self.__renda):
                raise ValueError (f'Saldo insuficiente. O Valor excede o seu cheque especial.\n Saldo atual: R${self.__saldo}')
            else:
                self.__saldo -= valor_operacao
                self.__operacoes.append(f'-R${valor_operacao}')
        else:
            if valor_operacao > self.__saldo:
                raise ValueError (f'Saldo insuficiente. O saldo atual é de {self.__saldo}')
            else:
                self.__saldo -= float(valor_operacao)
                self.__operacoes.append(f'-R${valor_operacao}')


    def depositar(self, valor_operacao: float):
        self.__saldo += (valor_operacao)
        self.__operacoes.append(f'+R${valor_operacao:.2f}')

    @property
    def saldo(self):
         return self.__saldo
    
    @property
    def operacoes(self):
         return self.__operacoes
    
    @property
    def titulares(self):
         return self.__titulares


            
conta_mulher = ClienteMulher('Maria', '(88)98989-8989', '2500.00')
conta_homem = ClienteHomem('João', '(5)56767-6767', '2100.00')

conta_1 = Conta(conta_mulher)
conta_2 = Conta(conta_homem)



print(conta_1.saldo)
print(conta_1.chequ)
print(conta_2.saldo)
print(conta_2.cheque_especial)
print()

conta_1.depositar(5000.0)
conta_2.depositar(50.0)

print(conta_1.saldo)
print(conta_2.saldo)
print()

valor_saque = input('Quanto você deseja sacar? ')
valor_saque = float(valor_saque)

try:
    conta_1.sacar(valor_saque)
    conta_2.sacar(valor_saque)
except:
    ValueError

print(conta_1.saldo)
print(conta_2.saldo)
print()

print(conta_1.operacoes)
print(conta_2.operacoes)
print()