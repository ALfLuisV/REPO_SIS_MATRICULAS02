import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))


from db_connection import connect_to_db

# Função para inserir dados na tabela 'alunos'
def logar_sistema(email):
    connection, cursor = connect_to_db()
    if connection and cursor:
        try:
            inserir_query_usuario = '''
            SELECT * FROM users WHERE email = %s
            '''
            
            cursor.execute(inserir_query_usuario, (email,))
            pwd = cursor.fetchone()
            connection.commit()

            return pwd
        except Exception as error:
            print(f"Erro ao logar usuario: {error}")
        finally:
            cursor.close()
            connection.close()

