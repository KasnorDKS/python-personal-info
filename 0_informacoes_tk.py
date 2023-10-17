import tkinter as tk
from informacoes import Pessoa

PESSOA = Pessoa('pedro', # Nome (nome())
                'silva', # Sobrenome (sobrenome())
                '41/7/2023', # Data de nascimento (nascimento()) (calcular_idade())
                'pedrinho7@gmail.com', # Email (email())
                '+55 (00) 91234-5678', # Telefone (telefone())
                '123.456.789.10', # CPF (cpf())
                '1234567', # RG (rg())
                '05424020', # Cep (endereco())
                )

janela = tk.Tk()

janela.geometry('640x480')

texto = f"""{PESSOA.nome()}
{PESSOA.sobrenome()}
{PESSOA.email()}
{PESSOA.cpf()}
{PESSOA.rg()}
{PESSOA.telefone()}
{PESSOA.nascimento()}
{PESSOA.endereco()[0]}
{PESSOA.endereco()[1]}
{PESSOA.endereco()[2]}
{PESSOA.endereco()[3]}
"""

label = tk.Label(janela, text=texto)
label.pack()

quit = tk.Button(janela, text="Fechar", command=janela.destroy)
quit.pack()

janela.mainloop()