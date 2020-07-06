from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import model as model
import control as control

class showMsg():
    def __init__(self, str):
        messagebox.showinfo('Mensagem', str)

class mainView():
    def __init__(self, root):
        self.root = root
        self.root.geometry('300x300')

        self.Frm1 = tk.Frame(self.root)
        self.Frm2 = tk.Frame(self.root)
        self.Frm3 = tk.Frame(self.root)

        self.Btn1 = tk.Button(self.Frm2, text = "Alunos", height = 2, width = 25)
        self.Btn1.pack(side = "top")
        self.Btn1.bind("<Button>", control.alunoControl)

        self.Btn2 = tk.Button(self.Frm1, text = "Cursos", height = 2, width = 25)
        self.Btn2.pack(side = "top")
        self.Btn2.bind("<Button>", control.cursoControl)

        self.Btn3 = tk.Button(self.Frm3, text = "Disciplinas", height = 2, width = 25)
        self.Btn3.pack(side = "top")
        self.Btn3.bind("<Button>", control.discControl)

        self.Frm1.pack(fill=X)
        self.Frm2.pack(fill=X)
        self.Frm3.pack(fill=X)

class alunoView(tk.Toplevel):
    def __init__(self, ctrl):
        tk.Toplevel.__init__(self)
        self.geometry('300x300')
        self.title("Alunos")

        self.Frm1 = tk.Frame(self)
        # self.Frm2 = tk.Frame(self)
        # self.Frm3 = tk.Frame(self)
        # self.Frm4 = tk.Frame(self)

        self.Btn1 = tk.Button(self.Frm1, text = "Inserir", height = 2, width = 25)
        self.Btn1.pack(side = "top")
        self.Btn1.bind("<Button>", ctrl.insertAluno)

        self.Btn2 = tk.Button(self.Frm1, text = "Buscar", height = 2, width = 25)
        self.Btn2.pack(side = "top")
        self.Btn2.bind("<Button>", ctrl.searchAluno)

        self.Btn3 = tk.Button(self.Frm1, text = "Histórico", height = 2, width = 25)
        self.Btn3.pack(side = "top")
        self.Btn3.bind("<Button>", control.historicoControl)

        self.Btn4 = tk.Button(self.Frm1, text = "Voltar", height = 2, width = 25)
        self.Btn4.pack(side = "top")
        self.Btn4.bind("<Button>", ctrl.closeMainHandler)

        self.Frm1.pack(fill=X)
        # self.Frm2.pack(fill=X)
        # self.Frm3.pack(fill=X)

class insertAlunoView(tk.Toplevel):
    def __init__(self, ctrl, cursos):
        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Inserir aluno")

        self.Frm1 = Frame(self)
        self.Frm2 = Frame(self)
        self.Frm3 = Frame(self)
        self.Frm4 = Frame(self)

        self.Lb1 = Label(self.Frm1, text = "Nome:")
        self.Lb1.pack(side = "left")
        self.EnterName = Entry(self.Frm1, width = 20)
        self.EnterName.pack(side = "left")

        self.Lb2 = Label(self.Frm2, text = "Matrícula:")
        self.Lb2.pack(side = "left")
        self.EnterMat = Entry(self.Frm2, width = 20)
        self.EnterMat.pack(side = "left")

        self.CursoLabel = Label(self.Frm3, text = "Curso")
        self.CursoLabel.pack(side = "left")
        self.escolha = StringVar()
        self.combobox = ttk.Combobox(self.Frm3, width = 15 , textvariable = self.escolha)
        self.combobox.pack(side="left")
        self.combobox['values'] = cursos

        self.EnterButton = Button(self.Frm4, text = "Enviar")
        self.EnterButton.pack(side = "left")
        self.EnterButton.bind("<Button>", ctrl.insertHandler)

        self.CloseButton = Button(self.Frm4, text = "Salvar e Sair", bg = "red", fg = "white")
        self.CloseButton.pack(side = "left")
        self.CloseButton.bind("<Button>", ctrl.closeHandler)

        self.Frm1.pack()
        self.Frm2.pack()
        self.Frm3.pack()
        self.Frm4.pack()

