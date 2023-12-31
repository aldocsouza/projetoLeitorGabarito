import customtkinter as ctk
from tkinter import *
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk
import imutils

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
app.minsize(width=800, height=600)


#CRIAÇÃO DAS TELAS-FRAMES
FirstFrameScreen = ctk.CTkFrame(app)
SecondFrameScreen = ctk.CTkFrame(app)
TerceiroFrameScreen = ctk.CTkFrame(app)
QuartoFrame = ctk.CTkFrame(app)
QuintoFrame = ctk.CTkFrame(app)

#TELA PRINCIPAL
def telaPrincipal():
    FirstFrameScreen.place_configure(relx=0, rely=0, relwidth=1, relheight=1)
    SecondFrameScreen.place_forget()
    TerceiroFrameScreen.place_forget()
    QuartoFrame.place_forget()
    QuintoFrame.place_forget()

    #CONTEÚDO DO FRAME:
    lb_title = ctk.CTkLabel(FirstFrameScreen, text="Avalia Prof", font=('Arial', 40, 'bold'), text_color="#1C89DC")
    lb_title.place_configure(rely=0.1, relwidth=1)

    lb_inst = ctk.CTkLabel(FirstFrameScreen, text="Selecione as opções:", font=('Arial', 20), text_color="#A5A5A5")
    lb_inst.place_configure(rely=0.25, relwidth=1)

#TELA DE CARTÃO RESPOSTA
def telaCartaoResp():
    SecondFrameScreen.place_configure(relx=0, rely=0, relwidth=1, relheight=1)
    FirstFrameScreen.place_forget()

    def enviar_imagem():
        file_path = filedialog.askopenfilename()
        if file_path:
            # Faça algo com o caminho do arquivo selecionado, como exibir ou processar
            print(f"Arquivo selecionado: {file_path}")

    #CONTEÚDO DO FRAME:
    CrFrame = ctk.CTkFrame(SecondFrameScreen).place_configure(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.6)

    lb_title_CR = ctk.CTkLabel(SecondFrameScreen, text="Avalia Prof", font=('Arial', 40, 'bold'), text_color="#1C89DC")
    lb_title_CR.place_configure(rely=0.1, relwidth=1)
    
    btn_return_CR = ctk.CTkButton(SecondFrameScreen, text="Voltar", font=('Arial', 20, 'bold'), command=telaPrincipal).place_configure(relx=0.1, rely=0.12)

    label_instrucao = ctk.CTkLabel(SecondFrameScreen, text="Envie o gabarito corrigido", font=("Arial", 14), fg_color="transparent")
    label_instrucao.place_configure(relx=0.41,rely=0.55)

    # Botão "Enviar cartão gabarito" 
    enviar_imagem_button = ctk.CTkButton(SecondFrameScreen, text="Enviar Imagem", font=("Arial", 16), command=enviar_imagem)
    enviar_imagem_button.place_configure(relx=0.25,rely=0.7, relwidth=0.5, relheight=0.1)

#TELA DE CORRIGIR PROVA
def telaCorrigir():
    global nova_tela
    app.iconify()
    nova_tela = ctk.CTkToplevel()

    width = 1000
    height = 600
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2


    nova_tela.geometry(f"{width}x{height}+{x}+{y}")

    #CONTEÚDO DO FRAME:
    CorFrame = ctk.CTkFrame(nova_tela).place_configure(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.6)
    lb_title_CP = ctk.CTkLabel(nova_tela, text="Avalia Prof", font=('Arial', 40, 'bold'), text_color="#1C89DC").place_configure(relx=0.4, rely=0.1)
    lb_subtitle_CP = ctk.CTkLabel(nova_tela, text="Posicione a câmera dentro da marcação", font=('Arial', 20), text_color="#A5A5A5").place_configure(relx=0.32, rely=0.2)
    btn_return_CP = ctk.CTkButton(nova_tela, text="Voltar", font=('Arial', 20, 'bold'), command=telaPrincipal).place_configure(relx=0.1, rely=0.12)

    webcam_janela = ctk.CTkLabel(nova_tela, text='')
    webcam_janela.place_configure(relx=0.25, rely=0.27)

    def configurar_webcam():
        global video
        video = cv2.VideoCapture(0)
        iniciar_webcam()


    def iniciar_webcam():
        global image
        if video is not None:
            ret, frame = video.read()
            if ret == True:
                frame = imutils.resize(frame, width=500)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                image = ImageTk.PhotoImage(image=img)
                webcam_janela.configure(image=image)
                webcam_janela.image = image
                webcam_janela.after(10, iniciar_webcam)
    
    configurar_webcam()

