import customtkinter as ctk
from tkinter import *

app = ctk.CTk()
app.geometry("1000x600")
app.title("Bem-vindo ao Avalia Prof!")
app.resizable(False, False)

#CRIAÇÃO DAS TELAS-FRAMES
FirstFrameScreen = ctk.CTkFrame(app, fg_color="#2D1E1E")
SecondFrameScreen = ctk.CTkFrame(app, fg_color="#2D1E1E")

#TELA PRINCIPAL
def telaPrincipal():
    FirstFrameScreen.place_configure(relx=0, rely=0, relwidth=1, relheight=1)
    SecondFrameScreen.place_forget()

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


#BOTÕES TELA PRINCIPAL
CResposta = ctk.CTkButton(FirstFrameScreen, text="Cartão Resposta", font=('Poppins', 20, 'bold'), fg_color="#1C89DC", corner_radius=30, command=telaCartaoResp).place_configure(relx=0.4, rely=0.35, relwidth=0.2, relheight=0.1)

CProva = ctk.CTkButton(FirstFrameScreen, text="Corrigir Prova", font=('Poppins', 20, 'bold'), fg_color="#1C89DC", corner_radius=30).place_configure(relx=0.4, rely=0.475, relwidth=0.2, relheight=0.1)

Alunos = ctk.CTkButton(FirstFrameScreen, text="Alunos", font=('Poppins', 20, 'bold'), fg_color="#1C89DC", corner_radius=30).place_configure(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.1)

GPlanilha = ctk.CTkButton(FirstFrameScreen, text="Gerar Planilha", font=('Poppins', 20, 'bold'), fg_color="#1C89DC", corner_radius=30).place_configure(relx=0.4, rely=0.725, relwidth=0.2, relheight=0.1)

telaPrincipal()

app.mainloop()