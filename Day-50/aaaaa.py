
valor_para_sacar = int(input("Digite o valor que deseja sacar: "))

while (valor_para_sacar % 5) != 0:
    valor_para_sacar = int(input("Valor Inválido, por favor digite um valor que termine em 0 ou 5. Tente novamente: "))
resposta = []

while valor_para_sacar - 50 >= 0:
    valor_para_sacar -= 50
    resposta.append(50)

while valor_para_sacar - 20 >= 0:
    valor_para_sacar -= 20
    resposta.append(20)

while valor_para_sacar - 5 >= 0:
    valor_para_sacar -= 5
    resposta.append(5)

notas_de_50 = resposta.count(50)
notas_de_20 = resposta.count(20)
notas_de_5 = resposta.count(5)

print(f'Você recebeu {notas_de_50} nota(s) de 50, {notas_de_20} nota(s) de 20 e {notas_de_5} nota(s) de 5,')
