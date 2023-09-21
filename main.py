import customtkinter as ctk
from tkinter import *

app = ctk.CTk()
# Defina as dimensões da janela principal
width = 1000
height = 600

# Obtenha as dimensões da tela
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

# Calcule as coordenadas x e y para centralizar a janela
x = (screen_width - width) // 2
y = (screen_height - height) // 3

# Configure a geometria da janela principal para centralizá-la
app.geometry(f"{width}x{height}+{x}+{y}")

# Configure outras propriedades da janela, se necessário
app.title("Bem-vindo ao Avalia Prof!")
app.resizable(True, True)
app._set_appearance_mode('dark')

#CRIAÇÃO DAS TELAS-FRAMES
FirstFrameScreen = ctk.CTkFrame(app, fg_color="#2D1E1E")
SecondFrameScreen = ctk.CTkFrame(app, fg_color="#2D1E1E")
TerceiroFrameScreen = ctk.CTkFrame(app, fg_color="#2D1E1E")
QuartoFrame = ctk.CTkFrame(app, fg_color="#2D1E1E")

#TELA PRINCIPAL
def telaPrincipal():
    FirstFrameScreen.place_configure(relx=0, rely=0, relwidth=1, relheight=1)
    SecondFrameScreen.place_forget()
    TerceiroFrameScreen.place_forget()
    QuartoFrame.place_forget()

    #CONTEÚDO DO FRAME:
    lb_title = ctk.CTkLabel(FirstFrameScreen, text="Avalia Prof", font=('Arial', 40, 'bold'), text_color="#1C89DC", fg_color="#2D1E1E").place_configure(relx=0.4, rely=0.1)

    lb_inst = ctk.CTkLabel(FirstFrameScreen, text="Selecione as opções:", font=('Arial', 20), text_color="#A5A5A5", fg_color="#2D1E1E").place_configure(relx=0.4, rely=0.25)

#TELA DE CARTÃO RESPOSTA
def telaCartaoResp():
    SecondFrameScreen.place_configure(relx=0, rely=0, relwidth=1, relheight=1)
    FirstFrameScreen.place_forget()

    #CONTEÚDO DO FRAME:
    CrFrame = ctk.CTkFrame(SecondFrameScreen).place_configure(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.6)

    lb_title_CR = ctk.CTkLabel(SecondFrameScreen, text="Avalia Prof", font=('Arial', 40, 'bold'), text_color="#1C89DC").place_configure(relx=0.4, rely=0.1)
    
    btn_return_CR = ctk.CTkButton(SecondFrameScreen, text="Voltar", font=('Arial', 20, 'bold'), command=telaPrincipal).place_configure(relx=0.1, rely=0.12)

#TELA DE CORRIGIR PROVA
def telaCorrigir():
    TerceiroFrameScreen.place_configure(relx=0, rely=0, relwidth=1, relheight=1)
    FirstFrameScreen.place_forget()
    
    #CONTEÚDO DO FRAME:
    CorFrame = ctk.CTkFrame(TerceiroFrameScreen).place_configure(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.6)

    lb_title_CP = ctk.CTkLabel(TerceiroFrameScreen, text="Avalia Prof", font=('Arial', 40, 'bold'), text_color="#1C89DC", fg_color="#2D1E1E").place_configure(relx=0.4, rely=0.1)

    lb_subtitle_CP = ctk.CTkLabel(TerceiroFrameScreen, text="Posicione a câmera dentro da marcação", font=('Arial', 20), text_color="#A5A5A5", fg_color="#2D1E1E").place_configure(relx=0.32, rely=0.2)
    
    btn_return_CP = ctk.CTkButton(TerceiroFrameScreen, text="Voltar", font=('Arial', 20, 'bold'), command=telaPrincipal).place_configure(relx=0.1, rely=0.12)

