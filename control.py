from tkinter import *
from tkinter import messagebox
import model as model
import view as view

#INÍCIO DAS EXCEPTION CLASS
class alunoExistente(Exception):
    pass


#FIM DAS EXCEPTION CLASS

class mainControl():
    def __init__(self):
        self.root = Tk()

        # self.ctrlAluno = alunoControl()

        self.view = view.mainView(self.root)

        self.root.title("Sistema de Controle Acadêmico")
        self.root.mainloop()

    # def viewAluno(self):
    #     vA = alunoControl()
    #     vA.trigView()

    def viewCurso(self):
        vC = cursoControl()
        vC.trigView()

    def viewDisc(self):
        vD = discControl()
        vD.trigView()


class alunoControl():
    def __init__(self, event):
        self.listaAlunos = []
        self.view = None
        self.view = view.alunoView(self)
    #TEESTAR SE N POSSO COMEÇAR DIRETO
    # def trigView(self):
        # self.view = view.alunoView()
    
    def insertAluno(self, event):
        self.insertView = view.insertAlunoView(self)

    def insertHandler(self, event):
        matricula = self.insertView.EnterMat.get()
        nome = self.insertView.EnterName.get()
        curso = self.insertView.EnterCurso.get()
        alunoInsert = model.Aluno(matricula, nome, cursoControl)
        try:
            if alunoInsert.getNroMatric() in self.listaAlunos:
                raise alunoExistente()

        
        self.listaAlunos.append(alunoInsert)
        # print("Nome:{} Mat.:{}".format(alunoInsert.getNome(), alunoInsert.getNroMatric()))

        
# class insertAlunoControl():
#     def __init__(self, event):
#         self.insertView = view.insertAlunoView(self)

#     def insertHandler(self, event):
#         matricula = self.insertView.EnterMat.get()
#         nome = self.insertView.EnterName.get()
#         curso = self.insertView.EnterCurso.get()
#         alunoInsert = model.Aluno(matricula, nome, cursoControl)
    

class cursoControl():
    def __init__(self):
        self.view = None

    def trigView(self):
        self.view = view.cursoView()

class discControl():
    def __init__(self):
        self.view = None

    def trigView(self):
        self.view = view.discView()

# class gradeControl()
# class historicoControl()