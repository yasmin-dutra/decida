import random
from time import sleep


def converte_em_lista(arquivo, lista):
    with open(arquivo, 'r', encoding='UTF8') as texto:
        for linha in texto:
            lista.append(str(linha).replace('\n', ''))
        return lista
        # print(lista)


frases = []

frases = converte_em_lista('ditados.txt', frases)

# Inicio do programa
print('Olá, qual é o seu nome?')
sleep(1)
player = input('Seu nome: ')
sleep(2)
print(f'Prazer em te conhecer { player } ')
sleep(1)
print(f'Sou o Guru Pythonico, me faça uma pergunta e te darei a resposta mais sabia!')
jogar = True
perguntas = []
while jogar == True:
    print(f'Quer fazer uma pergunta {player}?')
    sleep(2)
    print('Sim (1)')
    print('Não (2)')
    try:
        resposta = int(input('Sua resposta: '))
        sleep(1)
        if resposta == 1:
            print('Ok, então faça sua pergunta')
            sleep(3)
            pergunta = input('Sua pergunta: ')
            if pergunta not in perguntas:
                perguntas.append(pergunta)
                sleep(2)
                print('Hummm...')
                for i in range(5):
                    print('...')
                    sleep(1)
                resposta = frases[random.randint(0, len(frases))]
                print(resposta)
                sleep(5)
        elif resposta == 2:
            jogar = False
            print(f'Ok, até a próxima { player }!')
    except:
        print('Resposta invalida, tente de novo')