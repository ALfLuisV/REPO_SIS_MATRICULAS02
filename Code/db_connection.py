import psycopg2

# Informações de conexão
host = "ep-broad-bird-a4kz4zta-pooler.us-east-1.aws.neon.tech"
dbname = "verceldb"
user = "default"
password = "z8lc5vOdDbBL"
port = "5432"
sslmode = "require"

# Função para conectar ao banco de dados
def connect_to_db():
    try:
        # Estabelecendo a conexão com o banco de dados
        connection = psycopg2.connect(
            host=host,
            dbname=dbname,
            user=user,
            password=password,
            port=port,
            sslmode=sslmode
        )
        
        # Criando um cursor para realizar operações no banco de dados
        cursor = connection.cursor()

        # Teste de conexão
        cursor.execute("SELECT version();")
        print(f"Conectado ao banco de dados PostgreSQL.")

        return connection, cursor

    except Exception as error:
        print(f"Erro ao conectar ao banco de dados: {error}")
        return None, None



