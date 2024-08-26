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
        
        #Frame
        selecao_frame = ctk.CTkFrame(master=app, width=250, height=300)
        selecao_frame.place(x=230, y=90)
        
        #Texto
        titulo = ctk.CTkLabel(master=selecao_frame, text="Selecione o tipo de usuário", font=("Arial", 18)).place(x=20, y=15)
        
        #Botoes
        def TelaLoginSecretaria():
        
            #Apagar frame anterior
            selecao_frame.place_forget()
            
            #Frame
            loginSecretaria_frame = ctk.CTkFrame(master=app, width=300, height=500)
            loginSecretaria_frame.pack(expand=True, side="right", fill="both")
            
            imgLoginSecretaria = ctk.CTkLabel(master=app, text="" ,image=imgLogin)
            imgLoginSecretaria.pack(expand=True, side="left")
            
            ctk.CTkLabel(master=loginSecretaria_frame, text="Bem Vindo!", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
            ctk.CTkLabel(master=loginSecretaria_frame, text="Sign in to your account", text_color="#7E7E7E", anchor="w", justify="left", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))
            
            ctk.CTkLabel(master=loginSecretaria_frame, text="  Email:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
            ctk.CTkEntry(master=loginSecretaria_frame, width=300, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000").pack(anchor="w", padx=(25, 0))

            ctk.CTkLabel(master=loginSecretaria_frame, text="  Password:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
            ctk.CTkEntry(master=loginSecretaria_frame, width=300, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", show="*").pack(anchor="w", padx=(25, 0))

            ctk.CTkButton(master=loginSecretaria_frame, text="Login", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=300).pack(anchor="w", pady=(40, 0), padx=(25, 0))
            
        btn_secretaria = ctk.CTkButton(master=selecao_frame, text="Secretaria", command=TelaLoginSecretaria, width=230, height=50, corner_radius=30).place(x=10, y=70)
        
        def TelaAluno():
            pass
        
        btn_aluno = ctk.CTkButton(master=selecao_frame, text="Aluno", command=TelaAluno, width=230, height=50, corner_radius=30).place(x=10, y=130)
        
        def TelaProfessor():
            pass
        
        btn_professor = ctk.CTkButton(master=selecao_frame, text="Professor", command=TelaProfessor, width=230, height=50, corner_radius=30).place(x=10, y=190)
    
Main()