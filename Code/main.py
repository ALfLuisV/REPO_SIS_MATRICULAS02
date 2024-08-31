from aluno import Aluno
from secretario import Secretario
from professor import Professor
from login import Login


sec1 = Secretario(1, "maria","33753729","maria@gmail.com", "manha")
# log = Login()
# log.logar_sistema("mateus@gmail.com", "6qkC50U")
# # sec1.cadastrar_aluno()
aluno = Aluno(1, "JV", "31990890989", "jvdobairro@gmail.com","xxxxxxxxx")
# aluno.matricular(28)

# prof = Professor(1, "mario", "33759686","mario@gmail.com", 40, 3200.00 )

# prof.visualizaralunos(27)
# sec1.cadastrar_professor()
# sec1.cadastrar_curso()
# sec1.cadastrar_disciplina_em_curso_existente()
sec1.gerarcurriculo()