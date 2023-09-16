#IMPORTAÇÃO DE BIBLIOTECAS
import brazilcep as bc
import pandas as pd
import time

#CRIANDO LISTAS VAZIAS PARA ARMAZENAR AS INFORMAÇÕES CAPTURADAS PELA BIBLIOTECA PYCEP_CORREIOS
ceps = []
logradouros = []
bairros = []
cidades = []
ufs = []
complementos = []

#LEITURA DA PLANILHA COM OS CEP'S
df = pd.read_excel('lista_de_ceps.xlsx')

#INICIANDO O PROCESSAMENTO DO ARQUIVO
print('Processamento iniciado ...')

#PERCORRENDO A PLANILHA LIDA ACIMA
for index, row in df.iterrows():
    
    #LENDO A COLUNA 'CEP' DA PLANILHA
    cep = df['CEP'][index]
    
    #EFETUANDO A REQUISIÇÃO 
    address = bc.get_address_from_cep(cep)

    print(address)

    #ADICIONANDO INFORMAÇÕES CAPTURADAS NOS ARRAYS
    ceps.append(address['cep'])
    logradouros.append(address['street'])
    bairros.append(address['district'])
    cidades.append(address['city'])
    ufs.append(address['uf'])
    complementos.append(address['complement'])
    
    #DELAY DE 1 SEGUNDO PARA NÃO SOBRECARREGAR A API DE CONSULTA
    time.sleep(1)
    
#TRANSFORMAÇÃO DAS LISTAS EM UM DICIONÁRIO    
data = {'cep':ceps,'logradouro':logradouros,'bairro':bairros,'cidade':cidades,'uf':ufs,'complemento':complementos}

#CRIANDO UM DATA FRAME COM BASE NO DICIONÁRIO CRIADO ACIMA
data = pd.DataFrame(data)

#TRANSFORMANDO EM UM ARQUIVO EXCEL
data.to_excel("lista_de_ceps_preenchidos.xlsx",index=False)

#FINALIZANDO O PROCESSAMENTO DO ARQUIVO
print('Processamento finalizado ...')