#TELA DE ALUNOS
def telaAlunos():
    QuartoFrame.place_configure(relx=0, rely=0, relwidth=1, relheight=1)
    FirstFrameScreen.place_forget()

     # FUNÇÃO PARA SALVAR DADOS
    def salvar_dados():
        matricula = entry_matricula.get()
        nota = entry_nota.get()


    #CONTEÚDO DO FRAME:

    # Instrução
    label_titulo = ctk.CTkLabel(QuartoFrame, text="Avalia Prof", font=('Arial', 40, 'bold'), text_color="#1C89DC", fg_color="#2D1E1E").place_configure(relx=0.4, rely=0.1)

    label_instrucao = ctk.CTkLabel(QuartoFrame, text="Insira a matrícula e a nota do aluno", font=('Arial', 20), text_color="#A5A5A5", fg_color="#2D1E1E").place_configure(relx=0.35, rely=0.18)

    #FRAME
    CorFrame = ctk.CTkFrame(QuartoFrame)
    CorFrame.place_configure(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.7)

    # Campo de Matrícula

    def on_entry_click(event):
        if entry_matricula.get() == "Matrícula":
            entry_matricula.delete(0, "end")
            entry_matricula.insert(0, "")
            entry_matricula.config(fg='black')  # Define a cor do texto para preto

    def on_focusout(event):
        if entry_matricula.get() == "":
            entry_matricula.insert(0, "Matrícula")
            entry_matricula.config(font=("Arial", 20), fg='grey')  # Define a cor do texto para cinza

    entry_matricula = ctk.CTkEntry(CorFrame, font=("Arial", 24))
    entry_matricula.place_configure(relx=0.25,rely=0.2, relwidth=0.5, relheight=0.15)

    entry_matricula.insert(0, "Matrícula")
    entry_matricula.bind("<FocusIn>", on_entry_click)
    entry_matricula.bind("<FocusOut>", on_focusout)

    # Campo de Nota

    def on_entry_click(event):
        if entry_nota.get() == "Nota":
            entry_nota.delete(0, "end")
            entry_nota.insert(0, "")
            entry_nota.config(fg='black')  # Define a cor do texto para preto

    def on_focusout(event):
        if entry_nota.get() == "":
            entry_nota.insert(0, "Nota")
            entry_nota.config(font=("Arial", 20), fg='grey')  # Define a cor do texto para cinza
            
    entry_nota = ctk.CTkEntry(CorFrame, font=("Arial", 24))
    entry_nota.place_configure(relx=0.25,rely=0.4, relwidth=0.5, relheight=0.15)

    entry_nota.insert(0, "Nota")
    entry_nota.bind("<FocusIn>", on_entry_click)
    entry_nota.bind("<FocusOut>", on_focusout)

    # Botão Salvar
    botao_salvar = ctk.CTkButton(CorFrame, text="Salvar", font=("Arial", 20), fg_color="#1C89DC", command=salvar_dados)
    botao_salvar.place_configure(relx=0.25,rely=0.6, relwidth=0.5, relheight=0.15)
    

#BOTÕES TELA PRINCIPAL
CResposta = ctk.CTkButton(FirstFrameScreen, text="Cartão Resposta", font=('Poppins', 20, 'bold'), fg_color="#1C89DC", corner_radius=30, command=telaCartaoResp).place_configure(relx=0.4, rely=0.35, relwidth=0.2, relheight=0.1)

CProva = ctk.CTkButton(FirstFrameScreen, text="Corrigir Prova", font=('Poppins', 20, 'bold'), fg_color="#1C89DC", corner_radius=30, command=telaCorrigir).place_configure(relx=0.4, rely=0.475, relwidth=0.2, relheight=0.1)

Alunos = ctk.CTkButton(FirstFrameScreen, text="Alunos", font=('Poppins', 20, 'bold'), fg_color="#1C89DC", corner_radius=30, command=telaAlunos).place_configure(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.1)

GPlanilha = ctk.CTkButton(FirstFrameScreen, text="Gerar Planilha", font=('Poppins', 20, 'bold'), fg_color="#1C89DC", corner_radius=30).place_configure(relx=0.4, rely=0.725, relwidth=0.2, relheight=0.1)

telaPrincipal()

app.mainloop()