# Defina CorFrame no escopo global
CorFrame = None
alunos = {}

#TELA DE ALUNOS
def telaAlunos():
    global CorFrame, alunos  # Indica que você está usando as variáveis globais CorFrame e alunos
    QuartoFrame.place_configure(relx=0, rely=0, relwidth=1, relheight=1)
    FirstFrameScreen.place_forget()

    

    def salvar_dados():
        # Acesse a variável global alunos diretamente
        matricula = entry_matricula.get()
        nota = entry_nota.get()

        
        if matricula != "Matrícula" and nota != "Nota":
            # Adiciona os dados ao dicionário global
            alunos[matricula] = nota


    #CONTEÚDO DO FRAME:

    
    label_titulo = ctk.CTkLabel(QuartoFrame, text="Avalia Prof", font=('Arial', 40, 'bold'), text_color="#1C89DC")
    label_titulo.place_configure(rely=0.1, relwidth=1)

    label_instrucao = ctk.CTkLabel(QuartoFrame, text="Insira a matrícula e a nota do aluno", font=('Arial', 20), text_color="#A5A5A5").place_configure(relx=0.35, rely=0.18)

    
    CorFrame = ctk.CTkFrame(QuartoFrame)
    CorFrame.place_configure(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.7)


    def on_entry_click_matricula(event):
        if entry_matricula.get() == "Matrícula":
            entry_matricula.delete(0, "end")
            entry_matricula.insert(0, "")
            entry_matricula.config(fg='black')  

    def on_focusout_matricula(event):
        if entry_matricula.get() == "":
            entry_matricula.insert(0, "Matrícula")
            entry_matricula.config(font=("Arial", 20), fg='grey')  

    entry_matricula = ctk.CTkEntry(CorFrame, font=("Arial", 24))
    entry_matricula.place_configure(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.15)

    entry_matricula.insert(0, "Matrícula")
    entry_matricula.bind("<FocusIn>", on_entry_click_matricula)
    entry_matricula.bind("<FocusOut>", on_focusout_matricula)

    # Campo de Nota

    def on_entry_click_nota(event):
        if entry_nota.get() == "Nota":
            entry_nota.delete(0, "end")
            entry_nota.insert(0, "")
            entry_nota.config(fg='black') 

    def on_focusout_nota(event):
        if entry_nota.get() == "":
            entry_nota.insert(0, "Nota")
            entry_nota.config(font=("Arial", 20), fg='grey')  

    entry_nota = ctk.CTkEntry(CorFrame, font=("Arial", 24))
    entry_nota.place_configure(relx=0.25, rely=0.4, relwidth=0.5, relheight=0.15)

    entry_nota.insert(0, "Nota")
    entry_nota.bind("<FocusIn>", on_entry_click_nota)
    entry_nota.bind("<FocusOut>", on_focusout_nota)

    # Botão Salvar
    botao_salvar = ctk.CTkButton(CorFrame, text="Salvar", font=("Arial", 20), command=salvar_dados)
    botao_salvar.place_configure(relx=0.25, rely=0.6, relwidth=0.5, relheight=0.15)

     #Botão Voltar
    btn_return_CP = ctk.CTkButton(QuartoFrame, text="Voltar", font=('Arial', 20, 'bold'), command=telaPrincipal).place_configure(relx=0.1, rely=0.12)


