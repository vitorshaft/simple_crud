from simple_crud import Database

# Inicializar o banco de dados
db = Database("test.db")

# Criar a tabela
db.create_table()

# Inserir pessoas
db.add_pessoa("Alice", 30, "alice@example.com")
db.add_pessoa("Bob", 25, "bob@example.com")

# Listar todas as pessoas
pessoas = db.get_pessoas()
for pessoa in pessoas:
    print(pessoa)

# Atualizar uma pessoa
db.update_pessoa(1, "Alice", 31, "alice.updated@example.com")

# Deletar uma pessoa
db.delete_pessoa(2)

# Listar todas as pessoas após a atualização e deleção
pessoas = db.get_pessoas()
for pessoa in pessoas:
    print(pessoa)

# Fechar a conexão com o banco de dados
db.close_connection()
