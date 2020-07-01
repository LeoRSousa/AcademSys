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
    
    def insertAluno(self, event):
        self.insertView = view.insertAlunoView(self)

    def insertHandler(self, event):
        matricula = self.insertView.EnterMat.get()
        nome = self.insertView.EnterName.get()
        curso = self.insertView.EnterCurso.get()
        alunoInsert = model.Aluno(matricula, nome, cursoControl)

        #Tratamento de inserção, caso já exista a matrícula
        count = 0
        for mat in self.listaAlunos:
            if alunoInsert.getNroMatric() != mat.getNroMatric():
                count += 1
                #Se o contador for menor que os itens na lista, então há um elemento igual
        # print("Contador: {}".format(count))
        try:
            if count < len(self.listaAlunos):
                raise alunoExistente()
            else:
                print("Aluno inserido!")
                self.listaAlunos.append(alunoInsert)

        except alunoExistente:
            print("Matrícula já existente!\nTente outra...")

    def closeHandler(self, event):
        self.insertView.destroy()
        
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