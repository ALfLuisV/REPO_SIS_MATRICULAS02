from aluno import Aluno
from secretario import Secretario
from professor import Professor


sec1 = Secretario(1, "maria","33753729","maria@gmail.com", "manha")
# sec1.cadastrar_aluno()
aluno = Aluno(1, "JV", "31990890989", "jvdobairro@gmail.com","xxxxxxxxx")
aluno.matricular(21)

prof = Professor(1, "mario", "33759686","mario@gmail.com", 40, 3200.00 )

prof.visualizaralunos(22)
 