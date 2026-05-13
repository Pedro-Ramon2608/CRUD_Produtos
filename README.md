# CRUD_Produtos

📦 __*Simple CRUD Python & MySQL*__

Este é um sistema de CRUD (Create, Read, Update, Delete) simples desenvolvido em Python para o gerenciamento de produtos em um banco de dados MySQL. O projeto utiliza a biblioteca Rich para proporcionar uma interface de linha de comando (CLI) visualmente atraente e organizada.  

---
🚀 __*Funcionalidades*__

O sistema permite gerenciar uma tabela de produtos com as seguintes operações: 

* __Listar Produtos (Read)__: Exibe todos os produtos cadastrados com seus respectivos valores formatados.

* __Adicionar Produto (Create)__: Insere um novo nome de produto e seu preço no banco de dados.

* __Alterar Produto (Update)__: Atualiza o valor de um produto existente buscando pelo nome.

* __Excluir Produto (Delete)__: Remove um produto do banco de dados com uma confirmação de segurança.

---
🛠️ __*Tecnologias Utilizadas*__

* __Python 3__: Linguagem base do projeto.

* __MySQL__: Sistema de gerenciamento de banco de dados.

* __mysql-connector-python__: Driver para conectar o Python ao MySQL.

* __Rich__: Biblioteca para formatação de texto e cores no terminal.

---
📂 __*Estrutura do Projeto*__

`main.py`: O ponto de entrada do programa que inicia a aplicação. 

`app.py`: Contém o menu interativo e a lógica de fluxo do usuário.  

`db.py`: Gerencia a conexão com o banco de dados e as funções SQL (CRUD).  

---
🔧 __*Configuração do Banco de Dados*__

Para rodar o sistema, você precisará de um servidor MySQL ativo com um banco de dados chamado dbcrud e uma tabela chamada produtos.  

##### SQL
```sql

CREATE DATABASE dbcrud;

USE dbcrud;

CREATE TABLE produtos (

    id_produto INT AUTO_INCREMENT PRIMARY KEY,
    
    nome_produto VARCHAR(45) NOT NULL,
    
    valor DECIMAL(10, 2) NOT NULL
    
);
```

---
⚙️ __*Como Executar*__

1. Instale as dependências:

##### Bash
```
pip install mysql-connector-python rich
```
2. Configure o acesso:

No arquivo db.py, ajuste as credenciais de host, user e password na função conectar() conforme as suas configurações locais.  

3. Inicie o programa:

##### Bash
```bash

python main.py
```

---
⚠️ __*Tratamento de Erros*__

* O sistema inclui proteções para garantir uma boa experiência ao usuário: 

* Validação de entradas para garantir que apenas números inteiros sejam aceitos no menu.  

* Tratamento de KeyboardInterrupt para evitar erros caso o usuário cancele a operação repentinamente.  

* Verificação de conexão com o banco de dados para evitar fechamentos inesperados.
