# NÃO EXCLUIR ESSA LÓGICA
# LÓGICA AVANÇADA PARA DATA DE NASCIMENTO
MESES = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

mes = 7
dia = 28



'''
if any(i >= mes or i <= mes for i in MESES.keys()) or any(i >= dia or i <= dia for i in MESES[mes]):
    print('Certo')
else:
    print('Erro')
'''