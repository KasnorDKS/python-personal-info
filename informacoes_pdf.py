import pydf
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

pdf = pydf.generate_pdf(f'''<html>
<head>
    <meta charset="UTF-8">
</head>
<body>                      
    <h1>INFORMAÇÕES PESSOAIS</h1>
    <br>
    <p>Nome: {PESSOA.nome()}</p>
    <p>Sobrenome: {PESSOA.sobrenome()}</p>
    <p>Data de nascimento: {PESSOA.nascimento()}</p>
    <p>Risco: {PESSOA.risco()}</p>
    <p>Email: {PESSOA.email()}</p>
    <p>Telefone: {PESSOA.telefone()}</p>
    <p>CPF: {PESSOA.cpf()}</p>
    <p>RG: {PESSOA.rg()}</p>
    <p>CEP: {PESSOA.endereco()[0]}</p>
    <p>Rua: {PESSOA.endereco()[1]}</p>
    <p>Cidade: {PESSOA.endereco()[2]}</p>
    <p>Estado: {PESSOA.endereco()[3]}</p>
</body>
</html>
''')

with open('informacao pessoal.pdf', 'wb') as f:
    f.write(pdf)
    