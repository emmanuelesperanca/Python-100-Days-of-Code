import random

intervalo = []
intervalo.append(int(input('Escolha o primeiro número do intervalo: ')))
intervalo.append(int(input('Escolha o segundo número do intervalo: ')))
intervalo.sort()

numero_sorteado = random.randint(intervalo[0], intervalo[1] + 1)

fim_jogo = False
tentativas = 0

def checagem(numero_jogador):
    if numero_jogador < numero_sorteado:
        print('Baixo demais!')
    elif numero_jogador > numero_sorteado:
        print('Alto demais!')
    else:
        return 0


while not fim_jogo:
    numero_escolhido = int(input('Escolha um número: '))
    tentativas += 1
    if checagem(numero_escolhido) == 0:
        print(f'Parabéns! Você acertou! Em {tentativas} tentativas.')
        fim_jogo = True
