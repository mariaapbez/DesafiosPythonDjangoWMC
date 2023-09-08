# Exercícios: Exercícios Banco de Dados

import sqlite3

conexao = sqlite3.connect('banco_exercicios_bd') # os comandos commit e close estão no final do arquivo
cursor = conexao.cursor()

# Exercício 1: ----------------------------------------------------------------------------------
'''
Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).
'''

def exercicio_1():
    print('\nExercício 1')
    cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')

# Exercício 2: ----------------------------------------------------------------------------------
'''
Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
'''

def exercicio_2():
    print('\nExercício 2')
    cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (1, "Carlos Figueiredo", 34, "Matemática")')
    cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (2, "Alessandra Santos", 29, "Química")')
    cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (3, "Vanessa Almeida", 40, "Letras")')
    cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (4, "Fernando Mendes", 27, "História")')
    cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (5, "Beatriz Silva", 20, "Educação Física")')
    cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (6, "John Fernandes", 19, "Engenharia")')
    cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (7, "Fernanda Mesquita", 21, "Engenharia")')
    cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (8, "Kellen Mariano", 25, "Letras")')


# Exercício 3: ----------------------------------------------------------------------------------
'''
Consultas Básicas - Escreva consultas SQL para realizar as seguintes tarefas:
a) Selecionar todos os registros da tabela "alunos".
b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
d) Contar o número total de alunos na tabela.
'''

def exercicio_3():
    print('\nExercício 3')
    print('a)')
    consultas = cursor.execute('SELECT * FROM alunos')
    for alunos in consultas:
        print(alunos)
    print()

    print('b)')
    consultas = cursor.execute('SELECT nome,idade FROM alunos WHERE idade > 20')
    for alunos in consultas:
        print(alunos)
    print()

    print('c)')
    consultas = cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome')
    for alunos in consultas:
        print(alunos)
    print()

    #ou

    consultas = cursor.execute('SELECT * FROM alunos GROUP BY nome HAVING curso = "Engenharia" ORDER BY nome')
    for alunos in consultas:
        print(alunos)
    print()


    print('d)')
    consultas = cursor.execute('SELECT COUNT(*) FROM alunos')
    for alunos in consultas:
        print(alunos)
    print()


# Exercício 4: ----------------------------------------------------------------------------------
'''
Atualização e Remoção:
a) Atualize a idade de um aluno específico na tabela.
b) Remova um aluno pelo seu ID.
'''

def exercicio_4():
    print('\nExercício 4')
    #a)
    cursor.execute('UPDATE alunos SET idade = 28 WHERE nome = "Alessandra Santos"')

    #b)
    cursor.execute('DELETE FROM alunos WHERE id = 4')


# Exercício 5: ----------------------------------------------------------------------------------
'''
Criar uma Tabela e Inserir Dados:
Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.
'''

def exercicio_5():
    print('\nExercício 5')
    cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT)')

    cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (1, "Maria Sousa", 29, 2650)')
    cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (2, "Paula Fernandes", 35, 1700)')
    cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (3, "João Mariano", 22, 980)')
    cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (4, "Marlene Silva", 42, 3250)')
    cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (5, "Jussara Freire", 25, 1380)')
    cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (6, "Nayara Francisco", 19, 650)')
    cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (7, "Mariana Felício", 40, 1650)')


# Exercício 6: ----------------------------------------------------------------------------------
'''
Consultas e Funções Agregadas - Escreva consultas SQL para realizar as seguintes tarefas:
a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
b) Calcule o saldo médio dos clientes.
c) Encontre o cliente com o saldo máximo.
d) Conte quantos clientes têm saldo acima de 1000.
'''

def exercicio_6():
    print('\nExercício 6')
    print('a)')
    consultas = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
    for clientes in consultas:
        print(clientes)
    print()

    print('b)')
    consultas = cursor.execute('SELECT AVG(saldo) AS saldo_medio FROM clientes')
    for clientes in consultas:
        print(f'{clientes}')
    print()

    print('c)')
    consultas = cursor.execute('SELECT nome FROM clientes WHERE saldo = (SELECT MAX(saldo) AS maior_saldo FROM clientes)')
    for clientes in consultas:
        print(clientes)
    print()

    print('d)')
    consultas = cursor.execute('SELECT COUNT(saldo) AS saldo_mil_acima FROM clientes WHERE saldo > 1000')
    for clientes in consultas:
        print(clientes)
    print()

# Exercício 7: ----------------------------------------------------------------------------------
'''
Atualização e Remoção com Condições:
a) Atualize o saldo de um cliente específico.
b) Remova um cliente pelo seu ID. 
'''

def exercicio_7():
    print('\nExercício 7')
    #a)
    cursor.execute('UPDATE clientes SET saldo = 950 WHERE nome = "Nayara Francisco"')

    #b)
    cursor.execute('DELETE FROM clientes WHERE id = 2')

# Exercício 8: ----------------------------------------------------------------------------------
'''
Junção de Tabelas - Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando  o id da tabela "clientes"), produto (texto) e valor (real). Insira algumas compras associadas a clientes existentes na tabela "clientes". Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.
'''

def exercicio_8():
    print('\nExercício 8')
    cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(100), valor FLOAT, CONSTRAINT fk_clientes FOREIGN KEY (cliente_id) REFERENCES clientes (id))')

    cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (1, 4, "Fogão", 1348)')

    cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (2, 6, "Ferro de Passar", 135)')

    cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (3, 1, "Fritadeira Elétrica", 860)')

    cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (4, 3, "Celular", 700)')

    cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (5, 5, "Ventilador", 350)')


    consultas =  cursor.execute('SELECT nome, produto, valor FROM compras LEFT JOIN clientes ON compras.cliente_id = clientes.id') # retorna os dados nas colunas produto e valor da tabela da esquerda (compras, citada primeiro no código) e da tabela da direita (clientes) os dados na coluna nome que tenham id correspondente ao id do cliente (cliente_id) na tabela compras. Os dados que não tem correspondência na tabela da direita aparecem como none.
    for compras in consultas:
        print(compras)
    print()

#------------------------------------------------------------------------------------------------------------------------------

#exercicio_1()
#exercicio_2()
#exercicio_3()
#exercicio_4()
#exercicio_5()
#exercicio_6()
#exercicio_7()
#exercicio_8()

conexao.commit()
conexao.close