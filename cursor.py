import mysql.connector

def conexao():
    return mysql.connector.connect(
    user='root',
    password='1234',
    host='127.0.0.1',
    database='GerenciadorBiblioteca'
    )
    
def buscar(dados,tabela):
    x = conexao()
    print(x.is_connected())
    y = x.cursor()
    query = f'select {dados} from {tabela} ;'
    y.execute(query)
    t = y.fetchall()
    y.close()
    x.close()
    return t

def inserir(tabela,**dados):
    x = conexao()
    print(x.is_connected())
    y = x.cursor()
    colunas = ' ,'.join(dados.keys())
    valores = ' ,'.join(['%s']* len(dados))
    query = f"insert into {tabela} ({colunas}) values ({valores})"
    y.execute(query, tuple(dados.values()))
    x.commit()
    y.close()
    x.close()


    
    
    
    
    