class searchAlunoView(tk.Toplevel):
    def __init__(self, ctrl):
        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Buscar")

        self.Fr1 = Frame(self)
        self.Fr2 = Frame(self)

        self.Lb1 = Label(self.Fr1, text = "Matrícula:")
        self.Lb1.pack(side = "left")
        self.EnterMat = Entry(self.Fr1, width = 20)
        self.EnterMat.pack()

        self.SearchButton = Button(self.Fr2, text = "Buscar")
        self.SearchButton.pack(side = "left")
        self.SearchButton.bind("<Button>", ctrl.searchHandler)

        self.CloseButton = Button(self.Fr2, text = "Sair")
        self.CloseButton.pack(side = "left")
        self.CloseButton.bind("<Button>", ctrl.closeSearchHandler)

        self.Fr1.pack()
        self.Fr2.pack()

    def mostraAluno(self, string):
        tk.messagebox.showinfo("Aluno", string)

class cursoView(Toplevel):
    def __init__(self, ctrl):
        tk.Toplevel.__init__(self)
        self.geometry('300x300')
        self.title("Cursos")

        self.Frm1 = Frame(self)
        self.Frm2 = Frame(self)
        self.Frm3 = Frame(self)

        self.insertButton = Button(self.Frm1, text = "Inserir Curso", height = 2, width = 25)
        self.insertButton.pack(side = "top")
        self.insertButton.bind("<Button>", ctrl.insertCurso)

        self.searchButton = Button(self.Frm1, text = "Buscar Curso", height = 2, width = 25)
        self.searchButton.pack(side = "top")
        self.searchButton.bind("<Button>", ctrl.searchCurso)

        self.gradesButton = Button(self.Frm1, text = "Inserir Grades", height = 2, width = 25)
        self.gradesButton.pack(side = "top")
        self.gradesButton.bind("<Button>", control.gradeControl)

        self.closeButton = Button(self.Frm1, text = "Voltar", height = 2, width = 25)
        self.closeButton.pack(side = "top")
        self.closeButton.bind("<Button>", ctrl.closeMainHandler)

        self.Frm1.pack()
        # self.Frm2.pack()
        # self.Frm3.pack()
        

class insertCursoView(tk.Toplevel):
    def __init__(self, ctrl):
        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Inserir Curso")

        self.Frm1 = Frame(self)
        self.Frm2 = Frame(self)

        self.Lb1 = Label(self.Frm1, text = "Nome: ")
        self.Lb1.pack(side = "left")
        self.EnterName = Entry(self.Frm1, width = 20)
        self.EnterName.pack(side = "right")

        self.EnterButton = Button(self.Frm2, text = "Inserir")
        self.EnterButton.pack(side = "left")
        self.EnterButton.bind("<Button>", ctrl.insertHandler)

        self.CloseButton = Button(self.Frm2, text = "Salvar e Sair", bg = "red", fg = "white")
        self.CloseButton.pack(side = "left")
        self.CloseButton.bind("<Button>", ctrl.closeHandler)

        self.Frm1.pack()
        self.Frm2.pack()


class searchCursoView(tk.Toplevel):
    def __init__(self, ctrl, listaCursos):
        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Buscar")

        self.Fr1 = Frame(self)
        self.Fr2 = Frame(self)

        self.CursoLabel = Label(self.Fr1, text = "Curso")
        self.CursoLabel.pack(side = "left")
        self.escolha = StringVar()
        self.combobox = ttk.Combobox(self.Fr1, width = 15 , textvariable = self.escolha)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaCursos

        self.SearchButton = Button(self.Fr2, text = "Buscar")
        self.SearchButton.pack(side = "left")
        self.SearchButton.bind("<Button>", ctrl.searchHandler)

        self.AllButton = Button(self.Fr2, text = "Ver todos")
        self.AllButton.pack(side = "left")
        self.AllButton.bind("<Button>", ctrl.verTodosHandler)

        self.CloseButton = Button(self.Fr2, text = "Sair")
        self.CloseButton.pack(side = "left")
        self.CloseButton.bind("<Button>", ctrl.closeSearchHandler)

        self.Fr1.pack()
        self.Fr2.pack()

