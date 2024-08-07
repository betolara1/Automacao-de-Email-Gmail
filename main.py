import smtplib
import email.message

lista = []
with open("email.txt", "r") as arquivo:
    for arq in arquivo:
        lista.append(arq.splitlines())


def enviar_email(remetente):  
    # AQUI VAI O CORPO DO E-MAIL
    corpo_email = """
    <p>Bom dia</p>
    <p>Venha aprender a mandar e-mail automatico</p>
    """

    msg = email.message.Message()
    msg['Subject'] = '' # ASSUNTO DA MENSAGEM
    msg['From'] = '' # SEU E-MAIL
    msg['To'] = remetente # E-MAIL DO DESTINATARIO
    password = '' # SUA SENHA GERADO PELA API DO GOOGLE
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

# LOOP QUE PEGA OS EMAIL DA LISTA PRA ENVIAR
for l in lista:
    lista_convertida = str(l).replace('[', '').replace(']', '').replace("'", '') #BUGIGANGA PARA CONSEGUIR ENVIAR O EMAIL DE MANEIRA CERTA
    enviar_email(lista_convertida) #FUNÇÃO QUE RETORNA OS EMAIL ENVIADOS