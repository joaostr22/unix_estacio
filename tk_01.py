import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


# Conexão com o banco de dados SQLite
conn = sqlite3.connect('registro.db')
cursor = conn.cursor()


# Criar a tabela alunos (se ainda não existir)
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    idade INTEGER,
    curso TEXT,
    endereco TEXT,
    telefone TEXT,
    email TEXT,
    nome_responsavel TEXT,
    telefone_responsavel TEXT
)
""")
conn.commit()


# Criar a janela principal
janela = tk.Tk()
janela.title("Sistema de Registro")
janela.geometry("800x700")
janela.configure(bg="#F0F0F0")
logo = PhotoImage(file='logo.png')


# Função para lidar com o registro de estudante
def registrar_aluno():
    nome = entrada_nome_aluno.get()
    idade = int(entrada_idade_aluno.get())
    curso = entrada_curso_aluno.get()
    endereco = entrada_endereco_aluno.get()
    telefone = entrada_telefone_aluno.get()
    email = entrada_email_aluno.get()
    

    sql = """
    INSERT INTO alunos (nome, idade, curso, endereco, telefone, email)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    valores = (nome, idade, curso, endereco, telefone, email)
    cursor.execute(sql, valores)
    conn.commit()

    limpar_campos()
    messagebox.showinfo("Sucesso", "Aluno registrado com sucesso!")

def limpar_campos():
    entrada_nome_aluno.delete(0, tk.END)
    entrada_idade_aluno.delete(0, tk.END)
    entrada_curso_aluno.delete(0, tk.END)
    entrada_endereco_aluno.delete(0, tk.END)
    entrada_telefone_aluno.delete(0, tk.END)
    entrada_email_aluno.delete(0, tk.END)
    

# Estilo para os frames
s = ttk.Style()
s.configure('TFrame', background='#F0F0F0')


# Criar as abas
abas = ttk.Notebook(janela)
abas.pack(fill='both', expand=True)


# Aba de Registro de Aluno
aba_aluno = ttk.Frame(abas)
abas.add(aba_aluno, text='Cadastrar Aluno')
aba_prof = ttk.Frame(abas)
abas.add(aba_prof, text='Cadastrar Professor')


# Cabeçalho universidade
cabecalho = tk.Label(aba_aluno, text="Universidade X", font=("Cambria", 35), image=logo, compound='left')
cabecalho.place(relx=0.5, rely=0.1, anchor=tk.CENTER)


# Frames
fr_cadastro01 = Frame(aba_aluno, borderwidth=1, relief="solid", bg="#E7DFDF")
fr_cadastro01.place(x=160, y=210, width=500, height=300)


# Formulário alunos
label_explicativo = tk.Label(aba_aluno, text="Cadastro de alunos:", font=("Cambria", 20, "bold"), fg="black", bg="#F0F0F0")
label_explicativo.place(relx=0.5, rely=0.24, anchor=tk.CENTER)

#
label_nome_aluno = tk.Label(fr_cadastro01, text="Nome:", font=("Arial", 12), fg="black", bg="#E7DFDF")
label_nome_aluno.place(relx=0.35, rely=0.1, anchor=tk.E) #antes 0.3

entrada_nome_aluno = tk.Entry(fr_cadastro01, font=("Arial", 12))
entrada_nome_aluno.place(relx=0.7, rely=0.1, anchor=tk.CENTER)

#
label_idade_aluno = tk.Label(fr_cadastro01, text="Idade:", font=("Arial", 12), fg="black", bg="#E7DFDF")
label_idade_aluno.place(relx=0.35, rely=0.25, anchor=tk.E)

entrada_idade_aluno = tk.Entry(fr_cadastro01, font=("Arial", 12))
entrada_idade_aluno.place(relx=0.7, rely=0.25, anchor=tk.CENTER)

#
label_curso_aluno = tk.Label(fr_cadastro01, text="Curso:", font=("Arial", 12), fg="black", bg="#E7DFDF")
label_curso_aluno.place(relx=0.35, rely=0.4, anchor=tk.E)

entrada_curso_aluno = tk.Entry(fr_cadastro01, font=("Arial", 12))
entrada_curso_aluno.place(relx=0.7, rely=0.4, anchor=tk.CENTER)

#
label_endereco_aluno = tk.Label(fr_cadastro01, text="Endereço:", font=("Arial", 12), fg="black", bg="#E7DFDF")
label_endereco_aluno.place(relx=0.35, rely=0.55, anchor=tk.E)

entrada_endereco_aluno = tk.Entry(fr_cadastro01, font=("Arial", 12))
entrada_endereco_aluno.place(relx=0.7, rely=0.55, anchor=tk.CENTER)

#
label_telefone_aluno = tk.Label(fr_cadastro01, text="Telefone:", font=("Arial", 12), fg="black", bg="#E7DFDF")
label_telefone_aluno.place(relx=0.35, rely=0.70, anchor=tk.E)

entrada_telefone_aluno = tk.Entry(fr_cadastro01, font=("Arial", 12))
entrada_telefone_aluno.place(relx=0.7, rely=0.70, anchor=tk.CENTER)

#
label_email_aluno = tk.Label(fr_cadastro01, text="Email:", font=("Arial", 12), fg="black", bg="#E7DFDF")
label_email_aluno.place(relx=0.35, rely=0.85, anchor=tk.E)

entrada_email_aluno = tk.Entry(fr_cadastro01, font=("Arial", 12))
entrada_email_aluno.place(relx=0.7, rely=0.85, anchor=tk.CENTER)

#
botao_enviar = tk.Button(aba_aluno, text="Enviar", command=registrar_aluno, font=("Arial", 14), fg="white", bg="#a94040")
botao_enviar.place(relx=0.6, rely=0.85, anchor=tk.CENTER)

botao_limpar = tk.Button(aba_aluno, text="Limpar", command=limpar_campos, font=("Arial", 14), fg="white", bg="#a94040")
botao_limpar.place(relx=0.4, rely=0.85, anchor=tk.CENTER)







janela.mainloop()
