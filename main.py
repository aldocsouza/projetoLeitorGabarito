import customtkinter as ctk
from tkinter import *

app = ctk.CTk()
app.geometry("1000x600")
app.title("Bem-vindo ao Avalia Prof!")
app.resizable(False, False)

FirstFrameScreen = ctk.CTkFrame(app, fg_color="#2D1E1E")
#TELA PRINCIPAL
def telaPrincipal():
    FirstFrameScreen.place_configure(relx=0, rely=0, relwidth=1, relheight=1)

    #CONTEÚDO DO FRAME:
    lb_title = ctk.CTkLabel(FirstFrameScreen, text="Avalia Prof", font=('Arial', 40, 'bold'), text_color="#1C89DC", fg_color="#2D1E1E").place_configure(relx=0.4, rely=0.1)

    lb_inst = ctk.CTkLabel(FirstFrameScreen, text="Selecione as opções:", font=('Arial', 20), text_color="#A5A5A5", fg_color="#2D1E1E").place_configure(relx=0.4, rely=0.25)

telaPrincipal()

app.mainloop()