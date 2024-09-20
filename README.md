# simple_crud: CRUD Simples em Python com SQLite

Este projeto é um exemplo básico de um sistema CRUD (Create, Read, Update, Delete) utilizando Python e SQLite. Ele permite gerenciar uma tabela de pessoas em um banco de dados SQLite, executando operações como adicionar, atualizar, listar e deletar registros.

O código foi implementado de forma simples e eficiente, ideal para quem deseja aprender como interagir com um banco de dados SQLite em Python.

## Funcionalidades

- **Criar Tabela**: Cria a tabela `pessoas` no banco de dados para armazenar informações de nome, idade e email.
- **Inserir Registros**: Adiciona uma nova pessoa à tabela, com os campos nome, idade e email.
- **Listar Registros**: Exibe todos os registros armazenados na tabela `pessoas`.
- **Atualizar Registros**: Atualiza os dados de uma pessoa existente, com base no ID.
- **Deletar Registros**: Remove uma pessoa do banco de dados, usando seu ID.
- **Conectar e Desconectar**: Gerencia a conexão com o banco de dados SQLite.

## Estrutura do Projeto

- `simple_crud.py`: Contém a classe `Database`, responsável por todas as operações de CRUD no banco de dados.
- `main.py`: Script de exemplo que demonstra o uso da classe `Database` para criar uma tabela, adicionar, listar, atualizar e deletar pessoas.

## Como Começar

### Pré-requisitos

- Python 3.9 ou superior instalado no seu computador.
- O SQLite já vem embutido no Python, então você não precisa de instalações adicionais para rodar este projeto.

### Executando o Projeto

1. Clone este repositório:

    ```sh
    git clone https://github.com/seuusuario/simple_crud.git
    ```

2. Navegue até o diretório do projeto:

    ```sh
    cd simple_crud
    ```

3. Execute o arquivo `main.py`:

    ```sh
    python main.py
    ```

## Exemplo de Uso

No script `main.py`, é demonstrado como interagir com o banco de dados:

1. **Criar a tabela**: O banco de dados `test.db` é inicializado e a tabela `pessoas` é criada.
2. **Inserir pessoas**: Duas pessoas, Alice e Bob, são adicionadas.
3. **Listar pessoas**: O sistema exibe todas as pessoas cadastradas no banco.
4. **Atualizar um registro**: Alice tem seu email e idade atualizados.
5. **Deletar um registro**: Bob é removido do banco de dados.
6. **Listar pessoas novamente**: O sistema exibe a lista atualizada, com Alice após a atualização e sem o Bob.

```python
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
```
## Detalhes Técnicos
- Conexão com o Banco de Dados: A conexão é aberta no momento em que o objeto Database é criado, e fechada no final, garantindo que os recursos sejam gerenciados corretamente.
- Criação da Tabela: A tabela pessoas possui três campos principais: nome (texto), idade (inteiro) e email (texto, com restrição de ser único).
- Tratamento de Erros: Cada operação com o banco de dados está encapsulada em blocos try-except para capturar e tratar erros, garantindo maior estabilidade ao programa.
## Próximas Melhorias
- Implementação de validações para entradas do usuário, como garantir que o email seja válido ou que a idade seja um número positivo.
- Adicionar mais funcionalidades como filtros de busca por nome ou email.
- Interface gráfica ou uma API para facilitar a interação com o sistema.
## Licença
Este projeto é open-source e está sob a licença MIT. Sinta-se à vontade para modificar e melhorar o código conforme necessário.#   s i m p l e _ c r u d  
 