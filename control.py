from tkinter import *
# from tkinter import messagebox
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
                print("Aluno inserido!")#Mostra pro usuario tbm

                                        #E SE CRIASSE A CLASSE MENSAGEMVIEW E USASSE ELA PRA GERAL?
                self.listaAlunos.append(alunoInsert)

        except alunoExistente:
            print("Matrícula já existente!\nTente outra...")#Cade a mensagem pro usuário?

    def closeHandler(self, event):
        self.insertView.destroy()

    def searchAluno(self, event):
        self.searchView = view.searchAlunoView(self)
        
    def searchHandler(self, event):
        mat = self.searchView.EnterMat.get()
        print(mat)
        string = None
        #Verificar se não está vazio antes, ou dá problema na busca
        if not self.listaAlunos:
            string = "Nenhum aluno cadastrado!"
        else:
            for al in self.listaAlunos:
                if mat == al.getNroMatric():
                    string = "Matrícula: " + al.getNroMatric() + "\nNome: " + al.getNome()
                    break
                else:
                    string = "Aluno Não encontrado!"
        #A busca acima monta uma string com o resiltado e é passada pra uma messagebox
        self.searchView.mostraAluno(string)

    def closeSearchHandler(self, event):
        self.searchView.destroy()
    

class cursoControl():
    def __init__(self, event):
        self.view = view.cursoView(self)
        self.listaCursos = []

    def insertCurso(self):
        self.insertView = view.insertCursoView(self)

    def insertHandler(self, event):
        nome = self.insertView.EnterName.get()
        cursoInsert = model.Curso(nome) 
        count = 0
        if not self.listaCursos:
            self.listaCursos.append(cursoInsert)
        else:
            for curso in self.listaCursos:
                if cursoInsert.getNome() != curso.getNome():
                count += 1
            try:
                if count < len(self.listaCursos):
                    raise alunoExistente()#Muda o exception
                else:
                    # print("Aluno inserido!")
                    self.listaCursos.append(cursoInsert)

            except alunoExistente:
                print("Matrícula já existente!\nTente outra...")

    def closeHandler(self, event):
        self.insertView.destroy()


class discControl():
    def __init__(self, event):
        self.view = view.discView(self)

        

# class gradeControl()
# class historicoControl()