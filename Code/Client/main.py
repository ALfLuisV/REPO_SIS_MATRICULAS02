import customtkinter as ctk
from PIL import Image
from Classes.Usuarios.login import Login
from Classes.Usuarios.secretario import Secretario


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
        
        self.email_var = ctk.StringVar()
        emailLabel = ctk.CTkLabel(master=login_frame, text="  Email:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
        emailInput = ctk.CTkEntry(master=login_frame, width=300, height=40, fg_color="#EEEEEE", border_color="#601E88", border_width=1.5, text_color="#000000", corner_radius=30, textvariable=self.email_var).pack(anchor="w", padx=(25, 0))

        self.senha_var = ctk.StringVar()
        senhaLabel = ctk.CTkLabel(master=login_frame, text="  Password:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
        senhaInput = ctk.CTkEntry(master=login_frame, width=300, height=40, fg_color="#EEEEEE", border_color="#601E88", border_width=1.5, text_color="#000000", show="*", corner_radius=30, textvariable=self.senha_var).pack(anchor="w", padx=(25, 0))

        btnLogin = ctk.CTkButton(master=login_frame, text="Login", fg_color="#601E88", hover_color="#601E65", font=("Arial Bold", 18), text_color="#ffffff", width=300, height=50, command=lambda: self.logar(usuario_tipo), corner_radius=30).pack(anchor="w", pady=(50, 0), padx=(25, 0))
        btnVoltar = ctk.CTkButton(master=login_frame, text="Voltar", command=self.TelaSelecao, fg_color="#601E88", hover_color="#601E65", font=("Arial Bold", 14), text_color="#ffffff", width=50, height=30, corner_radius=30).pack(anchor="w", pady=(30, 0), padx=(255, 0))

    
    def logar(self, usuario_tipo):
        email = self.email_var.get()
        senha = self.senha_var.get()

        login_obj = Login()
        usuario = login_obj.logar_sistema(email, senha)

        if usuario:
            print(f"Login realizado com sucesso para {usuario_tipo}")
            if usuario_tipo == "Secretario(a)":
                self.TelaSecretaria()
            elif usuario_tipo == "Aluno(a)":
                self.TelaAluno()
            elif usuario_tipo == "Professor(a)":
                self.TelaProfessor()
        else:
            print("Email ou senha incorretos!")
            # Aqui você pode adicionar uma notificação na UI para informar o usuário do erro
    
    
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
        tab_view = ctk.CTkTabview(master=app)
        tab_view.pack(padx=(20), pady=(20), expand=True, fill="both")

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
        secretariaDisciplinas_frame = ctk.CTkScrollableFrame(master=dashboard_frame, width=150, height=500)
        secretariaDisciplinas_frame.grid(row=0, column=1, rowspan=2, sticky="nsew", padx=(20, 20), pady=(20, 20))

        # Frame para Professores
        secretariaProfessores_frame = ctk.CTkScrollableFrame(master=dashboard_frame, width=150, height=250)
        secretariaProfessores_frame.grid(row=0, column=0, sticky="nsew", padx=(20, 20), pady=(20, 20))

        # Frame para Alunos
        secretariaAlunos_frame = ctk.CTkScrollableFrame(master=dashboard_frame, width=150, height=250)
        secretariaAlunos_frame.grid(row=1, column=0, sticky="nsew", padx=(20, 20), pady=(20, 20))

        # Labels
        ctk.CTkLabel(master=secretariaDisciplinas_frame, text="Disciplinas", font=("Arial Bold", 20)).pack(pady=20, padx=(40,0), side="left")
        ctk.CTkLabel(master=secretariaProfessores_frame, text="Professores", font=("Arial Bold", 20)).pack(pady=20, padx=(40,0), side="left")
        ctk.CTkLabel(master=secretariaAlunos_frame, text="Alunos", font=("Arial Bold", 20)).pack(pady=20, padx=(40,0), side="left")
        
        # Botões
        btnCadastrarDisciplina = ctk.CTkButton(master=secretariaDisciplinas_frame, text="Novo", fg_color="#601E88", hover_color="#601E65", font=("Arial", 14), width=30, height=25, corner_radius=30).pack(pady=20, padx=(0,40), side="right")
        btnCadastrarProfessor = ctk.CTkButton(master=secretariaProfessores_frame, text="Novo", fg_color="#601E88", hover_color="#601E65", font=("Arial", 14), width=30, height=25, corner_radius=30).pack(pady=20, padx=(0,40), side="right")
        btnCadastrarAluno = ctk.CTkButton(master=secretariaAlunos_frame, text="Novo", fg_color="#601E88", hover_color="#601E65", font=("Arial", 14), width=30, height=25, corner_radius=30).pack(pady=20, padx=(0,40), side="right")

        # ===================== Conteúdo da aba Gerência =====================
        
        gerencia_frame = tab_view.tab("Gerência")
        
        # Configurando a grade no gerencia_frame (aqui você pode adicionar o conteúdo específico de Gerência)
        gerencia_frame.grid_columnconfigure(0, weight=1)
        gerencia_frame.grid_columnconfigure(1, weight=1)
        gerencia_frame.grid_rowconfigure(0, weight=1)
        gerencia_frame.grid_rowconfigure(1, weight=1)

        # Exemplo de conteúdo na aba Gerência (você pode modificar conforme necessário)
        ctk.CTkLabel(master=gerencia_frame, text="Gerenciamento de Recursos", font=("Arial Bold", 20)).grid(row=0, column=0, columnspan=2, pady=(20, 20))

        # Outros frames e widgets relacionados à Gerência podem ser adicionados aqui

        
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


# instanciar secretario sec1
# sec1 = Secretario(32, "Davi", "31999999999", "davi@gmail.com", "Manhã")
# sec1.cadastrar_aluno()

Main()
