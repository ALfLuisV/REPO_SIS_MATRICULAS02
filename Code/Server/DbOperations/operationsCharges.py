import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[2]))


from Server.db_connection import connect_to_db

sys.path.append(str(Path(__file__).parents[0]))

from operationsDiscipline import get_discipline_type


def inserir_cobranca(lista_disciplinas, lista_ids, id_aluno):
    connection, cursor = connect_to_db()
    if connection and cursor:
        try:

            nova_lista_ids = [item[0] for item in lista_ids]#formata o array de ids de matricula

            

            lista_type_discipline = []
            for const in lista_disciplinas:
                lista_type_discipline.append(get_discipline_type(const['id_disc']))#pega o tipo de cada disciplina matriculada

            resultado = [item[0][0] for item in lista_type_discipline]#formata o array de tipos de disciplinas matriculas
            
            chargers_list = [] 

            for i in range(len(lista_disciplinas)):
                if resultado[i] == 'Obrigatoria':
                    charge = {"debt": 5, "fee": 1200.00, "status": "pendente", "id_registration": nova_lista_ids[i], "id_student": id_aluno}
                else:
                    charge = {"debt": 3, "fee": 800.00, "status": "pendente", "id_registration": nova_lista_ids[i], "id_student": id_aluno}
                
                chargers_list.append(charge)

            lista_charge_length = len(chargers_list)

            insert_disciplines_query = '''
            INSERT INTO charge (debttime, fees, status, idregistration, idStudent)
            VALUES
            '''
            
            


            count = -1
            for charge in chargers_list:
                count +=1
                if count == lista_charge_length-1:
                    insert_disciplines_query += f'''
                    ('{charge["debt"]}', {charge["fee"]}, '{charge["status"]}', {charge["id_registration"]}, {charge["id_student"]});
                    '''
                else:
                    insert_disciplines_query += f'''
                    ('{charge["debt"]}', {charge["fee"]}, '{charge["status"]}', {charge["id_registration"]}, {charge["id_student"]}),
                    '''
                
            cursor.execute(insert_disciplines_query)
            connection.commit()
            print("Cobrança(s) registrada(s) com sucesso.")
        except Exception as error:
            print(f"Erro ao processar cobranças: {error}")
        finally:
            cursor.close()
            connection.close()

# Função para buscar todos os cursos
def buscar_cursos():
    connection, cursor = connect_to_db()
    if connection and cursor:
        try:
            buscar_query = "SELECT * FROM course;"
            cursor.execute(buscar_query)
            cursos = cursor.fetchall()
            return cursos
        except Exception as error:
            print(f"Erro ao buscar cursos: {error}")
        finally:
            cursor.close()
            connection.close()
