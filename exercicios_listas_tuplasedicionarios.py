# Exercícios: Listas, Tuplas e Dicionários

# Exercício 1: ----------------------------------------------------------------------------------
'''
"Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa lista a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.'''

print('\nExercício 1 - Programa 1')
def medias_aprovados(aluno, contagem_nota):
    lista_notas = [0, 0, 0, 0] # cria (inicializa) lista para as 4 notas de cada aluno
    alunos = {} # cria dicionário com as  4 notas dos 10 alunos
    aluno = 1 # inicia (declara) variável de contagem de aluno inserido
    contagem_nota = 1 # inicia (declara) variável de contagem de nota inserida
    notas_aluno_x = list

    print(f'\nLançamento de notas do Semestre:')

    while aluno <= 10: # inicia laço para obter notas de 10 alunos.
        aluno_nota = int(input(f'\nAluno {aluno} - Insira a {contagem_nota}ª nota: \n')) # solicita inserção da primeira nota do aluno
        lista_notas.pop(contagem_nota - 1) # remove nota de índice '0', para inserir a nota informada no seu lugar [(contagem nota = 1) - 1]
        lista_notas.insert(contagem_nota - 1,aluno_nota) # insere nota digitada à lista de notas do aluno, na posição '0' [(contagem nota = 1) - 1]
        contagem_nota += 1 # incrementa a contagem de notas do aluno em +1 (2ª nota)
        for nota in range(3): # inicia o laço para solicitação das outras 3 notas a serem inseridas
            aluno_nota = int(input(f'\nAluno {aluno} - Insira a {contagem_nota}ª nota: \n')) # solicita a inserção da 2ª, 3ª e 4ª nota no looping
            lista_notas.pop(contagem_nota - 1) # remove nota de índice '1', para inserir a nota informada no seu lugar [(contagem nota = 1) += 1 - 1]
            lista_notas.insert(contagem_nota - 1,aluno_nota) # insere nota digitada à lista de notas do aluno, na posição '1' [(contagem nota = 1) += 1 - 1]. No looping, como a contagem da nota está com incremento de + 1, as próximas posições serão '2' e '3', respectivamente.
            contagem_nota += 1 # incrementa a contagem de notas do aluno em +1 (3ª nota e 4ª nota)
        else:
            notas_aluno_x = lista_notas.copy() # faz cópia da lista de notas gerada para o primeiro aluno. *A alteração de uma lista não modifica a outra.
            alunos[f'{aluno}'] = notas_aluno_x # cria primeira chave no dicionario (aluno 1) e adiciona a lista copiada com as notas do primeiro aluno. No looping, adiciona as próximas listas de notas dos demais alunos.
            contagem_nota = 1 # reinicia variável de contagem de nota para iniciar inserção das notas do aluno seguinte
            aluno += 1 # incrementa variável de contagem de aluno em + 1 ( iniciar seguinte e demais, no looping)
                       
    else:
        print(f'\nLista de Alunos e respectivas notas:\n')
        aluno = 1 # reinivia variável aluno, para utilização em contagens abaixo
        for k, v in alunos.items(): # inicia laço para printar itens na biblioteca alunos
            print(f'Aluno {aluno}: {v}') # printa os valores do dicionário alunos

        print(f'\nMédia Individual:\n')
        qtd_alunos_na_media = 0 # inicia (declara) variável para contagem de alunos com média maior que 7
        for k, v in alunos.items(): # inicia laço para calcular média de alunos e verificar quantos estão acima da média.
            nota_x = v # recupera valor referente a cada chave (aluno) no dicionário
            media_nota_x = (sum(nota_x)) / 4 # calcula média do valor recuperado
            print(f'Aluno {aluno}: {media_nota_x}')
            aluno += 1 # incrementa contagem de aluno, para fazer cálculo dos demais
            if  7.0 <= media_nota_x <= 10: # verifica se a nota é maior que 7
                qtd_alunos_na_media += 1 # incremnta ou não +1 na variável, dependendo do resultadodo if
        print(f'\n{qtd_alunos_na_media} Alunos tiveram média acima de 7,0.\n\n')

        
aluno = int
contagem_nota = int
medias_aprovados(aluno, contagem_nota)


# Exercício 2: ----------------------------------------------------------------------------------
'''
Programa nome ao contrário em maiúsculas.
Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre-se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.
'''        

print('\nExercício 2 - Programa 2')
def reverse():                                          # definindo a função
    nome_inserido = input('\nDigite o seu nome: ')      # solicita inserção do nome
    letras_do_nome = list(nome_inserido)                # coloca itens da string em uma lista
    letras_do_nome.reverse()                            # inverte ordem dos itens na lista
    nome_invertido = ''.join(letras_do_nome)            # junta itens da lisa em uma string, neste caso, sem separações, pois não é informado nenhum separador entre as ''.
    nome_invertido = nome_invertido.upper()             # converte string em maiúsculas
    print(f'\n{nome_invertido}\n')
    
reverse()


# Exercício 3: ----------------------------------------------------------------------------------
'''
Escreva um programa em Python onde todos os valores em um dicionário são emitidos (entendi como "todos os valores buscados são emitidos"). Se sim, imprima "True". Caso contrário, imprima "False".
'''

print('\nExercício 3 - Programa 3')
def dicionario():
    to_do_list = {'Pilates':'OK',                     # define dicionário
                  'Lista de Execícios':'OK',
                  'Compras':'a fazer',
                  'Inscrição':'OK'}
             
    incompleta = 'a fazer' in to_do_list.values()     # verifica se um valor específico está em alguma chave e registra como verdadeiro ou falso
    print(f'\n{incompleta}\n')                        # imprime "true" ou "false" se o item estiver ou não no dicionário 
        
dicionario()
    

# Exercício 4: ----------------------------------------------------------------------------------
'''
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são: 
"Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima". O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4, como "Cúmplice", e a 5, como "Assassino". Caso contrário,ele será classificado como "Inocente".
'''

print('\nExercício 4 - Programa 4')
def investigacao():
    questoes = ["Telefonou para a vítima?",
                "Esteve no local do crime?",
                "Mora perto da vítima?",
                "Devia para a vítima?",
                "Já trabalhou com a vítima"]
    
    pergunta_resposta = {}
    
    resp_pergunta = 0  
    indice = 0
    for resposta in range(5):
        print(f'\n{questoes[indice]}')
        respostas = input('\nResponda Sim ou Não (S ou N): \n')
        respostas = respostas.upper()
        #print(f'\n{respostas}\n')
        pergunta_resposta[questoes[indice]] = respostas
        #(f'\n{pergunta_resposta}\n')
        indice = indice + 1
        resp_pergunta + 1

    print(f'\n"Perguntas e respostas que constam na investigação do crime:')
    for k, v in pergunta_resposta.items():
        print(f'{k, v}') 

    resp = list(pergunta_resposta.values())
    contagem_resp = resp.count('S')
    #print(f'\n{resp}\n')
    #print(f'\n{contagem_resp}\n') 
       
    print(f'\nCom base em suas respostas o(a) invetigado(a) foi considerado(a):\n')    
    if contagem_resp == 2:
        print(f'\nSuspeito(a)\n')
    elif 3 <= contagem_resp <= 4:
        print(f'\nCúmplice\n')
    elif contagem_resp == 5:   
        print(f'\nAssassino(a)\n')
    else:
        print(f'\nInocente\n')

        
investigacao()