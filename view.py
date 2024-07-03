import sqlite3 as lite
from datetime import datetime

# Criando conexão
con = lite.connect('dados.db')

# CRUD


# Inserir dados
def inserir_form(i):      
    with con:
            cur = con.cursor()
            query = "INSERT INTO Produtos(cod, nome, descricao, valor_unitario) VALUES (?,?,?,?)"
            cur.execute(query, i)


# Atualizar dados
def atualizar_form(i):
    with con:
            cur = con.cursor()
            query = "UPDATE Produtos SET cod=?, nome=?, descricao=?, valor_unitario=? WHERE cod=?"
            cur.execute(query, i)


# Deletar dados
def deletar_form(i):
    with con:
            cur = con.cursor()
            query = "DELETE FROM Produtos WHERE cod=?"
            cur.execute(query, i)


# Ver dados
def ver_form():
    ver_dados= []
    with con:
            cur = con.cursor()
            query = "SELECT * FROM Produtos"
            cur.execute(query)

            rows = cur.fetchall()
            for row in rows:
                ver_dados.append(row)
    return ver_dados
