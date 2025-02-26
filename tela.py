import tkinter as tk
from tkinter import messagebox
from crud import creat_user,read_users,update_user,delet_user

class CRUDApp:
    def __init__(self,root):
        self.root = root
        self.root.title("CRUD USUARIOS")

        #Criação de widgets
        self.create_widgets()

    def create_widgets(self):
        #Labels
        tk.label(self.root,text="Nome:").grid(row=0,collumn=0)
        tk.label(self.root,text="telefone:").grid(row=1,collumn=0)
        tk.label(self.root,text="Email:").grid(row=2,collumn=0)
        tk.label(self.root,text="usuário:").grid(row=3,collumn=0)
        tk.label(self.root,text="senha:").grid(row=4,collumn=0)

        tk.label(self.root,text="User ID(for update/delete):").grid(row=5,collumn=0)


        # CRIAR AS CAIXAS PARA DIGITAR OS VALORES (OS DADOS).
        self.nome_entry = tk.Entry(self.root)

        self.telefone_entry = tk.Entry(self.root)
        self.email_entry = tk.Entry(self.root)
        self.usuario_entry = tk.Entry(self.root)
        self.senha_entry = tk.Entry(self.root)
        self.user_id_entry = tk.Entry(self.root)

        self.nome_entry.grid(row=0,column=1)
        self.telefone_entry.grid(row=1,column=1)
        self.email_entry.grid(row=2,column=1)
        self.usuario_entry.grid(row=3,column=1)
        self.senha_entry.grid(row=4,column=1)
        
        self.user_id_entry.grid(row=5,column=1)

        #botões do CRUD
        tk.Button(self.root,text="Criar Usuario",command=self.creat_user).grid(row=6,column=0,columnspan=1)
        tk.Button(self.root,text="listar usuario",command=self.creat_user).grid(row=6,column=1,columnspan=1)
        tk.Button(self.root,text="Alterar usuário",command=self.creat_user).grid(row=7,column=0,columnspan=1)
        tk.Button(self.root,text="Excluir usuário",command=self.creat_user).grid(row=7,column=1,columnspan=1)

    def creat_user(self):
        nome = self.nome_entry.get()
        telefone = self.telefone_entry.get()
        email = self.email_entry.get()
        usuario = self.usuario_entry.get()
        senha = self.senha_entry_entry.get()
        
        if nome and telefone and email and usuario and senha:
            creat_user(nome,telefone,email,usuario,senha)
            self.nome_entry.delete(0,tk.END)
            self.telefone_entry.delete(0,tk.END)
            self.email_entry.delete(0,tk.END)
            self.usuario_entry.delete(0,tk.END)
            self.senha_entry.delete(0,tk.END)
            messagebox.showerror("Success","Usuário criado com sucesso")
        else:
            messagebox.showerror("Error","Todos os campos são obrigatórios")
    def read_users(self):
        users = read_users()
        self.text_area.delete(1.0,tk.END)
        for user in users:
            self.text_area.insert(tk.END,f"ID: {user[0]}, nome:{user[1]},telefone:{user[2]},Email:{user[3]}\n")
tk.mainloop()