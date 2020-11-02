import mysql.connector

con = mysql.connector.connect(host='localhost', database='Cadastro_Clientes', user='root', password='Poker1993Face#')

if con.is_connected(): # USAR ESSE CÓDIGO PARA VERIFICAR SE A CONEXÃO COM O BANCO DE DADOS FOI ESTABELECIDA COM SUCESSO.
    bd_info = con.get_server_info()
    print(f'CONECTADO AO SERVIDOR MySQL, VERSÃO: {bd_info}')

