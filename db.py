import mysql.connector
from rich import print
from conector import conectar


# Criação do cursor
# cursor = db.cursor() # Cria o cursor para executar o banco de dados 

# Comandos básicos 
# comando = ''


# cursor.execute(comando) # executa o comando
# db.commit() # edita o banco de dados (create, update & delete)
# result = cursor.fetchall()  # lê o banco de dados (read)

# CREATE
def create(produto, preco):
    try:
        db = conectar()
    except:
        print("[bright_red][ERRO][/] [bright_white]Não foi possível acessar o banco de dados.[/]")
    cursor = db.cursor()

    nome_produto = produto # VARCHAR(45)
    valor = preco # DECIMAL(10, 2)
    comando = 'INSERT INTO produtos (nome_produto, valor) VALUES (%s, %s)'
    cursor.execute(comando, (nome_produto, valor))
    if cursor.rowcount == 0:
        print("\n[bright_yellow]Produto não enconstrado.[/]\n")
    else:
        print("\n[bright_white]Produto [underline bright_green]ADICIONADO[/] com sucesso![/]\n")
    db.commit()

    cursor.close()
    db.close()

# READ
def read():
    try:
        db = conectar()
    except:
        print("[bright_red][ERRO][/] [bright_white]Não foi possível acessar o banco de dados.[/]")
    cursor = db.cursor()

    comando = 'SELECT * FROM produtos'
    cursor.execute(comando)
    result = cursor.fetchall()
    print("[bold white]-[/]" * 36)
    print(f"[bold white]{'LISTA DE PRODUTOS':^36}[/]")
    print("[bold white]-[/]" * 36)
    cont = 1
    for produto in result:
        print(f"[bright_white]{cont}. {produto[1]} -[/] [bright_green]R$ {str(produto[2]).replace('.', ',')}[/]")
        cont += 1
    print('[bright_white]-[/]' * 36)

    cursor.close()
    db.close()

# UPDATE 
def update(produto, preco):
    try:
        db = conectar()
    except:
        print("[bright_red][ERRO][/] [bright_white]Não foi possível acessar o banco de dados.[/]")
    cursor = db.cursor()

    nome_produto = produto
    valor = preco
    comando = 'UPDATE produtos SET valor = %s WHERE nome_produto= %s'
    cursor.execute(comando, (valor, nome_produto))
    if cursor.rowcount == 0:
        print("\n[bright_yellow]Produto não encontrado.[/]\n")
    else:
        print("\n[bright_white]Produto [underline bright_green]ATUALIZADO[/] com sucesso![/]\n")
    db.commit()

    cursor.close()
    db.close()

# DELETE
def delete(produto):
    try:
        db = conectar()
    except:
        print("[bright_red][ERRO][/] [bright_white]Não foi possível acessar o banco de dados.[/]")
    cursor = db.cursor()

    nome_produto = produto
    # Seleciona o id de cada produto com aquele nome
    comando1 = 'SELECT id_produto FROM produtos WHERE nome_produto = %s LIMIT 1'
    cursor.execute(comando1, (nome_produto,))

    # Lê e guarda o id do produto lido
    id_product = cursor.fetchall()
    
    for (id_produto,) in id_product:
        comando2 = 'DELETE FROM produtos WHERE id_produto = %s'
        cursor.execute(comando2, (id_produto,))

        if cursor.rowcount == 0:
            print("\n[bright_yellow]Produto não encontrado.[/]\n")
        else:
            print("\n[bright_white]Produto [underline bright_green]EXCLUIDO[/] com sucesso![/]\n")
        db.commit()

    cursor.close()
    db.close()

# Encerramento 
# cursor.close()
# db.close() 
