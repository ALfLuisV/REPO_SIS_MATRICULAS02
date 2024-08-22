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

# Função para criar uma tabela no banco de dados
def criar_tabela(connection, cursor):
    if connection and cursor:
        try:
            # Query SQL para criar a tabela
            criar_tabela_query = '''
            CREATE TABLE IF NOT EXISTS alunos (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100),
                email VARCHAR(100) UNIQUE,
                telefone VARCHAR(15)
            );
            '''

            # Executar a query de criação da tabela
            cursor.execute(criar_tabela_query)

            # Confirmar a criação da tabela no banco de dados
            connection.commit()
            print("Tabela criada com sucesso.")
        
        except Exception as error:
            print(f"Erro ao criar a tabela: {error}")
        
        finally:
            # Fechar o cursor e a conexão
            cursor.close()
            connection.close()

# Testando a conexão e criando a tabela
connection, cursor = connect_to_db()

if connection and cursor:
    criar_tabela(connection, cursor)
else:
    print("Não foi possível conectar ao banco de dados.")

