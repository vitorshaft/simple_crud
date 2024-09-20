import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self, db_file):
        """Inicializa a conexão com o banco de dados SQLite."""
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
            print("Conexão com SQLite estabelecida.")
        except Error as e:
            print(f"Erro ao conectar ao SQLite: {e}")

    def close_connection(self):
        """Fecha a conexão com o banco de dados."""
        if self.conn:
            self.conn.close()
            print("Conexão com SQLite fechada.")

    def create_table(self):
        """Cria uma tabela 'pessoas' no banco de dados."""
        try:
            sql_create_pessoas_table = """
            CREATE TABLE IF NOT EXISTS pessoas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER,
                email TEXT UNIQUE
            );"""
            self.conn.execute(sql_create_pessoas_table)
            print("Tabela 'pessoas' criada com sucesso.")
        except Error as e:
            print(f"Erro ao criar tabela: {e}")

    def add_pessoa(self, nome, idade, email):
        """Insere uma nova pessoa na tabela 'pessoas'."""
        try:
            sql_insert = """
            INSERT INTO pessoas(nome, idade, email)
            VALUES (?, ?, ?);"""
            cur = self.conn.cursor()
            cur.execute(sql_insert, (nome, idade, email))
            self.conn.commit()
            print("Pessoa adicionada com sucesso.")
        except Error as e:
            print(f"Erro ao adicionar pessoa: {e}")

    def get_pessoas(self):
        """Retorna todas as pessoas da tabela 'pessoas'."""
        try:
            sql_select = "SELECT * FROM pessoas;"
            cur = self.conn.cursor()
            cur.execute(sql_select)
            rows = cur.fetchall()
            return rows
        except Error as e:
            print(f"Erro ao buscar pessoas: {e}")
            return []

    def update_pessoa(self, pessoa_id, nome, idade, email):
        """Atualiza uma pessoa existente na tabela 'pessoas'."""
        try:
            sql_update = """
            UPDATE pessoas
            SET nome = ?, idade = ?, email = ?
            WHERE id = ?;"""
            cur = self.conn.cursor()
            cur.execute(sql_update, (nome, idade, email, pessoa_id))
            self.conn.commit()
            print("Pessoa atualizada com sucesso.")
        except Error as e:
            print(f"Erro ao atualizar pessoa: {e}")

    def delete_pessoa(self, pessoa_id):
        """Deleta uma pessoa da tabela 'pessoas'."""
        try:
            sql_delete = "DELETE FROM pessoas WHERE id = ?;"
            cur = self.conn.cursor()
            cur.execute(sql_delete, (pessoa_id,))
            self.conn.commit()
            print("Pessoa deletada com sucesso.")
        except Error as e:
            print(f"Erro ao deletar pessoa: {e}")
