import pymysql.cursors
from informacoes import Pessoa

def conecta():
    conexao = pymysql.connect(
        host='localhost',
        user='root',
        password='password',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return conexao

PESSOA = Pessoa('pedro', # Nome (nome())
                'silva', # Sobrenome (sobrenome())
                '21/7/2001', # Data de nascimento (nascimento()) (calcular_idade())
                'usuariopedro7@gmail.com', # Email (email())
                '+55 (00) 91234-5678', # Telefone (telefone())
                '123.456.789.10', # CPF (cpf())
                '1234567', # RG (rg())
                '05424020', # Cep (endereco())
                )

nome = PESSOA.nome()
sobrenome = PESSOA.sobrenome()
email = PESSOA.email()
cpf = PESSOA.cpf()
rg = PESSOA.rg()
telefone = PESSOA.telefone()
nascimento = PESSOA.nascimento()
risco = PESSOA.risco()
cep = PESSOA.endereco()[0]
rua = PESSOA.endereco()[1]
cidade = PESSOA.endereco()[2]
estado = PESSOA.endereco()[3]

usuario = 'user'
usuario = usuario.lower()
senha = 'password'

EMAILS = ['@gmail.com', '@outlook.com', '@hotmail.com', '@yahoo.com']

banco_dados = 'pessoas'
tabela = 'clientes'
tabela2 = 'contas'

class BDSQL():

    # Criação do banco de dados
    def criarDB():
        conexao = conecta()
        try:
            with conexao.cursor() as cursor:
                cursor.execute(f'CREATE DATABASE IF NOT EXISTS {banco_dados}')
                print('Banco de dados criado com sucesso')
        finally:
            conexao.close()
            print('Conexão encerrada.')
            
    # Criação das tabelas
    def criarTBL():
        conexao = conecta()
        try:
            with conexao.cursor() as cursor:
                # Seleciona o banco de dados
                cursor.execute(f'USE {banco_dados}')
                
                # Cria uma tabela com suas colunas no bando de dados selecionado
                cursor.execute(f'''CREATE TABLE IF NOT EXISTS {tabela}(
                        id_user INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
                        nome VARCHAR(255) NOT NULL, 
                        sobrenome VARCHAR(255) NOT NULL, 
                        data_nasc VARCHAR(86) NOT NULL,
                        email VARCHAR(86) NOT NULL,
                        telefone VARCHAR(86) NOT NULL,
                        cpf VARCHAR(86) NOT NULL,
                        rg VARCHAR(86) NOT NULL,
                        gp_risco VARCHAR(16) NOT NULL,
                        cep VARCHAR(64) NOT NULL,
                        rua VARCHAR(128) NOT NULL,
                        cidade VARCHAR(86) NOT NULL,
                        estado VARCHAR(64) NOT NULL,
                        INDEX idx_{tabela} (id_user, nome, email, telefone)
                    );''')
                conexao.commit()
            print(f'\nTabela {tabela} criada com sucesso!')
            
            with conexao.cursor() as cursor:
                # Cria uma segunda tabela no bando de dados selecionado
                # Algumas colunas da tabela2 deverão ser iguais aos da tabela1
                cursor.execute(f'''CREATE TABLE IF NOT EXISTS {tabela2}(
                id_user INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                email VARCHAR(86) NOT NULL,
                telefone VARCHAR(86) NOT NULL,
                usuario VARCHAR(255) NOT NULL,
                senha VARCHAR(64) NOT NULL,
                FOREIGN KEY(id_user, nome, email, telefone) 
                REFERENCES {tabela}(id_user, nome, email, telefone)
                )''')
                conexao.commit()
            print(f'Tabela {tabela2} criada com sucesso!')

        finally:
            # Finaliza a conexão com o banco de dados
            conexao.close()
            print('Conexão encerrada.')
            
    # Inserção de dados nas tabelas 1 e 2
    def inserirTBL():
        conexao = conecta()
        try:
            with conexao.cursor() as cursor:
                # Seleciona o banco de dados
                cursor.execute(f'USE {banco_dados}')
                
                # Verifica se há algum cpf, rg ou email igual ao que o usuário vai colocar
                cursor.execute(f'SELECT cpf, rg, email FROM {tabela}')
                registros_existentes = cursor.fetchall()
                novo_cpf = cpf
                novo_rg = rg
                novo_email = email
                
                for registro in registros_existentes:
                    if novo_cpf == registro['cpf']:
                        print("\nERRO: CPF duplicado encontrado.")
                        return
                    if novo_rg == registro['rg']:
                        print("\nERRO: RG duplicado encontrado.")
                        return
                    if novo_email == registro['email']:
                        print('\nERRO: Este email já foi cadastrado.')
                        return
                    
                # Irá verificar se já tem algum usuário com o mesmo nome escolhido pelo usuário
                cursor.execute(f'SELECT usuario FROM {tabela2}')
                usuarios_existentes = cursor.fetchall()
                novo_usuario = usuario
                
                for usuarios in usuarios_existentes:
                    if novo_usuario == usuarios['usuario']:
                        print("\nERRO: Usuário já em uso.")
                        return
                    
                # Irá inserir informações na tabela1
                cursor.execute(f'''INSERT INTO {tabela}
                            (nome, sobrenome, email, cpf, rg, telefone, 
                            data_nasc, gp_risco, cep, rua, cidade, estado)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                            (nome, sobrenome, email, cpf, rg, telefone, \
                                nascimento, risco, cep, rua, cidade, estado))
                conexao.commit()
                # Irá inserir informações na tabela2
                cursor.execute(f'''INSERT INTO {tabela2}
                            (usuario, nome, senha, email, telefone)
                            VALUES (%s, %s, %s, %s, %s)''',
                            (usuario, nome, senha, email, telefone))
                conexao.commit()
            print('\nInserção realizada com sucesso!')
        finally:
            conexao.close()
            print('Encerrado.')
            
    # Cria uma View no banco de dados para utilizar depois
    def view(view):
        conexao = conecta()
        try:
            with conexao.cursor() as cursor:
                # Seleciona o banco de dados
                cursor.execute(f'USE {banco_dados}')
                # Query para criar a View
                cursor.execute(f'''CREATE VIEW {view.lower()} AS 
                                SELECT
                                    {tabela}.id_user,
                                    {tabela}.nome,
                                    {tabela}.sobrenome,
                                    {tabela}.data_nasc,
                                    {tabela}.gp_risco,
                                    {tabela}.email,
                                    {tabela}.telefone,
                                    {tabela}.cpf,
                                    {tabela}.rg,
                                    {tabela}.cep,
                                    {tabela}.rua,
                                    {tabela}.cidade,
                                    {tabela}.estado,
                                    {tabela2}.usuario,
                                    {tabela2}.senha
                                FROM {tabela}
                                JOIN {tabela2} ON {tabela}.id_user = {tabela2}.id_user''')
                conexao.commit()
            print(f"Visualização criada como {view}.")
        finally:
            conexao.close()
            print('Encerrado.')
            
    # Mostra todas as informações relevantes da tabela1 e tabela2
    def mostrar():
        conexao = conecta()
        try:
            with conexao.cursor() as cursor:
                cursor.execute(f'USE {banco_dados}')
                # Irá selecionar todas as informações da tabela1 e da tabela2
                cursor.execute(f'SELECT * FROM {tabela}, {tabela2}')
                resultados = cursor.fetchall()
                # Irá mostrar informações da tabela1 e da tabela2 
                for dados in resultados:
                    print('ID:', dados['id_user'], \
                        '\nNome:', dados['nome'], dados['sobrenome'], \
                        '\nData de Nascimento:', dados['data_nasc'], \
                        '\nGrupo de Risco:', dados['gp_risco'], \
                        '\nEmail:', dados['email'], \
                        '\nTelefone:', dados['telefone'], \
                        '\nCPF:', dados['cpf'], \
                        '\nRG:', dados['rg'], \
                        '\nCEP:', dados['cep'], \
                        '\nRua:', dados['rua'], \
                        '\nCidade:', dados['cidade'], \
                        '\nEstado:', dados['estado'], \
                        '\nUsuário:', dados['usuario'], \
                        '\nSenha:', dados['senha'],\
                        '\n')
                
        finally:
            conexao.close()
            print('Consulta encerrada.')
            
    # Faz uma verificação caso o usuário e senha se correspondam
    def verificacao(user, senha):
        login = False
        conexao = conecta()
        try:
            with conexao.cursor() as cursor:
                cursor.execute(f'USE {banco_dados}')
                if any(EMAILS) in user:
                    cursor.execute(f"""SELECT usuario, senha FROM {tabela2} 
                                WHERE email = '{user}';""")
                else:
                    cursor.execute(f"""SELECT usuario, senha FROM {tabela2} 
                                    WHERE usuario = '{user}';""")
                    
                resultados = cursor.fetchall()

                for dados in resultados:
                    if senha == dados['senha']:
                        login = True
                        print("Login bem-sucedido.")
                        return login
                    else:
                        print("Usuário ou senha inválidos, por favor tente novamente.")
                        return login
                    
        finally:
            conexao.close()

if __name__ == '__main__':
    
    BDSQL.criarDB() # Cria o banco de dados
    BDSQL.criarTBL() # Cria as tabelas predefinidas
    
    # Mostra as informações declaradas no início do código
    print(f'''\nInformações para inserir:
Nome: {nome}
Sobrenome: {sobrenome}
Nascimento: {nascimento}
Risco: {risco}
Email: {email}
Telefone: {telefone}
CPF: {cpf}
RG: {rg}
CEP: {cep}
Rua: {rua}
Cidade: {cidade}
Estado: {estado}
Nome de usuário: {usuario}
Senha: {senha}''')
    
    # Inserir as informações acima na tabela
    user = input(f'\nGostaria de inserir as informações nas tabelas {tabela} e {tabela2}? [Y/N] ')
    if user.upper() == "Y":
        BDSQL.inserirTBL()
    else:
        print(f"\nNão foi inserida nenhuma informação nas tabelas {tabela} e {tabela2}.")
    
    # Criar uma view
    user = input(f'\nGostaria de criar uma visualização juntando todas as informações da tabela 1 e 2? [Y/N] ')
    if user.upper() == "Y":
        user = input('\nDigite o nome que gostaria de criar para a visualização: ')
        BDSQL.view(user)
    else:
        print('\nNenhuma visualização foi criada.')
    
    # Ver todos os registros das tabelas
    user = input("\nGostaria de ver todos os registros? [Y/N] ")
    if user.upper() == "Y":
        print("\n---Registros---")
        BDSQL.mostrar()
    else:
        print('\nNenhuma consulta foi realizada.')
