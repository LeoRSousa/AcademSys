from tkinter import *
from tkinter import messagebox
import tkinter as tk
import model as model
import control as control

class showMsg():
    def __init__(self, str):
        messagebox.showinfo('Aviso', str)

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
        self.Btn1.bind("<Button>", control.alunoControl)

        self.Btn2 = tk.Button(self.Frm2, text = "Cursos", height = 2, width = 25)
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

        self.Btn3 = tk.Button(self.Frm1, text = "Ver Histórico", height = 2, width = 25)
        self.Btn3.pack(side = "top")
        # self.Btn3.bind("<Button>", ctrl.)

        self.Btn4 = tk.Button(self.Frm1, text = "Voltar", height = 2, width = 25)
        self.Btn4.pack(side = "top")
        self.Btn4.bind("<Button>", ctrl.closeMainHandler)

        self.Frm1.pack(fill=X)
        # self.Frm2.pack(fill=X)
        # self.Frm3.pack(fill=X)

class insertAlunoView(tk.Toplevel):
    def __init__(self, ctrl):
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

        self.Lb3 = Label(self.Frm3, text = "Curso:")
        self.Lb3.pack(side = "left")
        self.EnterCurso = Entry(self.Frm3, width = 20)
        self.EnterCurso.pack(side = "left")
        #Tentar fazer uma lista de opções

        self.EnterButton = Button(self.Frm4, text = "Enviar")
        self.EnterButton.pack(side = "left")
        self.EnterButton.bind("<Button>", ctrl.insertHandler)

        self.CloseButton = Button(self.Frm4, text = "Sair", bg = "red", fg = "white")
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

        self.gradesButton = Button(self.Frm1, text = "Grades", height = 2, width = 25)
        self.gradesButton.pack(side = "top")
        self.gradesButton.bind("<Button>", ctrl.insertGrade)

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

        self.CloseButton = Button(self.Frm2, text = "Voltar", bg = "red", fg = "white")
        self.CloseButton.pack(side = "left")
        self.CloseButton.bind("<Button>", ctrl.closeHandler)

        self.Frm1.pack()
        self.Frm2.pack()


class searchCursoView(tk.Toplevel):
    def __init__(self, ctrl):
        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Buscar")

        self.Fr1 = Frame(self)
        self.Fr2 = Frame(self)

        self.Lb1 = Label(self.Fr1, text = "Nome:")
        self.Lb1.pack(side = "left")
        self.EnterNome = Entry(self.Fr1, width = 20)
        self.EnterNome.pack()

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
    def __init__(self, ctrl):
        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Grade")

        self.Fr1 = Frame(self)#Talvez uma lista suspensa de cursos
        self.Fr2 = Frame(self)
        self.Fr3 = Frame(self)

        self.CursoLabel = Label(self.Fr1, text = "Nome do curso")
        self.CursoLabel.pack(side = "left")
        self.EnterCurso = Entry(self.Fr1, width = 20)
        self.EnterCurso.pack(side = "left")

        self.AnoLabel = Label(self.Fr2, text = "Ano da grade")
        self.AnoLabel.pack(side = "left")
        self.EnterAno = Entry(self.Fr2, width = 20)
        self.EnterAno.pack(side = "left")

        self.insertButton = Button(self.Fr3, text = "Inserir")
        self.insertButton.pack(side = "left")
        self.insertButton.bind("<Button>", ctrl.insertGradeHandler)

        self.closeButton = Button(self.Fr3, text = "Voltar")
        self.closeButton.pack(side = "left")
        # self.insertButton.bind("<Button>", )

        self.Fr1.pack()
        self.Fr2.pack()
        self.Fr3.pack()        


class discView(tk.Toplevel):
    def __init__(self, ctrl):
        tk.Toplevel.__init__(self)
        self.geometry('300x300')
        self.title("Disciplinas")

        self.Frm1 = Frame(self)

        self.insertButton = tk.Button(self.Frm1, text = "Inserir", height = 2, width = 25)
        self.insertButton.pack(side = "top")
        # self.insertButton.bind("<Button>", ctrl.insertDisc)

        self.searchButton = tk.Button(self.Frm1, text = "Buscar", height = 2, width = 25)
        self.searchButton.pack(side = "top")
        # self.searchButton.bind("<Button>", ctrl.searchDisc)

        self.closeButton = tk.Button(self.Frm1, text = "Voltar", height = 2, width = 25)
        self.closeButton.pack(side = "top")
        self.closeButton.bind("<Button>", ctrl.closeMainHandler)

        self.Frm1.pack()

# class gradeView(Toplevel):
# class historicoView(Toplevel):