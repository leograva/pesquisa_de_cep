# pesquisa_de_cep
Pesquisa de CEP automatizada utilizando as bibliotecas pycep_correios e pandas.

A pesquisa consiste em efetuar a leitura de uma planilha que contém uma lista de CEPS, efetuar a busca de cada um deles através da biblioteca pycep_correios e em seguida gerar uma nova planilha com os dados capturados.

Arquivo de lista de CEP's

![image](https://user-images.githubusercontent.com/34873898/230697354-a51db986-55ab-463c-9d66-3ab5e9e0b9ba.png)

Arquivo gerado após o processamento

![image](https://user-images.githubusercontent.com/34873898/230697373-0f72f3ba-9a77-44d7-bef7-4ff9f784ded3.png)

Instruções de execução:

- Instale as bibliotecas Pandas e Pycep_correios através do comandos abaixo:

    pip install pycep_correios pandas

- Execute o arquivo "consulta_de_cep.py" utilizando o comando abaixo:
  
    python consulta_de_cep.py
    python3 consulta_de_cep.py
    
- Após a execução é necessário aguardar até que o Processamento seja finalizado como na imagem abaixo:

![image](https://user-images.githubusercontent.com/34873898/230697496-7598e0f1-5908-4d19-93d0-e02ced70dc51.png)

- Por fim, abra o arquivo gerado ("lista_de_ceps_preenchidos.xlsx") e o arquivo estará com as informações capturadas :) 
