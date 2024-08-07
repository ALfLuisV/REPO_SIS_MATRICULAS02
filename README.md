# Sistema de Matrículas da Universidade

## Descrição do Sistema
Uma universidade pretende informatizar seu sistema de matrículas. A secretaria da universidade gera o currículo para cada semestre e mantém as informações sobre as disciplinas, professores e alunos. Cada curso tem um nome, um determinado número de créditos e é constituído por diversas disciplinas. Os alunos podem se matricular em 4 disciplinas como 1ª opção (obrigatórias) e em mais 2 outras alternativas (optativas). Há períodos para efetuar matrículas, durante os quais um aluno pode acessar o sistema para se matricular em disciplinas e/ou para cancelar matrículas feitas anteriormente.

## Regras de Negócio
- Uma disciplina só fica ativa, isto é, só vai ocorrer no semestre seguinte se, no final do período de matrículas, tiver pelo menos 3 alunos inscritos (matriculados). Caso contrário, a disciplina será cancelada.
- O número máximo de alunos inscritos em uma disciplina é de 60, e quando este número é atingido, as inscrições (matrículas) para essa disciplina são encerradas.
- Após um aluno se inscrever para um semestre, o sistema de cobranças é notificado pelo sistema de matrículas, de modo que o aluno possa ser cobrado pelas disciplinas daquele semestre.
- Os professores podem acessar o sistema para saber quais são os alunos que estão matriculados em cada disciplina.
- Todos os usuários do sistema têm senhas que são utilizadas para validação do respectivo login.

## Histórias de Usuário

### 1. Geração e Manutenção de Currículo
**Como Secretária**,  
preciso gerar um currículo para cada semestre e manter as informações sobre as disciplinas, professores e alunos,  
**para que os alunos possam se matricular nas disciplinas corretas.**

### 2. Matrícula em Disciplinas
**Como Aluno**,  
preciso me matricular em 4 disciplinas como 1º opção e em mais 2 outras optativas,  
**para que eu possa cursar as disciplinas necessárias para meu curso.**

### 3. Cancelamento de Matrícula
**Como Aluno**,  
preciso cancelar matrícula em um determinado período,  
**para ajustar minha grade curricular conforme necessário.**

### 4. Desativação de Disciplinas com Baixa Matrícula
**Como Secretária**,  
gostaria de desativar uma disciplina caso ela tenha menos de 3 matrículas ao final do semestre,  
**para abrir espaço para outras disciplinas.**

### 5. Encerramento de Matrículas por Capacidade
**Como Secretária**,  
gostaria de encerrar matrículas para uma disciplina caso esta alcance o limite máximo de 60,  
**para não exceder a capacidade máxima.**

### 6. Cobrança pela Matrícula
**Como Aluno**,  
gostaria de ser cobrado pelo Sistema de Cobranças pela disciplina na qual me matriculei,  
**para poder pagar a tempo.**

### 7. Notificação ao Sistema de Cobranças
**Como sistema**,  
gostaria de notificar o Sistema de Cobranças para realizar a cobrança do Aluno matriculado,  
**para que os alunos possam ser cobrados pelas disciplinas nas quais estão matriculados.**

### 8. Consulta de Matrículas por Professores
**Como Professor**,  
preciso acessar o Sistema para saber quais alunos estão matriculados em minha disciplina,  
**para que eu possa saber quem está inscrito nas minhas aulas.**

### 9. Cadastro de Alunos e Professores
**Como Secretária**,  
quero cadastrar alunos e professores no sistema,  
**para que eles possam acessar e utilizar o sistema de matrículas.**
