import psycopg2


def conectar():
    try:
        conexao = psycopg2.connect(
            host="localhost",
            database="posto_luizao",
            user="postgres",
            password="root",  # ⚠️ COLOQUE A SUA SENHA DO POSTGRESQL AQUI
            port="5432",
        )
        return conexao
    except Exception as error:
        print(f"Erro ao conectar ao PostgreSQL: {error}")
        return None