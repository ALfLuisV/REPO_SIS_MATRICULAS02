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
        
    def TelaSelecao(self):
        # Esconde todos os frames atuais
        for widget in app.winfo_children():
            # widget.destroy()
            widget.pack_forget()
            widget.place_forget()
            widget.grid_forget()
        
        # Frame
        selecao_frame = ctk.CTkFrame(master=app, width=250, height=300)
        selecao_frame.place(x=230, y=90)
        
        # Texto
        titulo = ctk.CTkLabel(master=selecao_frame, text="Selecione o tipo de usuário", font=("Arial", 18)).place(x=20, y=15)
        
        # Botões
        btn_secretaria = ctk.CTkButton(master=selecao_frame, text="Secretaria", command=self.TelaLoginSecretaria, width=230, height=50, corner_radius=30).place(x=10, y=70)
        btn_aluno = ctk.CTkButton(master=selecao_frame, text="Aluno", command=self.TelaLoginAluno, width=230, height=50, corner_radius=30).place(x=10, y=130)
        btn_professor = ctk.CTkButton(master=selecao_frame, text="Professor", command=self.TelaLoginProfessor, width=230, height=50, corner_radius=30).place(x=10, y=190)

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
            # widget.destroy()
            widget.pack_forget()
            widget.place_forget()
            widget.grid_forget()
        
        ctk.CTkLabel(master=app, text="Tela Principal - Secretaria", font=("Arial", 24)).pack(pady=20)
    
    def TelaAluno(self):
        # Esconde todos os frames atuais
        for widget in app.winfo_children():
            # widget.destroy()
            widget.pack_forget()
            widget.place_forget()
            widget.grid_forget()
        
        ctk.CTkLabel(master=app, text="Tela Principal - Aluno", font=("Arial", 24)).pack(pady=20)
        
    def TelaProfessor(self):
        # Esconde todos os frames atuais
        for widget in app.winfo_children():
            # widget.destroy()
            widget.pack_forget()
            widget.place_forget()
            widget.grid_forget()
            
        professorDisciplina_frame = ctk.CTkScrollableFrame(master=app, width=150, height=500)
        professorDisciplina_frame.pack(expand=True, side="left", fill="both", padx=(20, 20), pady=(20, 20))
        
        professorAlunos_frame = ctk.CTkScrollableFrame(master=app, width=150, height=500)
        professorAlunos_frame.pack(expand=True, side="right", fill="both", padx=(20, 20), pady=(20, 20))
        
        ctk.CTkLabel(master=professorDisciplina_frame, text="Disciplinas", font=("Arial Bold", 20)).pack(pady=20)
        ctk.CTkLabel(master=professorAlunos_frame, text="Alunos", font=("Arial Bold", 20)).pack(pady=20)
        
        
    
    def ProximaTela(self, usuario_tipo):
        # Esconde todos os frames atuais
        for widget in app.winfo_children():
            # widget.destroy()
            widget.pack_forget()
            widget.place_forget()
            widget.grid_forget()
        
        if usuario_tipo == "Secretario(a)":
            ctk.CTkLabel(master=app, text="Tela Principal - Secretario", font=("Arial", 24)).pack(pady=20)
        elif usuario_tipo == "Aluno(a)":
            ctk.CTkLabel(master=app, text="Tela Principal - Aluno", font=("Arial", 24)).pack(pady=20)
        elif usuario_tipo == "Professor(a)":
            self.TelaProfessor()

Main()