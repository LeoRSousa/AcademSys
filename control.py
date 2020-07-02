from tkinter import *
# from tkinter import messagebox
import model as model
import view as view

#INÍCIO DAS EXCEPTION CLASS
class alunoExistente(Exception):
    pass
class cursoExistente(Exception):
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
        self.view = view.alunoView(self)

    def insertAluno(self, event):
        self.insertView = view.insertAlunoView(self)

    def insertHandler(self, event):
        matricula = self.insertView.EnterMat.get()
        nome = self.insertView.EnterName.get()
        curso = self.insertView.EnterCurso.get()
        alunoInsert = model.Aluno(matricula, nome, curso)

        #Se não tiver nada na lista ele vai inserir
        if not self.listaAlunos:
            self.listaAlunos.append(alunoInsert)
            mensagemIns = view.showMsg("Aluno inserido!")
        #Se já puver aulguma coisa na lista
        else:
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
                    self.listaAlunos.append(alunoInsert)
                    print("Aluno inserido!")
                    mensagemIns = view.showMsg("Aluno inserido!")

            except alunoExistente:
                print("Matrícula já existente!\nTente outra...")#Cade a mensagem pro usuário?
                mensagemAlExst = view.showMsg("Matrícula já existente!\nTente outra...")

    #Mata a janela(geral) de Alunos
    def closeMainHandler(self, event):
        self.view.destroy()

    #Mata a janela de inserção Alunos
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

    #Mata a janela busca de Alunos
    def closeSearchHandler(self, event):
        self.searchView.destroy()
    

class cursoControl():
    def __init__(self, event):
        self.view = view.cursoView(self)
        self.listaCursos = []

    def closeMainHandler(self, event):
        self.view.destroy()

    def insertCurso(self, event):
        self.insertView = view.insertCursoView(self)

    def insertHandler(self, event):
        nome = self.insertView.EnterName.get()
        cursoInsert = model.Curso(nome) 
        count = 0
        #Se não tiver nada na lista ele vai inserir, se tiver ele procura por elementos iguais
        if not self.listaCursos:
            self.listaCursos.append(cursoInsert)
            view.showMsg("Curso inserido!")
        else:
            for curso in self.listaCursos:
                if cursoInsert.getNome() != curso.getNome():
                    count += 1
            try:
                if count < len(self.listaCursos):
                    raise cursoExistente()
                else:
                    print("Curso inserido!")
                    self.listaCursos.append(cursoInsert)
                    view.showMsg("Curso inserido!")

            except cursoExistente:
                print("Curso já existente!\nTente outra...")
                view.showMsg("Curso já existente!\nTente outro...")

    def closeHandler(self, event):
        self.insertView.destroy()

    def searchCurso(self, event):
        self.searchView = view.searchCursoView(self)

    def searchHandler(self, event):
        nome = self.searchView.EnterNome.get()
        print(nome)
        string = ""
        #Verificar se não está vazio antes, ou dá problema na busca
        if not self.listaCursos:
            string = "Nenhum curso cadastrado!"
        else:
            for cs in self.listaCursos:
                if nome == cs.getNome():
                    string = "Curso: " + cs.getNome() + "\n"
                    break
                else:
                    string = "Curso Não encontrado!"
        #A busca acima monta uma string com o resiltado e é passada pra uma messagebox
        view.showMsg(string)

    def verTodosHandler(self, event):
        string = "Cursos:\n"
        if not self.listaCursos:
            string = "Nenhum curso cadastrado!"
        for cs in self.listaCursos:
            string += cs.getNome() + "\n"
        view.showMsg(string)

    def closeSearchHandler(self, event):
        self.searchView.destroy()
    

class discControl():
    def __init__(self, event):
        self.view = view.discView(self)
        self.listaDisc = []

    def closeMainHandler(self, event):
        self.view.destroy()

# class gradeControl()
# class historicoControl()