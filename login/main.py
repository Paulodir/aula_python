import customtkinter as ctk
#configuração da aparencia
ctk.set_appearance_mode('light')

#Criação da funcionalidades 
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()
    
    #verificar se o usuário é Paulodir e a senha é 12345
    if usuario == 'Paulodir' and senha == '12345':
        resultado_login.configure(text='Login feito com sucesso!',text_color='green')
    else:
        resultado_login.configure(text='Login Incorreto!',text_color='red')

#criação da janela principal
app = ctk.CTk()
app.title('Sistema de Login')
app.geometry('300x300')
#criação dos campos 
#label 
label_usuario=ctk.CTkLabel(app,text='Usuário')
label_usuario.pack(pady=10)
#entry 
campo_usuario = ctk.CTkEntry(app,placeholder_text='Digite seu Usuário')
campo_usuario.pack(pady=10)
#label 
label_senha = ctk.CTkLabel(app,text='Senha')
label_senha.pack(pady=10)
#entry 
campo_senha = ctk.CTkEntry(app,placeholder_text='Digite sua Senha',show='*')
campo_senha.pack(pady=10)
#button 
botao_login = ctk.CTkButton(app,text='login', command=validar_login)
botao_login.pack(pady=10)

#campo de feedback do login 
resultado_login = ctk.CTkLabel(app,text='')
resultado_login.pack(pady=10)

#criação da janela principal

#iniciar aplicação 
app.mainloop()