class insertGradeView(tk.Toplevel):
    def __init__(self, ctrl, listaCursos, listaDisc):
        tk.Toplevel.__init__(self)
        self.geometry('400x300')
        self.title("Grade")

        self.Fr1 = Frame(self)
        self.Fr2 = Frame(self)
        self.Fr3 = Frame(self)
        self.Fr4 = Frame(self)

        self.CursoLabel = Label(self.Fr1, text = "Curso")
        self.CursoLabel.pack(side = "left")
        self.escolha = StringVar()
        self.combobox = ttk.Combobox(self.Fr1, width = 15 , textvariable = self.escolha)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaCursos

        self.AnoLabel = Label(self.Fr2, text = "Ano da grade")
        self.AnoLabel.pack(side = "left")
        self.EnterAno = Entry(self.Fr2, width = 20)
        self.EnterAno.pack(side = "left")

        self.discLbl = Label(self.Fr3, text = "Escolha Disciplina")
        self.discLbl.pack(side = "left")
        # self.EnterAno = Entry(self.Fr3, width = 20)
        # self.EnterAno.pack(side = "left")
        self.listbox = tk.Listbox(self.Fr3)
        self.listbox.pack(side="left")
        for disc in listaDisc:
            self.listbox.insert(tk.END, disc)

        self.insertButton = Button(self.Fr4, text = "Inserir Disciplina")
        self.insertButton.pack(side = "left")
        self.insertButton.bind("<Button>", ctrl.insertDisciplina)

        self.createButton = Button(self.Fr4, text = "Criar grade")
        self.createButton.pack(side = "left")
        self.createButton.bind("<Button>", ctrl.insertGradeHandler)

        self.closeButton = Button(self.Fr4, text = "Salvar e sair")
        self.closeButton.pack(side = "left")
        self.closeButton.bind("<Button>", ctrl.closeGradeView)

        self.Fr1.pack()
        self.Fr2.pack()
        self.Fr3.pack()   
        self.Fr4.pack()     


class discView(tk.Toplevel):
    def __init__(self, ctrl):
        tk.Toplevel.__init__(self)
        self.geometry('300x300')
        self.title("Disciplinas")

        self.Frm1 = Frame(self)

        self.insertButton = tk.Button(self.Frm1, text = "Inserir", height = 2, width = 25)
        self.insertButton.pack(side = "top")
        self.insertButton.bind("<Button>", ctrl.insertDisc)

        self.searchButton = tk.Button(self.Frm1, text = "Buscar", height = 2, width = 25)
        self.searchButton.pack(side = "top")
        self.searchButton.bind("<Button>", ctrl.searchDisc)

        self.closeButton = tk.Button(self.Frm1, text = "Voltar", height = 2, width = 25)
        self.closeButton.pack(side = "top")
        self.closeButton.bind("<Button>", ctrl.closeMainHandler)

        self.Frm1.pack()


class insertDiscView(tk.Toplevel):
    def __init__(self, ctrl):
        tk.Toplevel.__init__(self)
        self.geometry('300x300')
        self.title("Disciplinas")

        self.Fr1 = Frame(self)
        self.Fr2 = Frame(self)
        self.Fr3 = Frame(self)
        self.Fr4 = Frame(self)

        self.Lb1 = Label(self.Fr1, text = "Nome: ")
        self.Lb1.pack(side = "left")
        self.EnterName = Entry(self.Fr1, width = 20)
        self.EnterName.pack(side = "right")

        self.Lb2 = Label(self.Fr2, text = "Código: ")
        self.Lb2.pack(side = "left")
        self.EnterCod = Entry(self.Fr2, width = 20)
        self.EnterCod.pack(side = "right")

        self.Lb3 = Label(self.Fr3, text = "Carga Horária: ")
        self.Lb3.pack(side = "left")
        self.EnterCH = Entry(self.Fr3, width = 20)
        self.EnterCH.pack(side = "right")

        self.sendButton = Button(self.Fr4, text = "Enviar")
        self.sendButton.pack(side = "left")
        self.sendButton.bind("<Button>", ctrl.insertHandler)

        self.closeButton = Button(self.Fr4, text = "Salvar e Sair")
        self.closeButton.pack(side = "left")
        self.closeButton.bind("<Button>", ctrl.closeHandler)

        self.Fr1.pack()
        self.Fr2.pack()
        self.Fr3.pack()
        self.Fr4.pack()

class searchDiscView(tk.Toplevel):
    def __init__(self, ctrl):
        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Buscar")

        self.Fr1 = Frame(self)
        self.Fr2 = Frame(self)

        self.Lb1 = Label(self.Fr1, text = "Cod:")
        self.Lb1.pack(side = "left")
        self.EnterCod = Entry(self.Fr1, width = 20)
        self.EnterCod.pack(side = "right")

        self.sendButton = Button(self.Fr2, text = "Buscar")
        self.sendButton.pack(side = "left")
        self.sendButton.bind("<Button>", ctrl.searchHandler)

        self.searchAllButton = Button(self.Fr2, text = "Buscar Todas")
        self.searchAllButton.pack(side = "left")
        self.searchAllButton.bind("<Button>", ctrl.searchAllHandler)

        self.closeButton = Button(self.Fr2, text = "Fechar")
        self.closeButton.pack(side = "left")
        self.closeButton.bind("<Button>", ctrl.closeSearchHandler)

        self.Fr1.pack()
        self.Fr2.pack()

