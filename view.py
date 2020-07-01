from tkinter import *
from tkinter import messagebox
import tkinter as tk
import model as model
import control as control

class mainView():
    def __init__(self, root):
        self.root = root
        self.root.geometry('300x300')
        # self.root.attributes('-fullscreen',True)#Fullscreen total, sem o X
        
        #Maximiza a tela, mas eu quero isso?
        # m = self.root.maxsize()
        # self.root.geometry('{}x{}+0+0'.format(*m))

        self.Frm1 = tk.Frame(self.root)
        self.Frm2 = tk.Frame(self.root)
        self.Frm3 = tk.Frame(self.root)

        self.Btn1 = tk.Button(self.Frm1, text = "Alunos", height = 2, width = 25)
        self.Btn1.pack(side = "top")
        # self.Btn1.bind("<Button>", control.mainControl.viewAluno)
        self.Btn1.bind("<Button>", control.alunoControl)

        self.Btn2 = tk.Button(self.Frm2, text = "Cursos", height = 2, width = 25)
        self.Btn2.pack(side = "top")
        self.Btn2.bind("<Button>", control.mainControl.viewCurso)

        self.Btn3 = tk.Button(self.Frm3, text = "Disciplinas", height = 2, width = 25)
        self.Btn3.pack(side = "top")
        self.Btn3.bind("<Button>", control.mainControl.viewDisc)

        self.Frm1.pack(fill=X)
        self.Frm2.pack(fill=X)
        self.Frm3.pack(fill=X)

class alunoView(tk.Toplevel):
    def __init__(self, ctrl):
        tk.Toplevel.__init__(self)
        self.geometry('300x300')
        self.title("Alunos")

        self.Frm1 = tk.Frame(self)
        self.Frm2 = tk.Frame(self)
        self.Frm3 = tk.Frame(self)

        self.Btn1 = tk.Button(self.Frm1, text = "Inserir", height = 2, width = 25)
        self.Btn1.pack(side = "top")
        self.Btn1.bind("<Button>", ctrl.insertAluno)

        self.Btn2 = tk.Button(self.Frm2, text = "Buscar", height = 2, width = 25)
        self.Btn2.pack(side = "top")
        self.Btn2.bind("<Button>", ctrl.searchAluno)

        self.Btn3 = tk.Button(self.Frm3, text = "Ver Histórico", height = 2, width = 25)
        self.Btn3.pack(side = "top")
        # self.Btn3.bind("<Button>", control.mainControl.viewDisc)

        self.Frm1.pack(fill=X)
        self.Frm2.pack(fill=X)
        self.Frm3.pack(fill=X)

class insertAlunoView(tk.Toplevel):
    def __init__(self, ctrl):
        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Inserir aluno")

        self.Frm1 = Frame(self)
        self.Frm2 = Frame(self)
        self.Frm3 = Frame(self)
        self.Frm4 = Frame(self)

        self.Lb1 = Label(self.Frm1, text = "Nome: ")
        self.Lb1.pack(side = "left")
        self.EnterName = Entry(self.Frm1, width = 20)
        self.EnterName.pack(side = RIGHT)

        self.Lb2 = Label(self.Frm2, text = "Matrícula:")
        self.Lb2.pack(side = "left")
        self.EnterMat = Entry(self.Frm2, width = 20)
        self.EnterMat.pack(side = RIGHT)

        self.Lb3 = Label(self.Frm3, text = "Curso:")
        self.Lb3.pack(side = "left")
        self.EnterCurso = Entry(self.Frm3, width = 20)
        self.EnterCurso.pack(side = RIGHT)
        #Tentar fazer uma lista de opções

        self.EnterButton = Button(self.Frm4, text = "Enviar")
        self.EnterButton.pack(side = "left")
        self.EnterButton.bind("<Button>", ctrl.insertHandler)

        self.EnterButton = Button(self.Frm4, text = "Sair")
        self.EnterButton.pack(side = "left")
        self.EnterButton.bind("<Button>", ctrl.closeHandler)

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
        self.SearchButton.pack(side = "top")
        self.SearchButton.bind("<Button>", ctrl.searchHandler)

        self.Fr1.pack()
        self.Fr2.pack()

    def mostraAluno(self, string):
        tk.messagebox.showinfo("Aluno", string)

class cursoView(Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.geometry('300x300')
        self.title("Cursos")

        self.Frm1 = Frame(self)
        self.Btn1 = Button(self.Frm1, text = "Curso", height = 2, width = 25)
        self.Btn1.pack(side = "top")

class discView(Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.geometry('300x300')
        self.title("Disciplinas")

        self.Frm1 = Frame(self)
        self.Btn1 = Button(self.Frm1, text = "Disciplina", height = 2, width = 25)
        self.Btn1.pack(side = "top")

# class gradeView(Toplevel):
# class historicoView(Toplevel):