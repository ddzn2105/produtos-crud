# Para o código rodar, rode o arquivo criarbd.py primeiro e dps rode o main.py

from tkinter import*
from tkinter import Tk, StringVar, ttk
import tkinter.font as tkFont
from tkinter import messagebox
# Importando view.py

from view import inserir_form, ver_form, atualizar_form, deletar_form
import view
#from PIL import Image, ImageTk
################# cores ###############
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#3fbfb9"   # verde
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # ++ verde
co10 = "#FF0000" # Vermelho
co11 = "#008000" # VERDE GREEN

################# criando janela ###############

janela = Tk()
janela.title ("")
janela.geometry('900x600')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)


style = ttk.Style(janela)
style.theme_use("clam")



################# Frames ####################

frameCima = Frame(janela, width=1043, height=50, bg=co1, relief=FLAT)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1043, height=303, bg=co1, pady=20, relief=FLAT)
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=300, bg=co1, relief=FLAT)
frameBaixo.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

################# FUNÇÕES ####################

global tree

# Funcao inserir
def inserir():


    codigo = int(e_cod.get())
    nome = e_nome.get()
    descricao = e_descricao.get()
    valor = float(e_valor.get())

    lista_inserir = [codigo, nome, descricao, valor]

    for i in lista_inserir:
        if i=='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return

    inserir_form(lista_inserir)

    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

    e_cod.delete(0, 'end')
    e_nome.delete(0, 'end')
    e_descricao.delete(0, 'end')
    e_valor.delete(0, 'end')


    mostrar()


# Função atualizar

def consultar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        valor = treev_lista[0]

        e_cod.delete(0, 'end')
        e_nome.delete(0, 'end')
        e_descricao.delete(0, 'end')
        e_valor.delete(0, 'end')

        
        e_cod.insert(0, treev_lista[0])
        e_nome.insert(0, treev_lista[1])
        e_descricao.insert(0, treev_lista[2])
        e_valor.insert(0, treev_lista[3])     
    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela')
    
        

def update():
        try:    
            treev_dados = tree.focus()
            treev_dicionario = tree.item(treev_dados)
            treev_lista = treev_dicionario['values']
            cod = int(treev_lista[0])
            valor = float (treev_lista[0])

            codigo = e_cod.get()
            nome = e_nome.get()
            descricao = e_descricao.get()
            valor = float(e_valor.get())
            lista_atualizar = [codigo, nome, descricao, valor, cod]

            for i in lista_atualizar:
                if i=='':
                    messagebox.showerror('Erro', 'Preencha todos os campos')
                    return
            
            atualizar_form(lista_atualizar)
            messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')

            e_cod.delete(0, 'end')
            e_nome.delete(0, 'end')
            e_descricao.delete(0, 'end')
            e_valor.delete(0, 'end')

            mostrar()
        except IndexError:
            messagebox.showinfo('Erro', 'Preencha todos os campos')
        
# Função Deletar
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]

        

        deletar_form([valor])
        
        messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')

        mostrar()
    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela')
################# Frame Cima ####################



app_logo = Label(frameCima, text="Cadastro de Produtos", width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'),bg=co1, fg=co4 )
app_logo.place(x=0, y=0)

################# Frame Meio ####################

# Criando entradas

l_cod = Label(frameMeio, text="Código", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_cod.place(x=10, y=10)

e_cod = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_cod.place(x=130, y=11)

l_nome = Label(frameMeio, text="Nome", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=40)

e_nome = Entry(frameMeio, width=30, justify='left',relief=SOLID)
e_nome.place(x=130, y=41)

l_descricao = Label(frameMeio, text="Descrição", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_descricao.place(x=10, y=70)
e_descricao = Entry(frameMeio, width=30, justify='left',relief=SOLID)
e_descricao.place(x=130, y=71)


l_valor = Label(frameMeio, text="Valor Unitário", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_valor.place(x=10, y=100)

e_valor = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_valor.place(x=130, y=101)




#################### CRUD ####################


################# BOTÕES ####################
# Botao Inserir


botao_inserir = Button(frameMeio, command=inserir, anchor=NW, text="Adicionar".upper(), width=13, compound=LEFT, overrelief=RIDGE,  font=('ivy 8'),bg=co11, fg=co0 )
botao_inserir.place(x=450, y=10)


# Botao Consultar


botao_consultar = Button(frameMeio, command=consultar, anchor=NW, text="Consultar".upper(), width=13, compound=LEFT, overrelief=RIDGE,  font=('ivy 8'),bg=co7, fg=co0 )
botao_consultar.place(x=450, y=50)


# Botao Deletar

botao_deletar = Button(frameMeio, command=deletar, compound=CENTER, anchor=NW, text="Deletar".upper(), width=13, overrelief=RIDGE,  font=('ivy 8'),bg=co10, fg=co0 )
botao_deletar.place(x=450, y=90)

# Botao Atualizar

botao_atualizar = Button(frameMeio, command=update, text="Atualizar".upper(), width=13,  compound=LEFT, overrelief=RIDGE,  font=('ivy 8'),bg=co2, fg=co1 )
botao_atualizar.place(x=450, y=130)

# Labels Quantidade total e Valores
l_total = Label(frameMeio, text='',width=14, height=2, anchor=CENTER, font=('Ivy 17 bold'), bg=co7, fg=co1)
l_total.place(x=600, y=17)

l_valor_total = Label(frameMeio, text=' Valor Total de todos os itens  ' , height=1, anchor=NW, font=('Ivy 10 bold'), bg=co7, fg=co1)
l_valor_total.place(x=600, y=12)


l_qtd = Label(frameMeio, text='', width=14, height=2, anchor=CENTER, pady=5, font=('Ivy 17 bold'), bg=co7, fg=co1)
l_qtd.place(x=600, y=90)

l_qtd_itens = Label(frameMeio, text='       Quantidade total de itens' , height=1, anchor=NW, font=('Ivy 10 bold'), bg=co7, fg=co1)
l_qtd_itens.place(x=600, y=92)

# Funcao para mostrar

def mostrar(): 
    global tree
    # criando uma treeview com duas scrollbars
    tabela_head = ['#Código', 'Nome', 'Descrição', 'Valor unitário']

    lista_itens = ver_form()

    tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)


    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBaixo.grid_rowconfigure(0, weight=12)

    hd=["center","center","center","center"]
    h=[200,250,250,180]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)

        # Ajustar as larguras das colunas
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1

    # Inserindo os itens dentro da tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)


        
    quantidade = []
    for iten in lista_itens:
        quantidade.append(iten[3])

    Total_valor = sum(quantidade)
    Total_itens = len(quantidade)

    l_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
    l_qtd['text'] = Total_itens


mostrar()
janela.mainloop()
