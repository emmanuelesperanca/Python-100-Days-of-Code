adesivos = int(input('Insira a quantidade de adesivos disponíveis: '))

caixas = []

while adesivos != 0:
    numero_de_casas = int(len(str(adesivos)))
    adesivos -= numero_de_casas
    caixas.append(1)

print(f'Pode-se numerar {sum(caixas)} caixas.')
