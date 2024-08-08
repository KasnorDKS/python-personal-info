import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from informacoes import Pessoa

PESSOA = Pessoa('pedro', # Nome (nome())
                'silva', # Sobrenome (sobrenome())
                '21/7/2001', # Data de nascimento (nascimento()) (calcular_idade())
                'usuariopedro7@gmail.com', # Email (email())
                '+55 (00) 91234-5678', # Telefone (telefone())
                '123.456.789.10', # CPF (cpf())
                '1234567', # RG (rg())
                '05424020', # Cep (endereco())
                )

msg = MIMEMultipart()
msg['Subject'] = f'Informações Pessoais de {PESSOA.nome()} {PESSOA.sobrenome()}'
body = f'''Prezado(a) {PESSOA.nome()} {PESSOA.sobrenome()}, estou entrando em contato para lhe enviar \
    um arquivo pdf com suas principais informações pessoais.\n
    Segue o anexo para obter os resultados.
    \n\n-Teste'''

msg['From'] = 'remetente@gmail.com'
msg['To'] = PESSOA.email()
password = 'password'

msg.attach(MIMEText(body, 'plain'))

filename = 'informacao pessoal.pdf'

attachment = open('informacao pessoal.pdf','rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', f"attachment; filename={filename}")

msg.attach(part)

attachment.close()

context = ssl.create_default_context()

with smtplib.SMTP('smtp.gmail.com', 587) as conexao:
    conexao.starttls(context = context)
    conexao.login(msg['From'], password)
    conexao.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))

