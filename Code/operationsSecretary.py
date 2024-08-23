import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))


from db_connection import connect_to_db


def inserir_secretario(nome, email, telefone, senha, sk, turno):
    connection, cursor = connect_to_db()
    if connection and cursor:
        try:
            inserir_query_usuario = '''
            INSERT INTO users (name, number, email, password, saltk) 
            VALUES (%s, %s, %s, %s, %s)
            RETURNING idusuario;
            '''
            
            cursor.execute(inserir_query_usuario, (nome, telefone , email, senha, sk))
            idUsuario = cursor.fetchone()[0]
            connection.commit()
            print("usuario criado....")
            
            inserir_query_secretario = '''
            INSERT INTO secretary (idSecretary, turno)
            VALUES (%s, %s);
            '''
            cursor.execute(inserir_query_secretario, (idUsuario, turno))
            connection.commit()
            print("Secretario inserido com sucesso.")
            return idUsuario
        except Exception as error:
            print(f"Erro ao inserir secretario: {error}")
        finally:
            cursor.close()
            connection.close()

# Função para buscar todos os alunos
def buscar_secretarios():
    connection, cursor = connect_to_db()
    if connection and cursor:
        try:
            buscar_query = "SELECT * FROM secretary;"
            cursor.execute(buscar_query)
            alunos = cursor.fetchall()
            return alunos
            # for aluno in alunos:
            #     print(aluno)
        except Exception as error:
            print(f"Erro ao buscar secretarios: {error}")
        finally:
            cursor.close()
            connection.close()
