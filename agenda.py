from tkinter import *
from tkinter import messagebox
from tkinter import ttk
agenda = []

def adcionarContato() -> None:
    #pegar os valores digitados
    nome = txt_nome.get()
    telefone = txt_telefone.get()
    categoria = cb_categoria.get()
    contato = {
        "nome": nome,
        "telefone": telefone,
        "categoria": categoria
    }
    agenda.append(contato)
    messagebox.showinfo("adicionado!", "Contato adicionado com sucesso!")
    limparCampos()
    atualizarTabela() #da um bug!!! (tinha q usar o cod do atualizar para ajeitar)

def editarContato() -> None:
    contato_selecionado = tabela.selection()[0]
    if not contato_selecionado:
        return
    index = tabela.index(contato_selecionado)
    agenda[index] = {
        "nome": txt_nome.get(),
        "telefone": txt_telefone.get(),
        "categoria": cb_categoria.get()
    }
    limparCampos()
    atualizarTabela()


def deletarContato() -> None:
    contato_selecionado = tabela.selection()[0]
    if not contato_selecionado:
        return
    index = tabela.index(contato_selecionado)
    del agenda[index]
    limparCampos()
    atualizarTabela()

def limparCampos() -> None:
    txt_nome.delete(0, END)
    txt_telefone.delete(0, END)
    cb_categoria.delete(0, END)
def atualizarTabela() -> None:
    #limpando a tabela
    #get_children -> retorna uma lista com as linhas da tabela
    for linha in tabela.get_children(): #codigo sus
        tabela.delete(linha)
    for contato in agenda:
        tabela.insert("", END, values=(contato["nome"], contato["telefone"], contato["categoria"]))
def tabelaClique(event) -> None:
   contato_selecionado = tabela.selection()[0]
   if not contato_selecionado:
    return
   index = tabela.index(contato_selecionado)
   #preenchendo os campos com contato do index da tabela
   contato = agenda[index]
   limparCampos()
   txt_nome.insert(0, contato["nome"])
   txt_telefone.insert(0, contato["telefone"])
   cb_categoria.set(contato["categoria"])


window = Tk()
window.title("agenda telefonica")

label_nome = Label(window, text="nome: ", fg="navy", font=("Tahoma 14 bold"))
label_nome.grid(row=0, column=0)

label_telefone = Label(window, text="telefone: ", fg="navy", font=("Tahoma 14 bold"))
label_telefone.grid(row=1, column=0)

txt_nome = Entry(window, font=("Tahoma 14 "), width=27)
txt_nome.grid(row=0, column=1)

txt_telefone = Entry(window, font=("Tahoma 14 "), width=27)
txt_telefone.grid(row=1, column=1)

categorias = ["Amigos", "Familia", 'Trabalho']
cb_categoria = ttk.Combobox(window, values=categorias, width=25, font="tahoma 14")
cb_categoria.grid(row=2, column=1)

label_categoria = Label(window, text="categoria: ", fg="navy", font=("Tahoma 14 bold"))
label_categoria.grid(row=2, column=0)

btn_adicionar = Button(window, text="adicionar", fg="navy", bg="white", font=("tahoma 12 bold"), width=8, height=1,
                      command=adcionarContato)
btn_adicionar.grid(row=3, column=0)

btn_editar = Button(window, text="editar", fg="navy", bg="white", font=("tahoma 12 bold"), width=8, height=1,
                      command=editarContato)
btn_editar.grid(row=3, column=1)

btn_deletar = Button(window, text="deletar", fg="navy", bg="white", font=("Tahoma 12 bold"), width=8, height=1,
                      command=deletarContato)
btn_deletar.grid(row=3, column=2)

#como criar uma tabela => Treeview
tabela = ttk.Treeview(window, columns=("Nome","Telefone", "Categoria"), show="headings")
tabela.heading("Nome", text="Nome")
tabela.heading("Telefone", text="Telefone")
tabela.heading("Categoria", text="Categoria")
#criando uma ação/bind para quando o usuario clicar num contato da tabela
tabela.bind("<ButtonRelease-1>", tabelaClique)
tabela.grid(row=4, columnspan=3)

window.mainloop()