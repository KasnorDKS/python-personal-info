from datetime import date
import requests
from string import ascii_uppercase

DATA_ATUAL = date.today() # Pega o dia atual em formato YYYY-MM-DD
DIA_ATUAL = DATA_ATUAL.day # Armazena o dia
MES_ATUAL = DATA_ATUAL.month # Armazena o mês
ANO_ATUAL = DATA_ATUAL.year # Armazena o ano

# Armazena domínios comuns de endereços de emails
EMAILS = ['@gmail.com', '@outlook.com', '@hotmail.com', '@yahoo.com', '@icloud.com', '@aol.com']

# Armazena o número dos meses com os dias finais
MESES = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30, 
         '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}

class Pessoa():
    def __init__(self, nome, sobrenome, nascimento, email, telefone, cpf, rg, endereco):
        # Declaração dos valores
        self._nome = nome
        self._sobrenome = sobrenome
        self._email = email
        self.__cpf = cpf
        self.__rg = rg
        self._telefone = telefone
        self._nascimento = nascimento
        self.__calcular = nascimento
        self.__endereco = endereco
    
    def nome(self):
        # A primeira letra do nome ficará em caixa alta
        self._nome = self._nome.title()
        
        # Retorna o valor
        return f'{self._nome}'
    
    
    def sobrenome(self):
        # As primeiras letras de cada sobrenome ficará em caixa alta
        self._sobrenome = self._sobrenome.title()
        
        return f'{self._sobrenome}'
    
    # Formata para data padrão do Brasil
    def nascimento(self):
        
        # Separa e define as variáveis por meio de um caractere específico
        if any(char in self._nascimento for char in ['/', '.', '-']):
            if '/' in self._nascimento:
                dia, mes, ano = self._nascimento.split('/')
                self._nascimento = self._nascimento.replace('/', "")
            if '.' in self._nascimento:
                dia, mes, ano = self._nascimento.split('.')
                self._nascimento = self._nascimento.replace('.', "")
            if '-' in self._nascimento:
                dia, mes, ano = self._nascimento.split('-')
                self._nascimento = self._nascimento.replace('-', "")

        # Adiciona um ou dois 0 (zeros) caso o usuário não tenha colocado
        if (len(dia) == 1) or (len(dia) == 0):
            while True:
                dia = '0' + dia
                if len(dia) == 2:
                    break
        if (len(mes) == 1) or (len(mes) == 0):
            while True:
                mes = '0' + mes
                if len(mes) == 2:
                    break
        if (len(ano) == 3) or (len(ano) == 2) or (len(ano) == 1) or (len(ano) == 0):
            while True:
                ano = '0' + ano
                if len(ano) == 4:
                    break
        
        # Formata a data para o padrão brasileiro
        data = f'{dia}/{mes}/{ano}'
        
        # Converte o dia e o mês em números inteiros, removendo os 0 (zero) no início
        dia = int(dia)
        mes = int(mes)
        
        # Converte o mes em String sem nenhum 0 (zero) no início
        # Trás compatibilidade com o dicionário MESES
        mesStr = str(mes)
        
        # Retorna o valor de acordo com o resultado do usuário
        if len(data) == 10:
            if mesStr in MESES.keys() and 1 <= dia <= MESES[mesStr]:
                self._nascimento = data
                return f'{self._nascimento}'
        elif (ano[0] == '0') or (mes == '00') or (dia == '00'):
            self._nascimento = f'Erro: A data de nascimento fornecida ({data}) é inválida.'
            return f'{self._nascimento}'
        else:
            self._nascimento = f'Erro: A data de nascimento fornecida ({data}) é inválida.'
            return f'{self._nascimento}'
    
    # Verificação básica para verificar se é um endereço de email
    def email(self):
        
        # Caso tenha alguma letra maiúscula no email, irá retornar um erro
        if any(maiuscula in self._email for maiuscula in ascii_uppercase):
            self._email = 'Erro: Endereço de Email inválido'
            
        # Verifica se há @ no email
        elif ('@' in self._email):
            if any(dominio in self._email for dominio in EMAILS):
                self._email = self._email
            else:
                self._email = self._email
        else:
            # Considera como inválido
            self._email = 'Erro: Endereço de Email inválido'
            
        # Retorna o valor
        return f'{self._email}'
    
    # Formata o número de telefone para o formato padrão do Brasil
    def telefone(self):
        
        # Remove qualquer caractere ou espaço indesejado
        if any(char in self._telefone for char in ['.', '/', '-', '+', '(', ')', ' ']):
            self._telefone = self._telefone.replace('.', "").replace('/', "").replace('-', "")\
                .replace('+', "").replace('(', "").replace(')', "").replace(' ', '').strip()
        
        # Dependendo do tamanho, formata o número do telefone
        match len(self._telefone):
            # Verifica quantos caracteres há no número e, dependendo da quantidade, altera para determinado formato
            case 10:
                self._telefone = f'+55 ({self._telefone[:2]}) 9{self._telefone[2:6]}-{self._telefone[6:]}'
            case 11:
                self._telefone = f'+55 ({self._telefone[:2]}) {self._telefone[2:7]}-{self._telefone[7:]}'
            case 12:
                self._telefone = f'+{self._telefone[:2]} ({self._telefone[2:4]}) 9{self._telefone[4:8]}-{self._telefone[8:]}'
            case 13:
                self._telefone = f'+{self._telefone[:2]} ({self._telefone[2:4]}) {self._telefone[4:9]}-{self._telefone[9:]}'
            case _:
                self._telefone = 'Erro: Telefone inválido'
        
        return f'{self._telefone}'
    
    # Formata o CPF para o formato padrão do Brasil
    def cpf(self):
        
        if self.__cpf.isdigit():
            self.__cpf = str(self.__cpf)
        
        if any(char in self.__cpf for char in ['.', '/', '-', '+', '(', ')']):
            self.__cpf = self.__cpf.replace('.', "").replace('/', "").replace('-', "")\
                .replace('+', "").replace('(', "").replace(')', "")
        
        # Formata para o padrão de cpf
        self.__cpf = f'{self.__cpf[0:3]}.{self.__cpf[3:6]}.{self.__cpf[6:9]}-{self.__cpf[-2:]}'
        
        if len(self.__cpf) == 14:
            self.__cpf = self.__cpf
        else:
            # Considera como inválido
            self.__cpf = 'Erro: CPF inválido'
            
        return f'{self.__cpf}'
    
    # Retira síbolos comuns do RG
    def rg(self):
        
        if any(char in self.__rg for char in [ '/', '+', '(', ')']):
            self.__rg = self.__rg.replace('/', "").replace('+', "")\
                .replace('(', "").replace(')', "")

        if (len(self.__rg) > 13) or (len(self.__rg) <= 6):
            self.__rg = 'Erro: RG inválido'
        else:
            self.__rg = self.__rg

        return f'{self.__rg}'    
    
    # Procura o endereço pelo CEP (Não inclui número do domicílio)
    def endereco(self):
        
        # Remove qualquer caractere ou espaço indesejado
        if any(char in self.__endereco for char in ['-', '.', ' ']):
            self.__endereco.replace('-', '').replace('.', '').replace(' ', '').strip()
        
        # Verifica se o CEP formatado possui 8 caracteres
        if len(self.__endereco) == 8:
            # Formata o CEP para o padrão brasileiro
            cep = f'{self.__endereco[:5]}-{self.__endereco[-3:]}'
            
            # Busca o endereço pelo CEP fornecido
            url = f"https://cep.awesomeapi.com.br/json/{self.__endereco}"
            response = requests.get(url)
            data = response.json()
            
            rua = f"{data.get('address', 'N/A')}"
            cidade = f"{data.get('city', 'N/A')}"
            estado = f"{data.get('state', 'N/A')}"
            
            # Retorna todos os valores em formato de lista
            return [cep, rua, cidade, estado]

        else:
            self.__endereco = 'Erro: Endereço inválido ou não encontrado.'
            return f'{self.__endereco}'
        
    def risco(self):
        
        # Remove qualquer caractere ou espaço indesejado
        if any(char in self._nascimento for char in ['.', '/', '-', '(', ')', 'NA']):
            self._nascimento = self._nascimento.replace('.', "").replace('/', "").replace('-', "")\
                .replace('NA', '').strip()

        # Formata a data para o padrão brasileiro
        data = f"{self._nascimento[0:2]}/{self._nascimento[2:4]}/{self._nascimento[-4:]}"
        
        # Irá separar e armazenar cada valor nas variáveis já formatada para int
        dia, mes, ano = map(int, data.split('/'))
        
        # Calcula a idade do usuário pelo ano de nascimento com o ano atual
        idade = ANO_ATUAL - ano
        
        # Verifica se o usuário já fez aniversário este ano
        if mes > MES_ATUAL or (mes == MES_ATUAL and dia > DIA_ATUAL):
            idade = idade - 1
        
        # Converte o mês para String para ter compatibilidade com o dicionário MESES
        mes = str(mes)
        
        if mes in MESES.keys() and 1 <= dia <= MESES[mes]:
            mes = int(mes)
            if (ano > ANO_ATUAL) or (ano == ANO_ATUAL and mes > MES_ATUAL) \
            or (dia > DIA_ATUAL and ano == ANO_ATUAL and mes == MES_ATUAL):
                self.__calcular = f'Erro: A data de nascimento fornecida ({data}) é inválida.'
                return f'{self.__calcular}'
            
            elif idade >= 65:
                self.__calcular = '[V]'
            else:
                self.__calcular = '[X]'
                
            return f'{self.__calcular}'
        
        else:
            self.__calcular = f'Erro: A data de nascimento fornecida ({data}) é inválida.'
            return f'{self.__calcular}'

if __name__ == '__main__':
    PESSOA = Pessoa('pedro', # Nome (nome())
                    'silva', # Sobrenome (sobrenome())
                    '12/12/2001', # Data de nascimento (nascimento()) (calcular_idade())
                    'usuariopedro7@gmail.com', # Email (email())
                    '+55 (00) 91234-5678', # Telefone (telefone())
                    '123.456.789.10', # CPF (cpf())
                    '1234567', # RG (rg())
                    '05424020', # Cep (endereco())
                    )
    
    print(f"Nome: {PESSOA.nome()}")
    print(f"Sobrenome: {PESSOA.sobrenome()}")
    print(f"Data de nascimento: {PESSOA.nascimento()}")
    print(f"Risco: {PESSOA.risco()}")
    print(f"Email: {PESSOA.email()}")
    print(f"Telefone: {PESSOA.telefone()}")
    print(f"CPF: {PESSOA.cpf()}")
    print(f"RG: {PESSOA.rg()}")
    print(f"CEP: {PESSOA.endereco()[0]}")
    print(f"Rua: {PESSOA.endereco()[1]}")
    print(f"Cidade: {PESSOA.endereco()[2]}")
    print(f"Estado: {PESSOA.endereco()[3]}")
