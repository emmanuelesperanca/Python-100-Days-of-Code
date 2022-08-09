# Considerando a importação do datset como um 'conjunto_de_notas', temos:
import conjunto_de_notas
import smtplib

# Função enviar email:
def enviar_email(destino_do_email, informacao_do_email):
    my_email = 'company@email.here'
    my_password = 'company_password_here'
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email, to_addrs=destino_do_email, msg=f'{informacao_do_email}')

notas = []
notas_zeradas = 0
banco_de_dados = []
centro_de_custo = 'centro_de_custo@email.here'

# Código para inclusão no banco de dados:
for valor in conjunto_de_notas:
    notas.append(valor)
    if valor == 0:
        notas_zeradas += 1
    elif valor < 5000:
        banco_de_dados.append(valor)

# Código para enviar os emails para centro de custo:
for valor in notas:
    elif valor >= 5000:
        enviar_email(centro_de_custo, valor)

enviar_email(centro_de_custo, len(notas))