#TELA DE PLANILHA
def telaPlanilha():
    global CorFrame, alunos  # variável global CorFrame e alunos
    QuintoFrame.place_configure(relx=0, rely=0, relwidth=1, relheight=1)
    FirstFrameScreen.place_forget()

# Definição do CorFrame no escopo global
CorFrame = None

# biblioteca csv e filedialog 
import csv
from tkinter import filedialog

# Dicionário para armazenar dados dos alunos
alunos = {}

# biblioteca openpyxl
import openpyxl

# Função para gerar a planilha
def gerar_planilha():
    # Abre uma janela de diálogo para escolher o local de salvamento
    destino_arquivo = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])

    if destino_arquivo:
        # Cria um novo workbook
        wb = openpyxl.Workbook()

        # Seleciona a planilha ativa
        ws = wb.active

        # Escreve o cabeçalho com base nas chaves do dicionário
        ws.append(['Matrícula', 'Nota'])

        # Escreve os dados na planilha
        for matricula, nota in alunos.items():
            # Escreve cada linha na coluna "A" e "B" respectivamente
            ws.append([matricula, nota])

        # Salva o workbook como um arquivo xlsx
        wb.save(destino_arquivo)




# Função para tela de planilha
def telaPlanilha():
    global CorFrame  # variável global CorFrame
    QuintoFrame.place_configure(relx=0, rely=0, relwidth=1, relheight=1)
    FirstFrameScreen.place_forget()

    # Adiciona CorFrame à tela de planilha
    CorFrame = ctk.CTkFrame(QuintoFrame)
    CorFrame.place_configure(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.6)

    lb_title_GP = ctk.CTkLabel(QuintoFrame, text="Avalia Prof", font=('Arial', 40, 'bold'), text_color="#1C89DC")
    lb_title_GP.place_configure(rely=0.1, relwidth=1)

    label_instrucao = ctk.CTkLabel(QuintoFrame, text="Gerar planilha de todos os alunos", font=('Arial', 20), text_color="#A5A5A5").place_configure(relx=0.35, rely=0.2)
    
    btn_return_GP = ctk.CTkButton(QuintoFrame, text="Voltar", font=('Arial', 20, 'bold'), command=telaPrincipal).place_configure(relx=0.1, rely=0.12)

    # Botão "Gerar Planilha" 
    gerar_planilha_btn = ctk.CTkButton(QuintoFrame, text="Gerar", font=("Arial", 20), command=gerar_planilha)
    gerar_planilha_btn.place_configure(relx=0.25, rely=0.5, relwidth=0.5, relheight=0.1)
        

#BOTÕES TELA PRINCIPAL
CResposta = ctk.CTkButton(FirstFrameScreen, text="Cartão Resposta", font=('Poppins', 20, 'bold'), corner_radius=30, command=telaCartaoResp)
CResposta.place_configure(relx=0.35, rely=0.35, relwidth=0.3, relheight=0.1)

CProva = ctk.CTkButton(FirstFrameScreen, text="Corrigir Prova", font=('Poppins', 20, 'bold'), corner_radius=30, command=telaCorrigir)
CProva.place_configure(relx=0.35, rely=0.475, relwidth=0.3, relheight=0.1)

Alunos = ctk.CTkButton(FirstFrameScreen, text="Alunos", font=('Poppins', 20, 'bold'), corner_radius=30, command=telaAlunos)
Alunos.place_configure(relx=0.35, rely=0.6, relwidth=0.3, relheight=0.1)

GPlanilha = ctk.CTkButton(FirstFrameScreen, text="Gerar Planilha", font=('Poppins', 20, 'bold'), corner_radius=30, command=telaPlanilha)
GPlanilha.place_configure(relx=0.35, rely=0.725, relwidth=0.3, relheight=0.1)

telaPrincipal()

app.mainloop()