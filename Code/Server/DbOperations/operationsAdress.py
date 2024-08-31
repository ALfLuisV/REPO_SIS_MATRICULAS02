import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[2]))


from Server.db_connection import connect_to_db


def inserir_endereco(street, city, state, country, idd):
    connection, cursor = connect_to_db()
    if connection and cursor:
        try:
            inserir_query_endereco = '''
            INSERT INTO address (idusuario, city, state, street, country) 
            VALUES (%s, %s, %s, %s, %s)
            RETURNING idusuario;
            '''
            
            cursor.execute(inserir_query_endereco, (idd, city , state, street, country))
            connection.commit()
            print("Endereço inserido com sucesso.")
        except Exception as error:
            print(f"Erro ao inserir endereço: {error}")
        finally:
            cursor.close()
            connection.close()

# Função para buscar todos os alunos
def buscar_endereco(idd):
    connection, cursor = connect_to_db()
    if connection and cursor:
        try:
            buscar_query = "SELECT * FROM address WHERE idusuario = %s;"
            cursor.execute(buscar_query, (idd))
            endereco = cursor.fetchall()
            return endereco
            # for aluno in alunos:
            #     print(aluno)
        except Exception as error:
            print(f"Erro ao buscar endereço: {error}")
        finally:
            cursor.close()
            connection.close()
