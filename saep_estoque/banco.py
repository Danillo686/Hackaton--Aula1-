import mysql.connector 

def conectar():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="senai",
        database="saep_estoque",
    ) 
    return conexao

def cadastrar_produto(nome, categoria, quantidade, preco):
    conexao = conectar()
    cursor = conexao.cursor() 

    sql = """
    INSERT INTO produtos (nome, categoria, quantidade, preco)
    VALUES (%s, %s, %s, %s);
    """

    valores = (nome, categoria, quantidade, preco)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()


#Busca de dados! ->

def listar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT id, nome, categoria, quantidade, preco FROM produtos")
    produtos = cursor.fetchall()
    
    cursor.close()
    conexao.close()
    return produtos


#Atualizar dados! ->

def atualizar_produto(id_produto, nome, categoria, quantidade, preco):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "UPDATE produtos SET nome = %s, categoria = %s, quantidade = %s, preco = %s WHERE id = %s;"
    valores = (nome, categoria, quantidade, preco, id_produto)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    

# EXcluir dados! ->    
def excluir_produto(id_produto):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "DELETE FROM produtos WHERE id = %s;"
    cursor.execute(sql, (id_produto,))
    conexao.commit()

    cursor.close()
    conexao.close()
    conexao.close()