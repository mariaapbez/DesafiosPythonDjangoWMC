# Exercícios: Listas, Tuplas e Dicionários

# Exercício 1: ----------------------------------------------------------------------------------
'''
"Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa lista a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.'''

print('\nExercício 1 - Programa 1')
def medias_aprovados():
    lista_notas_1 = []
    lista_notas_2 = []
    lista_notas_3 = []
    lista_notas_4 = []
    lista_notas_5 = []
    lista_notas_6 = []
    lista_notas_7 = []
    lista_notas_8 = []
    lista_notas_9 = []
    lista_notas_10 = []

    aluno_1 = int(input('\nAluno 1 - Insira uma nota: \n'))
    lista_notas_1.append(aluno_1)

    for nota in range(3):
        int(input('\nAluno 1 - Insira uma nota: \n'))
        lista_notas_1.append(aluno_1)

    else:
        aluno_2 = int(input('\nAluno 2 - Insira uma nota: \n'))
        lista_notas_2.append(aluno_2)

    for nota in range(3):
        int(input('\nAluno 2 - Insira uma nota: \n'))
        lista_notas_2.append(aluno_2)

    else:
        aluno_3 = int(input('\nAluno 3 - Insira uma nota: \n'))
        lista_notas_3.append(aluno_3)

    for nota in range(3):
        int(input('\nAluno 3 - Insira uma nota: \n'))
        lista_notas_3.append(aluno_3)

    else:
        aluno_4 = int(input('\nAluno 4 - Insira uma nota: \n'))
        lista_notas_4.append(aluno_4)

    for nota in range(3):
        int(input('\nAluno 4 - Insira uma nota: \n'))
        lista_notas_4.append(aluno_4)

    else:
        aluno_5 = int(input('\nAluno 5 - Insira uma nota: \n'))
        lista_notas_5.append(aluno_5)

    for nota in range(3):
        int(input('\nAluno 5 - Insira uma nota: \n'))
        lista_notas_5.append(aluno_5)

    else:
        aluno_6 = int(input('\nAluno 6 - Insira uma nota: \n'))
        lista_notas_6.append(aluno_6)

    for nota in range(3):
        int(input('\nAluno 6 - Insira uma nota: \n'))
        lista_notas_6.append(aluno_6)

    else:
        aluno_7 = int(input('\nAluno 7 - Insira uma nota: \n'))
        lista_notas_7.append(aluno_7)

    for nota in range(3):
        int(input('\nAluno 7 - Insira uma nota: \n'))
        lista_notas_7.append(aluno_7)

    else:
        aluno_8 = int(input('\nAluno 8 - Insira uma nota: \n'))
        lista_notas_8.append(aluno_8)

    for nota in range(3):
        int(input('\nAluno 8 - Insira uma nota: \n'))
        lista_notas_8.append(aluno_8)

    else:
        aluno_9 = int(input('\nAluno 9 - Insira uma nota: \n'))
        lista_notas_9.append(aluno_9)

    for nota in range(3):
        int(input('\nAluno 9 - Insira uma nota: \n'))
        lista_notas_9.append(aluno_9)

    else:
        aluno_10 = int(input('\nAluno 10 - Insira uma nota: \n'))
        lista_notas_10.append(aluno_10)

    for nota in range(3):
        int(input('\nAluno 10 - Insira uma nota: \n'))
        lista_notas_10.append(aluno_10)

    else:
        media_1 = sum(lista_notas_1)/4
        media_2 = sum(lista_notas_2)/4
        media_3 = sum(lista_notas_3)/4
        media_4 = sum(lista_notas_4)/4
        media_5 = sum(lista_notas_5)/4
        media_6 = sum(lista_notas_6)/4
        media_7 = sum(lista_notas_7)/4
        media_8 = sum(lista_notas_8)/4
        media_9 = sum(lista_notas_9)/4
        media_10 = sum(lista_notas_10)/4

        lista_media_alunos = [media_1, media_2,media_3,media_4,media_5,media_6, media_7,media_8,media_9,media_10]
        
        qtd_alunos_na_media = 0
        for media in lista_media_alunos:
            if 7.0 <= media <=10:
                qtd_alunos_na_media += 1

        print(f'\n{qtd_alunos_na_media} alunos tiveram média acima de 7,0.\n\n')

medias_aprovados()


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