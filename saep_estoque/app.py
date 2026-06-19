import tkinter as tk
from tkinter import messagebox 
from banco import cadastrar_produto

janela = tk.Tk()
janela.title("Sistema de Estoque")
janela.geometry("800x600")

titulo = tk.Label(
    janela, 
    text = " Sistema de Controle de Estoque ", 
    font=("Arial", 18, "bold")
)
titulo.pack(pady = 10)

frame_nome = tk.Frame(janela)
frame_nome.pack(pady=5)

#Campos (NOME)
tk.Label(frame_nome, text="Nome do produto: ").pack()
entrada_nome = tk.Entry(frame_nome, width=40)
entrada_nome.pack()

#Campos (CATEGORIA)
tk.Label(janela, text="Categoria: ").pack()
entrada_categoria = tk.Entry(janela, width=40)
entrada_categoria.pack()

#Campos (QUANTIDADE)
tk.Label(janela, text="Quantidade: ").pack()
entrada_quantidade = tk.Entry(janela, width=40)
entrada_quantidade.pack()

#Campos (PREÇO)
tk.Label(janela, text="Preço: ").pack()
entrada_preco = tk.Entry(janela, width=40)
entrada_preco.pack()

def salvar():
    nome = entrada_nome.get()
    categoria = entrada_categoria.get()
    quantidade = entrada_quantidade.get()
    preco = entrada_preco.get()

    if nome == "" or categoria == "" or quantidade == "" or preco == "":
        messagebox.showwarning("Atenção", "Todos os campos devem ser preenchidos")
        return 

    cadastrar_produto(nome, categoria, int(quantidade), float(preco))

    messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
    entrada_nome.delete(0, tk.END)
    entrada_categoria.delete(0, tk.END)
    entrada_quantidade.delete(0, tk.END)
    entrada_preco.delete(0, tk.END)


botao_salvar = tk.Button(janela, text="Cadastrar Produto", command=salvar, width    = 25)
botao_salvar.pack(pady=10)

janela.mainloop()
