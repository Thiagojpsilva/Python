# Enviando E-mails SMTP com Python
import os
import pathlib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template

from dotenv import load_dotenv  # type: ignore

load_dotenv()

# Caminho arquivo HTML
CAMINHO_HTML = pathlib.Path(__file__).parent / 'template_email.html'

# Dados do remetente e destinatário
remetente = os.getenv('FROM_EMAIL', '')
destinatario = remetente

# Configurações SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

# Mensagem de texto
# Tem que abrir o arquivo com Enconding correto.
with open(CAMINHO_HTML, 'r', encoding='utf-8') as arquivo:
    texto_arquivo = arquivo.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome='Thiago')
#    texto_email = texto_email.encode('utf-8')
#    msg = texto_email.encode('utf-8')

# Transformar nossa mensagem em MIMEMultipart
msg = MIMEMultipart()
msg['from'] = remetente
msg['to'] = destinatario
msg['subject'] = 'Este é o assunto do e-mail'
# msg['Content-Type'] = 'text/html; charset=utf-8'


corpo_email = MIMEText(texto_email, 'html', 'utf-8')
msg.attach(corpo_email)

# Envia o e-mail
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(msg)
    print('E-mail enviado com  sucesso!')
