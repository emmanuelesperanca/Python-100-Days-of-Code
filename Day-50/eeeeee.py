import random
count = 0
Lista1 = []
Lista2 = []

while count < 1000:
    numero_sorteado = random.randint(1, 10)
    if numero_sorteado > 5:
        Lista1.append(numero_sorteado)
    else:
        Lista2.append(numero_sorteado)
    count = count + 1

print(Lista1, Lista2, len(Lista1), len(Lista2))
