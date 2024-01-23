"""
SMTP - Simple Mail Transfer Protocol
Servidor/Protocolo padrão usado para transferência de emails entre dois dispositvos
SMTP É UM CONTEXT MANAGER DE SERVIDOR!


Obs: O encaminhamento IMAP tem que estar ativo, e verificação em duas etapas ativas

1 - Definir remetente e destino


2 - Configurar servidor smtp:
    server = 'smtp.gmail.com'
    port = 587
    user = email_remetente
    passwd = senha_app

    from_email = remetente
    email_password = senha_app

3 - Definir mensagem email a ser transferida(A msg tem que estar em html)

4 - Montar extrutura mimemultipart:
    obj =  mimemultipart()
    obj['from'] = rem
    obj['to'] = destin
    obj['subject'] =  assunto

    corpo = mimetext(filehtml, format(html), enconding)
    obj.attach(corpo)

5 - Abrir servidor com context manager SMTP(server, port) as server:
    server.ehlo() - Inicia conexão com server
    server.starttls - Inicia conexão segura com servidor
    server.login(user, senha)
    server.sendmessage(objmultimimepart)

email.mime.multipart.MIMEMultipart - É responsável por definir from, to, subject, e fazer um attach no assunto email html
email.mime.text.MIMEText(arquivo, format(html), encoding) - É responsável por criar o assunto email html]

Algoritmo receita de bola, assim como o algoritmo do cpf

smtplib.SMTP(HOST, PORT) - Cria context manager para servidor smtp
email.mime.multipart.MIMEMultipart - Cria objeto mime para definir from, to, subject, e attach no assunto

"""
from dotenv import load_dotenv
import os, datetime, pathlib, string, random, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

data=  datetime.datetime.now().strftime('%d/%m/%Y')
waymail = pathlib.Path(__file__).parent / 'email.html'
load_dotenv()

remetente_email = os.getenv('FROM_EMAIL')
destinatario = remetente_email

smtp_server = os.getenv('HOST')
smtp_port = os.getenv('PORT')
smtp_user = os.getenv('FROM_EMAIL')
passwd = os.getenv('EMAIL_PASSWORD')


with open(waymail, 'r', encoding='utf8') as mailfile:
    conteudo = mailfile.read()
    objmail = string.Template(conteudo)
    email_content = objmail.substitute({"nome": 'Tulio', "valor": f'R${random.randint(1, 50):.2f}'.replace('.',','), 'data': data, 'empresa': 'Coca-Cola', 'telefone': '(34)99668-5165'})


#Montar extrutura do email com mimemultipart e mime text
email = MIMEMultipart()
email["from"] = remetente_email
email["to"] = destinatario
email["subject"] = "Prosposta via Python"
corpo = MIMEText(email_content, 'html', 'utf-8')
email.attach(corpo)

#Abrir server smtp
servidor = smtplib.SMTP(smtp_server, smtp_port)

with servidor as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_user, passwd)
    server.send_message(email)
    print('Email enviado com sucesso')