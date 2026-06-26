import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
from banco import cadastrar_produto
from banco import listar_produtos
from banco import excluir_produto

janela = tk.Tk()
janela.title("Sistema de Estoque")
janela.geometry("900x900")

tabela = ttk.Treeview(janela, columns=('id', 'nome', 'categoria', 'quantidade', 'preco'), show='headings')

tabela.heading('id', text='ID')
tabela.heading('nome', text='Nome')
tabela.heading('categoria', text='Categoria')
tabela.heading('quantidade', text='Quantidade')
tabela.heading('preco', text='Preço')
tabela.pack(pady=10)

tabela.column('id', width=50)
tabela.column('nome', width=200)
tabela.column('categoria', width=150)
tabela.column('quantidade', width=100)
tabela.column('preco', width=100)
tabela.pack(pady=10)

#Titulo
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

#Atualizar tabela
def atualizar_tabela():
    for item in tabela.get_children():
        tabela.delete(item)
    
    produtos = listar_produtos()
    for produto in produtos:
        tabela.insert('', tk.END, values=produto)
        messagebox.showinfo("Sucesso", "Produto atualizado com sucesso") 
    entrada_nome.delete(0, tk.END)
    entrada_categoria.delete(0, tk.END)
    entrada_quantidade.delete(0, tk.END)
    entrada_preco.delete(0, tk.END)
atualizar_tabela()

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
    atualizar_tabela()

botao_salvar = tk.Button(janela, text="Cadastrar Produto", command=salvar, width = 25)
botao_salvar.pack(pady=10)

#Excluir
def excluir():
    item_selecionado = tabela.selection()
    if not item_selecionado:
        messagebox.showwarning("Atenção", "Selecione um produto para excluir")
        return
    
    item = tabela.item(item_selecionado)
    id_produto = item['values'][0]
    excluir_produto(id_produto)
    atualizar_tabela()

    messagebox.showinfo("Sucesso", "Produto excluído com sucesso")

#Botão Excluir
botao_excluir = tk.Button(janela, text="Excluir Produto", command=excluir, width = 25)
botao_excluir.pack(pady=10)


janela.mainloop()
