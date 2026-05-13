import db
from rich import print

def iniciar():
    while True:
        print("""[bright_white]------------------------------------[/]
[italic bright_white]Selecione a opção desejada:[/]

[bright_white][ 1 ] - Listar Produtos[/]
[bright_green][ 2 ] - Adicionar Produto[/]
[bright_blue][ 3 ] - Alterar Produto[/]
[bright_red][ 4 ] - Excluir Produto[/]
[bright_black][ 0 ] - Encerrar Programa[/]
[bright_white]------------------------------------[/]""")
        try:
            resposta = int(input("Opção: "))
        except ValueError:
            print("\n[bright_red][ERRO][/] [bright_white]Digite um número [underline white]Inteiro[/] válido.[/]\n")
            continue
        except KeyboardInterrupt:
            print("\n\n[bright_red][ERRO][/] [bright_white]Operação [underline bright_yellow]cancelada[/] pelo usuário.[/]\n")
            continue
        
        if resposta == 0:
            break
        elif resposta == 1:
            # Faz a leitura dos itens do banco de dados
            db.read()

        elif resposta == 2:
            # Adiciona um novo produto ao banco de dados
            produto = str(input("Digite o nome do produto: "))
            preco = float(input("Digite o valor do produto: R$ "))
            db.create(produto, preco)

        elif resposta == 3:
            # Altera os dados desejados no bd
            produto = str(input("Digite o nome do produto que você deseja alterar o nome do valor: "))
            preco = float(input("Digite para qual valor você deseja alterar: R$ "))
            db.update(produto, preco)

        elif resposta == 4: 
            # Deleta algum dado do bd
            produto = str(input("Digite o nome do produto que você deseja excluir: "))
            resp = str(input(f"Tem certeza que deseja excluir o produto {produto}? [S / N] ")).strip()[0]

            if resp in "Ss":
                db.delete(produto)
            elif resp in "Nn":
                print("\n[underline bright_yellow]Operação cancelada.[/]\n")
                continue
            else:
                print("\n[bright_white]Escolha uma opção válida de [underline white][S, s ou N, n][/][/]\n")

        elif resposta > 4 or resposta < 0:
            print("\n[bright_red][ERRO][/] [bright_white]Digite um número válido [underline white]dentro das opções disponiveis.[/][/]\n")
