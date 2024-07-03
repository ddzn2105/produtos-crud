# Importando o SQLite
import sqlite3 as lite


# Criando conexão
con = lite.connect('dados.db')

# Criando tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Produtos(cod INTEGER PRIMARY KEY,nome TEXT, descricao TEXT, valor_unitario DECIMAL)")