class historicoView(Toplevel):
    def __init__(self, ctrl):
        tk.Toplevel.__init__(self)
        self.geometry('250x250')
        self.title("Histórico")

        self.Fr1 = Frame(self)

        self.Bt1 = Button(self.Fr1, text = "Cadastrar/Atualizar Histórico", height = 2, width = 25)
        self.Bt1.pack(side = "top")
        self.Bt1.bind("<Button>", ctrl.insertHistView)
        self.Bt2 = Button(self.Fr1, text = "Buscar Histórico", height = 2, width = 25)
        self.Bt2.pack(side = "top")
        self.Bt2.bind("<Button>", ctrl.searchHandlerView)
        self.Bt3 = Button(self.Fr1, text = "Voltar")
        self.Bt3.pack(side = "top")
        self.Bt3.bind("<Button>", ctrl.closeView)

        self.Fr1.pack()

class insertHist(Toplevel):
    def __init__(self, ctrl, listaD):
        tk.Toplevel.__init__(self)
        self.geometry('400x310')
        self.title("Histórico")

        self.Fr1 = Frame(self)
        self.Fr2 = Frame(self)
        self.Fr3 = Frame(self)
        self.Fr4 = Frame(self)
        self.Fr5 = Frame(self)
        self.Fr6 = Frame(self)

        self.Lb1 = Label(self.Fr1, text = "Matrícula")
        self.Lb1.pack(side = "left")
        self.EnterMat = Entry(self.Fr1, width = 30)
        self.EnterMat.pack(side = "right")

        self.Lb2 = Label(self.Fr2, text = "Disciplina")
        self.Lb2.pack(side = "left")
        self.listbox = tk.Listbox(self.Fr2, width = 30)
        self.listbox.pack(side="right")
        for disc in listaD:
            self.listbox.insert(tk.END, disc)

        self.Lb3 = Label(self.Fr3, text = "Ano cursado")
        self.Lb3.pack(side = "left")
        self.EnterAno = Entry(self.Fr3, width = 30)
        self.EnterAno.pack(side = "right")

        self.Lb4 = Label(self.Fr4, text = "Semestre cursado")
        self.Lb4.pack(side = "left")
        self.escolha = StringVar()
        self.combobox = ttk.Combobox(self.Fr4, width = 30 , textvariable = self.escolha)
        self.combobox.pack(side="right")
        self.combobox['values'] = [1, 2]

        self.Lb5 = Label(self.Fr5, text = "Nota final")
        self.Lb5.pack(side = "left")
        self.EnterNota = Entry(self.Fr5, width = 30)
        self.EnterNota.pack(side = "right")

        self.Bt1 = Button(self.Fr6, text = "Colocar disciplina no histórico")
        self.Bt1.pack(side = "left")
        self.Bt1.bind("<Button>", ctrl.insertHistHandler)
        self.Bt2 = Button(self.Fr6, text = "Salvar e sair")
        self.Bt2.pack(side = "left")
        self.Bt2.bind("<Button>", ctrl.closeInsertHandler)

        self.Fr1.pack()
        self.Fr2.pack()
        self.Fr3.pack()
        self.Fr4.pack()
        self.Fr5.pack()
        self.Fr6.pack()

class searchHist(Toplevel):
    def __init__(self, ctrl):
        tk.Toplevel.__init__(self)
        self.geometry('200x200')
        self.title("Histórico")

        self.Fr1 = Frame(self)
        self.Fr2 = Frame(self)

        self.Lb1 = Label(self.Fr1, text = "Matrícula: ")
        self.Lb1.pack(side = "left")
        self.EnterMat = Entry(self.Fr1, width = 20)
        self.EnterMat.pack(side = "left")

        self.SearchButton = Button(self.Fr2, text = "Buscar")
        self.SearchButton.pack(side = "left")
        self.SearchButton.bind("<Button>", ctrl.searchHandler)

        self.closeButton = Button(self.Fr2, text = "Sair")
        self.closeButton.pack(side = "left")
        self.closeButton.bind("<Button>", ctrl.closeSearchHandler)

        self.Fr1.pack()
        self.Fr2.pack()