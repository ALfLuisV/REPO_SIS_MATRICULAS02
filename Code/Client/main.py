import customtkinter as ctk
from PIL import Image

imgLoginPIL = Image.open("Code/assets/Login-amico.png")
imgLogin = ctk.CTkImage(light_image=imgLoginPIL, size=(300, 500))

app = ctk.CTk()

class Main:
    def __init__(self):
        self.app = app
        self.tela()
        self.TelaSelecao()
        app.mainloop()

    def tela(self):
        # Criando a janela
        app.title("TechMatriculas")
        app.geometry("700x500")
        ctk.set_appearance_mode("dark")
        
    def TelaSelecao(self):
        # Esconde todos os frames atuais
        for widget in app.winfo_children():
            # widget.destroy()
            widget.pack_forget()
            widget.place_forget()
            widget.grid_forget()
        
        # Frame
        selecao_frame = ctk.CTkFrame(master=app, width=250, height=300, border_color="#601E88", border_width=2, corner_radius=30)
        selecao_frame.place(x=230, y=90)
        
        # Texto
        titulo = ctk.CTkLabel(master=selecao_frame, text="Selecione o tipo de Usuário", font=("Arial Bold", 18)).place(x=20, y=15)
        
        # Botões
        btn_secretaria = ctk.CTkButton(master=selecao_frame, text="Secretaria", fg_color="#601E88", hover_color="#601E65", font=("Arial Bold", 14), command=self.TelaLoginSecretaria, width=230, height=50, corner_radius=30).place(x=10, y=70)
        btn_aluno = ctk.CTkButton(master=selecao_frame, text="Aluno", fg_color="#601E88", hover_color="#601E65", font=("Arial Bold", 14), command=self.TelaLoginAluno, width=230, height=50, corner_radius=30).place(x=10, y=130)
        btn_professor = ctk.CTkButton(master=selecao_frame, text="Professor", fg_color="#601E88", hover_color="#601E65", font=("Arial Bold", 14), command=self.TelaLoginProfessor, width=230, height=50, corner_radius=30).place(x=10, y=190)

    def TelaLogin(self, usuario_tipo):
        # Esconde todos os frames atuais
        for widget in app.winfo_children():
            # widget.destroy()
            widget.pack_forget()
            widget.place_forget()
            widget.grid_forget()
        
        # Frame para o login
        login_frame = ctk.CTkFrame(master=app, width=300, height=500)
        login_frame.pack(expand=True, side="right", fill="both")
        
        imgTelaLogin = ctk.CTkLabel(master=app, text="" ,image=imgLogin)
        imgTelaLogin.pack(expand=True, side="left")
        
        titulo = ctk.CTkLabel(master=login_frame, text=f"Bem Vindo, {usuario_tipo}!", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 15), padx=(25, 0))
        
        subTitulo = ctk.CTkLabel(master=login_frame, text="Por Favor Insira Suas Credenciais De Acesso", text_color="#fff", anchor="w", justify="left", font=("Arial Bold", 14)).pack(anchor="w", padx=(25, 0))
        
        emailLabel = ctk.CTkLabel(master=login_frame, text="  Email:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
        
        emailInput = ctk.CTkEntry(master=login_frame, width=300, height=40, fg_color="#EEEEEE", border_color="#601E88", border_width=1.5, text_color="#000000", corner_radius=30).pack(anchor="w", padx=(25, 0))

        senhaLabel = ctk.CTkLabel(master=login_frame, text="  Password:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
        
        senhaInput = ctk.CTkEntry(master=login_frame, width=300, height=40, fg_color="#EEEEEE", border_color="#601E88", border_width=1.5, text_color="#000000", show="*", corner_radius=30).pack(anchor="w", padx=(25, 0))

        btnLogin = ctk.CTkButton(master=login_frame, text="Login", fg_color="#601E88", hover_color="#601E65", font=("Arial Bold", 18), text_color="#ffffff", width=300, height=50, command=lambda: self.ProximaTela(usuario_tipo), corner_radius=30).pack(anchor="w", pady=(50, 0), padx=(25, 0))
        
        btnVoltar = ctk.CTkButton(master=login_frame, text="Voltar", command=self.TelaSelecao, fg_color="#601E88", hover_color="#601E65", font=("Arial Bold", 14), text_color="#ffffff", width=50, height=30, corner_radius=30).pack(anchor="w", pady=(30, 0), padx=(255, 0))

    def TelaLoginSecretaria(self):
        self.TelaLogin("Secretario(a)")

    def TelaLoginAluno(self):
        self.TelaLogin("Aluno(a)")

    def TelaLoginProfessor(self):
        self.TelaLogin("Professor(a)")
        
    def TelaSecretaria(self):
        # Esconde todos os frames atuais
        for widget in app.winfo_children():
            widget.pack_forget()
            widget.place_forget()
            widget.grid_forget()
        
        # Adiciona um TabView para as abas Dashboard e Gerência
        tab_view = ctk.CTkTabview(master=app, width=700, height=500,segmented_button_selected_color= "#601E88", segmented_button_selected_hover_color= "#601E65", corner_radius=30)
        tab_view.pack(expand=True, fill="both")

        # Cria a aba Dashboard
        tab_view.add("Dashboard")
        
        # Cria a aba Gerência
        tab_view.add("Gerência")

        # Define a aba "Dashboard" como a aba inicial aberta
        tab_view.set("Dashboard")
        
        # ===================== Conteúdo da aba Dashboard =====================
        
        dashboard_frame = tab_view.tab("Dashboard")
        
        # Configurando a grade no dashboard_frame
        dashboard_frame.grid_columnconfigure(0, weight=1)
        dashboard_frame.grid_columnconfigure(1, weight=1)
        dashboard_frame.grid_rowconfigure(0, weight=1)
        dashboard_frame.grid_rowconfigure(1, weight=1)

        # Frame para Disciplinas (cobre as duas colunas na primeira linha)
        secretariaDisciplinas_frame = ctk.CTkScrollableFrame(master=dashboard_frame, width=150, height=500, border_width=2, border_color="#601E88", corner_radius=30)
        secretariaDisciplinas_frame.grid(row=0, column=1, rowspan=2, sticky="nsew", padx=(20, 0))

        # Frame para Professores
        secretariaProfessores_frame = ctk.CTkScrollableFrame(master=dashboard_frame, width=150, height=250, border_width=2, border_color="#601E88", corner_radius=30)
        secretariaProfessores_frame.grid(row=0, column=0, sticky="nsew", pady=(0, 15))

        # Frame para Alunos
        secretariaAlunos_frame = ctk.CTkScrollableFrame(master=dashboard_frame, width=150, height=250, border_width=2, border_color="#601E88", corner_radius=30)
        secretariaAlunos_frame.grid(row=1, column=0, sticky="nsew")

        # Labels
        ctk.CTkLabel(master=secretariaDisciplinas_frame, text="Disciplinas", font=("Arial Bold", 20)).pack(padx=(20))
        ctk.CTkLabel(master=secretariaProfessores_frame, text="Professores", font=("Arial Bold", 20)).pack(padx=(20))
        ctk.CTkLabel(master=secretariaAlunos_frame, text="Alunos", font=("Arial Bold", 20)).pack(padx=(20))
        
        
        # ===================== Conteúdo da aba Gerência =====================
        
        gerencia_frame = tab_view.tab("Gerência")
        
        # Configurando a grade no gerencia_frame
        gerencia_frame.grid_columnconfigure(0, weight=1)
        gerencia_frame.grid_columnconfigure(1, weight=1)  # Aumenta o espaço para o conteúdo de cadastro ou listagem
        gerencia_frame.grid_rowconfigure(0, weight=1)
        gerencia_frame.grid_rowconfigure(1, weight=1)
        gerencia_frame.grid_rowconfigure(2, weight=1)
        
        # Frames para Gerenciamento
        gerencia_disciplinas_frame = ctk.CTkFrame(master=gerencia_frame, height=166)
        gerencia_disciplinas_frame.grid(row=0, column=0, sticky="nsew")
        
        gerencia_professores_frame = ctk.CTkFrame(master=gerencia_frame, height=166)
        gerencia_professores_frame.grid(row=1, column=0, sticky="nsew")
        
        gerencia_alunos_frame = ctk.CTkFrame(master=gerencia_frame, height=166)
        gerencia_alunos_frame.grid(row=2, column=0, sticky="nsew")

        # Labels para identificar cada seção
        ctk.CTkLabel(master=gerencia_disciplinas_frame, text="Gerenciamento de Disciplinas", font=("Arial Bold", 20)).pack()
        ctk.CTkLabel(master=gerencia_professores_frame, text="Gerenciamento de Professores", font=("Arial Bold", 20)).pack()
        ctk.CTkLabel(master=gerencia_alunos_frame, text="Gerenciamento de Alunos", font=("Arial Bold", 20)).pack()

        # Botões para Gerenciamento de Disciplinas
        btnGerenciaDisciplinaCadastro = ctk.CTkButton(master=gerencia_disciplinas_frame, text="Cadastro", fg_color="#601E88", hover_color="#601E65", font=("Arial", 14), width=150, height=30, corner_radius=30, command= self.TelaCadastroDisciplina)
        btnGerenciaDisciplinaListagem = ctk.CTkButton(master=gerencia_disciplinas_frame, text="Listagem", fg_color="#601E88", hover_color="#601E65", font=("Arial", 14), width=150, height=30, corner_radius=30, command=lambda: mostrar_listagem("Disciplinas"))
        btnGerarCurriculo = ctk.CTkButton(master=gerencia_disciplinas_frame, text="Gerar Currículo", fg_color="#601E88", hover_color="#601E65", font=("Arial", 14), width=150, height=30, corner_radius=30, command=self.GerarCurriculo)
        btnGerenciaDisciplinaCadastro.pack(pady=(15, 5))
        btnGerenciaDisciplinaListagem.pack(pady=(5, 5))
        btnGerarCurriculo.pack(pady=(5, 5))
        
        # Botões para Gerenciamento de Professores
        btnGerenciaProfessorCadastro = ctk.CTkButton(master=gerencia_professores_frame, text="Cadastro", fg_color="#601E88", hover_color="#601E65", font=("Arial", 14), width=150, height=30, corner_radius=30, command= self.TelaCadastroProfessor)
        btnGerenciaProfessorListagem = ctk.CTkButton(master=gerencia_professores_frame, text="Listagem", fg_color="#601E88", hover_color="#601E65", font=("Arial", 14), width=150, height=30, corner_radius=30, command=lambda: mostrar_listagem("Professores"))
        btnGerenciaProfessorCadastro.pack(pady=(15, 5))
        btnGerenciaProfessorListagem.pack(pady=(5, 15))
        
        # Botões para Gerenciamento de Alunos
        btnGerenciaAlunoCadastro = ctk.CTkButton(master=gerencia_alunos_frame, text="Cadastro", fg_color="#601E88", hover_color="#601E65", font=("Arial", 14), width=150, height=30, corner_radius=30, command= self.TelaCadastroAluno)
        btnGerenciaAlunoListagem = ctk.CTkButton(master=gerencia_alunos_frame, text="Listagem", fg_color="#601E88", hover_color="#601E65", font=("Arial", 14), width=150, height=30, corner_radius=30, command=lambda: mostrar_listagem("Alunos"))
        btnGerenciaAlunoCadastro.pack(pady=(15, 5))
        btnGerenciaAlunoListagem.pack(pady=(5, 15))
        
        gerencia_conteudo_frame = ctk.CTkFrame(master=gerencia_frame, border_width=2, border_color="#601E88", corner_radius=30)
        gerencia_conteudo_frame.grid(row=0, column=1, rowspan=3, sticky="nsew")
        
        ctk.CTkLabel(master=gerencia_conteudo_frame, text="Tenha Um Bom Dia !!", font=("Arial Bold", 20)).pack(pady=50)
        ctk.CTkLabel(master=gerencia_conteudo_frame, text="😊", font=("Arial Bold", 50)).pack(pady=50)
    
    
    def TelaCadastroAluno(self):
        
        # Esconde todos os frames atuais
        for widget in app.winfo_children():
            # widget.destroy()
            widget.pack_forget()
            widget.place_forget()
            widget.grid_forget()
        
        # Frame para o Cadastro
        cadastro_frame = ctk.CTkFrame(master=app, width=300, height=500)
        cadastro_frame.pack(expand=True, side="right", fill="both")
        
        imgTelaLogin = ctk.CTkLabel(master=app, text="" ,image=imgLogin)
        imgTelaLogin.pack(expand=True, side="left")
        
        titulo = ctk.CTkLabel(master=cadastro_frame, text=f"Cadastrar Novo Aluno", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(20, 15), padx=(25, 0))
        
        subTitulo = ctk.CTkLabel(master=cadastro_frame, text="Por Favor Preencha Os Campos", text_color="#fff", anchor="w", justify="left", font=("Arial Bold", 14)).pack(anchor="w", padx=(25, 0))
        
        nomeLabel = ctk.CTkLabel(master=cadastro_frame, text="  Nome:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), compound="left").pack(anchor="w", pady=(20, 0), padx=(25, 0))
        
        nomeInput = ctk.CTkEntry(master=cadastro_frame, width=300, height=40, fg_color="#EEEEEE", border_color="#601E88", border_width=1.5, text_color="#000000", corner_radius=30).pack(anchor="w", padx=(25, 0))

        emailLabel = ctk.CTkLabel(master=cadastro_frame, text="  Email:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), compound="left").pack(anchor="w", pady=(20, 0), padx=(25, 0))
        
        emailInput = ctk.CTkEntry(master=cadastro_frame, width=300, height=40, fg_color="#EEEEEE", border_color="#601E88", border_width=1.5, text_color="#000000", corner_radius=30).pack(anchor="w", padx=(25, 0))

        telLabel = ctk.CTkLabel(master=cadastro_frame, text="  Telefone:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), compound="left").pack(anchor="w", pady=(20, 0), padx=(25, 0))
        
        telInput = ctk.CTkEntry(master=cadastro_frame, width=300, height=40, fg_color="#EEEEEE", border_color="#601E88", border_width=1.5, text_color="#000000", corner_radius=30).pack(anchor="w", padx=(25, 0))
        
        btnCadastro = ctk.CTkButton(master=cadastro_frame, text="Cadastrar", fg_color="#601E88", hover_color="#601E65", font=("Arial Bold", 18), text_color="#ffffff", width=300, height=50, command= self.TelaSecretaria, corner_radius=30).pack(anchor="w", pady=(20, 0), padx=(25, 0))
        
        btnVoltar = ctk.CTkButton(master=cadastro_frame, text="Voltar", command=self.TelaSecretaria, fg_color="#601E88", hover_color="#601E65", font=("Arial Bold", 14), text_color="#ffffff", width=50, height=30, corner_radius=30).pack(anchor="w", pady=(20, 0), padx=(255, 0))

    def salvar_aluno(self, nome, idade, curso):
        # Aqui você pode implementar a lógica para salvar os dados do aluno
        print(f"Aluno cadastrado: Nome={nome}, Idade={idade}, Curso={curso}")
        
    def TelaCadastroProfessor(self):
        
        # Esconde todos os frames atuais
        for widget in app.winfo_children():
            # widget.destroy()
            widget.pack_forget()
            widget.place_forget()
            widget.grid_forget()
        
        # Frame para o Cadastro
        cadastro_frame = ctk.CTkFrame(master=app, width=300, height=500)
        cadastro_frame.pack(expand=True, side="right", fill="both")
        
        imgTelaLogin = ctk.CTkLabel(master=app, text="" ,image=imgLogin)
        imgTelaLogin.pack(expand=True, side="left")
        
        titulo = ctk.CTkLabel(master=cadastro_frame, text=f"Cadastrar Novo Professor", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(20, 15), padx=(25, 0))
        
        subTitulo = ctk.CTkLabel(master=cadastro_frame, text="Por Favor Preencha Os Campos", text_color="#fff", anchor="w", justify="left", font=("Arial Bold", 14)).pack(anchor="w", padx=(25, 0))
        
        nomeLabel = ctk.CTkLabel(master=cadastro_frame, text="  Nome:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), compound="left").pack(anchor="w", pady=(10, 0), padx=(25, 0))
        
        nomeInput = ctk.CTkEntry(master=cadastro_frame, width=300, height=30, fg_color="#EEEEEE", border_color="#601E88", border_width=1.5, text_color="#000000", corner_radius=30).pack(anchor="w", padx=(25, 0))

        emailLabel = ctk.CTkLabel(master=cadastro_frame, text="  Email:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), compound="left").pack(anchor="w", pady=(10, 0), padx=(25, 0))
        
        emailInput = ctk.CTkEntry(master=cadastro_frame, width=300, height=30, fg_color="#EEEEEE", border_color="#601E88", border_width=1.5, text_color="#000000", corner_radius=30).pack(anchor="w", padx=(25, 0))

        telLabel = ctk.CTkLabel(master=cadastro_frame, text="  Telefone:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), compound="left").pack(anchor="w", pady=(10, 0), padx=(25, 0))
        
        telInput = ctk.CTkEntry(master=cadastro_frame, width=300, height=30, fg_color="#EEEEEE", border_color="#601E88", border_width=1.5, text_color="#000000", corner_radius=30).pack(anchor="w", padx=(25, 0))
        
        salarioLabel = ctk.CTkLabel(master=cadastro_frame, text="  Salário:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), compound="left").pack(anchor="w", pady=(10, 0), padx=(25, 0))
        
        salarioInput = ctk.CTkEntry(master=cadastro_frame, width=300, height=30, fg_color="#EEEEEE", border_color="#601E88", border_width=1.5, text_color="#000000", corner_radius=30).pack(anchor="w", padx=(25, 0))
        
        
        btnCadastro = ctk.CTkButton(master=cadastro_frame, text="Cadastrar", fg_color="#601E88", hover_color="#601E65", font=("Arial Bold", 18), text_color="#ffffff", width=300, height=50, command= self.TelaSecretaria, corner_radius=30).pack(anchor="w", pady=(10, 0), padx=(25, 0))
        
        btnVoltar = ctk.CTkButton(master=cadastro_frame, text="Voltar", command=self.TelaSecretaria, fg_color="#601E88", hover_color="#601E65", font=("Arial Bold", 14), text_color="#ffffff", width=50, height=30, corner_radius=30).pack(anchor="w", pady=(10, 0), padx=(255, 0))

    def TelaCadastroDisciplina(self):
        
        # Esconde todos os frames atuais
        for widget in app.winfo_children():
            # widget.destroy()
            widget.pack_forget()
            widget.place_forget()
            widget.grid_forget()
        
        # Frame para o Cadastro
        cadastro_frame = ctk.CTkFrame(master=app, width=300, height=500)
        cadastro_frame.pack(expand=True, side="right", fill="both")
        
        imgTelaLogin = ctk.CTkLabel(master=app, text="" ,image=imgLogin)
        imgTelaLogin.pack(expand=True, side="left")
        
        titulo = ctk.CTkLabel(master=cadastro_frame, text=f"Cadastrar Nova Disciplina", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(20, 15), padx=(25, 0))
        
        subTitulo = ctk.CTkLabel(master=cadastro_frame, text="Por Favor Preencha Os Campos", text_color="#fff", anchor="w", justify="left", font=("Arial Bold", 14)).pack(anchor="w", padx=(25, 0))
        
        nomeLabel = ctk.CTkLabel(master=cadastro_frame, text="  Nome:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), compound="left").pack(anchor="w", pady=(20, 0), padx=(25, 0))
        
        nomeInput = ctk.CTkEntry(master=cadastro_frame, width=300, height=40, fg_color="#EEEEEE", border_color="#601E88", border_width=1.5, text_color="#000000", corner_radius=30).pack(anchor="w", padx=(25, 0))

        periodoLabel = ctk.CTkLabel(master=cadastro_frame, text="  Periodo:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), compound="left").pack(anchor="w", pady=(20, 0), padx=(25, 0))
        
        periodoInput = ctk.CTkEntry(master=cadastro_frame, width=300, height=40, fg_color="#EEEEEE", border_color="#601E88", border_width=1.5, text_color="#000000", corner_radius=30).pack(anchor="w", padx=(25, 0))
        
        btnCadastro = ctk.CTkButton(master=cadastro_frame, text="Cadastrar", fg_color="#601E88", hover_color="#601E65", font=("Arial Bold", 18), text_color="#ffffff", width=300, height=50, command= self.TelaSecretaria, corner_radius=30).pack(anchor="w", pady=(50, 0), padx=(25, 0))
        
        btnVoltar = ctk.CTkButton(master=cadastro_frame, text="Voltar", command=self.TelaSecretaria, fg_color="#601E88", hover_color="#601E65", font=("Arial Bold", 14), text_color="#ffffff", width=50, height=30, corner_radius=30).pack(anchor="w", pady=(20, 0), padx=(255, 0))
    
    def ExcluirDisciplina(self):
        pass
    
    def GerarCurriculo(self):
        pass
    
    def TelaAluno(self):
        # Esconde todos os frames atuais
        for widget in app.winfo_children():
            # widget.destroy()
            widget.pack_forget()
            widget.place_forget()
            widget.grid_forget()
        
        #Frame
        alunoDisciplinas_frame = ctk.CTkScrollableFrame(master=app, width=150, height=500)
        alunoDisciplinas_frame.pack(expand=True, side="right", fill="both", padx=(20, 20), pady=(20, 20))
        
        alunoMatriculas_frame = ctk.CTkScrollableFrame(master=app, width=150, height=500)
        alunoMatriculas_frame.pack(expand=True, side="left", fill="both", padx=(20, 20), pady=(20, 20))
        
        titulo1 = ctk.CTkLabel(master=alunoDisciplinas_frame, text="Disciplinas", font=("Arial Bold", 20)).pack(pady=20)
        titulo2 = ctk.CTkLabel(master=alunoMatriculas_frame, text="Minhas Matriculas", font=("Arial Bold", 20)).pack(pady=20)
        
    def TelaProfessor(self):
        # Esconde todos os frames atuais
        for widget in app.winfo_children():
            # widget.destroy()
            widget.pack_forget()
            widget.place_forget()
            widget.grid_forget()
            
        #Frames
        professorDisciplina_frame = ctk.CTkScrollableFrame(master=app, width=150, height=500)
        professorDisciplina_frame.pack(expand=True, side="left", fill="both", padx=(20, 20), pady=(20, 20))
        
        professorAlunos_frame = ctk.CTkScrollableFrame(master=app, width=150, height=500)
        professorAlunos_frame.pack(expand=True, side="right", fill="both", padx=(20, 20), pady=(20, 20))
        
        titulo1 = ctk.CTkLabel(master=professorDisciplina_frame, text="Disciplinas", font=("Arial Bold", 20)).pack(pady=20)
        titulo2 = ctk.CTkLabel(master=professorAlunos_frame, text="Alunos", font=("Arial Bold", 20)).pack(pady=20)
        
    
    def ProximaTela(self, usuario_tipo):
        # Esconde todos os frames atuais
        for widget in app.winfo_children():
            # widget.destroy()
            widget.pack_forget()
            widget.place_forget()
            widget.grid_forget()
        
        if usuario_tipo == "Secretario(a)":
            self.TelaSecretaria()
        elif usuario_tipo == "Aluno(a)":
            self.TelaAluno()
        elif usuario_tipo == "Professor(a)":
            self.TelaProfessor()

Main()