import tkinter as tk
from tkinter import messagebox
from crud import create_user,read_users,update_user,delete_user

class CRUDApp:
    def __init__(self,root):
        self.root = root
        self.root.title("CRUD USUARIOS")

        #Criaçao de WIDGETS
        self.create_widgets()

    def create_widgets(self):
        #Labels
        tk.Label(self.root,text="nome: ").grid(row=0,column=0)
        tk.Label(self.root,text="telefone: ").grid(row=1,column=0)
        tk.Label(self.root,text="email: ").grid(row=2,column=0)
        tk.Label(self.root,text="usuario: ").grid(row=3,column=0)
        tk.Label(self.root,text="senha: ").grid(row=4,column=0)

        tk.Label(self.root,text="User ID(for update/delete): ").grid(row=5,column=0)

        # Criar as caixas para digitar os valores
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

        #Botoes do CRUD
        tk.Button(self.root,text="Criar Usuario",command=self.create_user).grid(row=6,column=0,columnspan=1)
        tk.Button(self.root,text="Listar Usuario",command=self.read_users).grid(row=6,column=1,columnspan=1)
        tk.Button(self.root,text="Alterar Usuario",command=self.update_user).grid(row=7,column=0,columnspan=1)
        tk.Button(self.root,text="Excluir Usuario",command=self.delete_user).grid(row=7,column=1,columnspan=1)
        self.text_area = tk.Text(self.root, height = 10, width=80)
        self.text_area.grid (row = 10, column = 0, columnspan= 4)


    def create_user(self):
        nome = self.nome_entry.get()
        telefone = self.telefone_entry.get()
        email = self.email_entry.get()
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()

        if nome and telefone and email and usuario and senha:
            create_user(nome,telefone,email,usuario,senha)
            self.nome_entry.delete(0,tk.END)
            self.telefone_entry.delete(0,tk.END)
            self.email_entry.delete(0,tk.END)
            self.usuario_entry.delete(0,tk.END)
            self.senha_entry.delete(0,tk.END)
            messagebox.showinfo("Success","Usuario criado com sucesso")
        else:
            messagebox.showerror("Error","Todos os campos são obrigatórios")
    def read_users(self):
        users =read_users()
        self.text_area.delete(1.0,tk.END)
        for user in users:
            self.text_area.insert(tk.END,f"ID: {user[0]}, Nome: {user[1]}, Telefone: {user[2]}, Email: {user[3]}\n")

    def update_user(self):
        user_id = self.user_id_entry.get()
        nome = self.nome_entry.get()
        telefone = self.telefone_entry.get()
        email = self.email_entry.get()
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()

        if user_id and nome and telefone and email and usuario and senha:
            update_user(user_id,nome,telefone,email,usuario,senha)
            self.nome_entry.delete(0,tk.END)
            self.telefone_entry.delete(0,tk.END)
            self.email_entry.delete(0,tk.END)
            self.usuario_entry.delete(0,tk.END)
            self.senha_entry.delete(0,tk.END)
            messagebox.showerror("Success","Usuario alterado com sucesso")
        else:
            messagebox.showerror("Error","Todos os campos são obrigatórios")

    def delete_user(self):
        user_id = self.user_id_entry.get()
        if user_id:
            delete_user(user_id)
            self.user_id_entry.delete(0,tk.END)
            messagebox.showerror("Success","Usuario excluido com sucesso!")
        else:
            messagebox.showerror("Error","ID do usuario é obrigatorio")
    
if __name__=="__main__":
    root = tk.Tk()
    app = CRUDApp(root)
    root.mainloop()
