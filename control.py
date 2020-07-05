from tkinter import *
import tkinter as tk
import model as model
import view as view
import os.path
import pickle

#INÍCIO DAS EXCEPTION CLASS
class alunoExistente(Exception):
    pass
class cursoExistente(Exception):
    pass
class discExistente(Exception):
    pass
class gradeExistente(Exception):
    pass
#FIM DAS EXCEPTION CLASS

class mainControl():
    def __init__(self):
        self.root = Tk()

        self.view = view.mainView(self.root)

        self.root.title("Sistema de Controle Acadêmico")
        self.root.mainloop()


class alunoControl():
    def __init__(self, event):
        #Cria ou carrega o arquivo contendo os alunos
        if not os.path.isfile("Alunos.pickle"):
            self.listaAlunos = []
        else:
            with open("Alunos.pickle", "rb") as arq:
                self.listaAlunos = pickle.load(arq)
        #Cria ou carrega o arquivo contendo os cursos
        if not os.path.isfile("Cursos.pickle"):
            self.listaCursos = []
        else:
            with open("Cursos.pickle", "rb") as arq:
                self.listaCursos = pickle.load(arq)
        
        #Lista com os nomes dos cursos
        self.listaC = self.nomeCursos()

        #Cria a view para as operações do aluno
        self.view = view.alunoView(self)

    #Para ver os cursos existentes
    def nomeCursos(self):
        nomesCursos = []
        for curso in self.listaCursos:
            nomesCursos.append(curso.getNome())
        return nomesCursos

    #Pegar instancia de curso
    def instanciaCurso(self, cursoNome):
        ins = None
        for curso in self.listaCursos:
            if cursoNome == curso.getNome():
                ins = curso
        return ins
    
    #Mata a janela(geral) de Alunos
    def closeMainHandler(self, event):
        self.view.destroy()
    
    #INSERÇÃO-----------------------------------------------------------
    def insertAluno(self, event):
        self.insertView = view.insertAlunoView(self, self.listaC)

    def insertHandler(self, event):
        matricula = self.insertView.EnterMat.get()
        nome = self.insertView.EnterName.get()
        curso = self.insertView.escolha.get()
        cursoIns = self.instanciaCurso(curso)
        alunoInsert = model.Aluno(matricula, nome, cursoIns)

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

    #Mata a janela de inserção Alunos
    def closeHandler(self, event):
        #Para salvar os alunos no arquivo, sempre quando fechar a tela de inserção
        if len(self.listaAlunos) != 0:
            with open("Alunos.pickle", "wb") as arq:
                pickle.dump(self.listaAlunos, arq)
        self.insertView.destroy()
    #--------------------------------------------------------------------

    #BUSCA---------------------------------------------------------------
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
                    string = "Matrícula: " + al.getNroMatric() + "\nNome: " + al.getNome() + "\nCurso: " + al.getCurso().getNome()
                    break
                else:
                    string = "Aluno Não encontrado!"
        #A busca acima monta uma string com o resiltado e é passada pra uma messagebox
        view.showMsg(string)

    #Mata a janela busca de Alunos
    def closeSearchHandler(self, event):
        self.searchView.destroy()
    #--------------------------------------------------------------------


class cursoControl():
    def __init__(self, event):
        #Cria ou carrega o arquivo contendo os cursos
        if not os.path.isfile("Cursos.pickle"):
            self.listaCursos = []
        else:
            with open("Cursos.pickle", "rb") as arq:
                self.listaCursos = pickle.load(arq)
        #Cria ou carrega o arquivo contendo as grades
        if not os.path.isfile("Grades.pickle"):
            self.listaGrades = []
        else:
            with open("Grades.pickle", "rb") as arq:
                self.listaGrades = pickle.load(arq)
        #Cria ou carrega o arquivo das disciplinas
        if not os.path.isfile("Discs.pickle"):
            self.listaDisc = []
        else:
            with open("Discs.pickle", "rb") as arq:
                self.listaDisc = pickle.load(arq)
        
        self.listaC = self.nomeCursos()
        self.listaD = self.nomeDiscs()
        # self.listaG = self.myGrades()

        self.view = view.cursoView(self)

    def closeMainHandler(self, event):
        self.view.destroy()

    def nomeCursos(self):
        nomesCursos = []
        for curso in self.listaCursos:
            nomesCursos.append(curso.getNome())
        return nomesCursos

    def nomeDiscs(self):
        nomesDiscs = []
        for disc in self.listaDisc:
            nomesDiscs.append(disc.getNome())
        return nomesDiscs

    def nomeDiscsGrade(self, curso, ano):
        nomesDiscsG = ""
        for grade in self.listaGrades:
            if grade.getAno() == ano and grade.getCurso() == curso:
                for dg in grade.getDiscs():
                    nomesDiscsG += dg + "\n"
                break
            else:
               nomesDiscsG += "" 
        return nomesDiscsG

    #Pegar instancia de disciplina
    # def instanciaDisc(self, discCod):
    #     ins = None
    #     for disc in self.listaDisc:
    #         if discCod == disc.getCodigo():
    #             ins = disc
    #     return ins

    #Pegas as grades do curso
    # def myGrades(self, nomeC):
    #     ins = None
    
    #INSERÇÃO-----------------------------------------------------------
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
        #Para salvar os cursos no arquivo, sempre quando fechar a tela de inserção
        if len(self.listaCursos) != 0:
            with open("Cursos.pickle", "wb") as arq:
                pickle.dump(self.listaCursos, arq)
        self.insertView.destroy()
    #--------------------------------------------------------------------

    #BUSCA---------------------------------------------------------------
    def searchCurso(self, event):
        self.searchView = view.searchCursoView(self, self.listaC)

    def searchHandler(self, event):
        #Cria ou carrega o arquivo contendo as grades
        if not os.path.isfile("Grades.pickle"):
            self.listaGrades = []
        else:
            with open("Grades.pickle", "rb") as arq:
                self.listaGrades = pickle.load(arq)
        nome = self.searchView.escolha.get()
        print(nome)
        string = ""
        #como o curso vem pelo combobox, não é necessário verificar se ele existe
        string += "Curso:\n" + nome + "\n"
        for grd in self.listaGrades:
            if nome == grd.getCurso():#.getNome():
                string += "\nGrade " + grd.getAno() + "\n"
                string += self.nomeDiscsGrade(nome, grd.getAno())

        #A busca acima monta uma string com o resultado e é passada pra uma messagebox
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
    #--------------------------------------------------------------------

class gradeControl():
    def __init__(self, event):
        #Cria ou carrega o arquivo contendo as grades
        if not os.path.isfile("Grades.pickle"):
            self.listaGrades = []
        else:
            with open("Grades.pickle", "rb") as arq:
                self.listaGrades = pickle.load(arq)
        #Cria ou carrega o arquivo contendo os cursos
        if not os.path.isfile("Cursos.pickle"):
            self.listaCursos = []
        else:
            with open("Cursos.pickle", "rb") as arq:
                self.listaCursos = pickle.load(arq)
        #Cria ou carrega o arquivo das disciplinas
        if not os.path.isfile("Discs.pickle"):
            self.listaDisc = []
        else:
            with open("Discs.pickle", "rb") as arq:
                self.listaDisc = pickle.load(arq)
        
        self.listaC = self.nomeCursos()
        self.listaD = self.nomeDiscs()

        self.listaDiscGrade = []

        self.gradeView = view.insertGradeView(self, self.listaC, self.listaD)


    # def closeMainHandler(self, event):
    #     #Para salvar as grades no arquivo, sempre quando fechar a tela de inserção
    #     if len(self.listaGrades) != 0:
    #         with open("Grades.pickle", "wb") as arq:
    #             pickle.dump(self.listaGrades, arq)
    #     self.view.destroy()

    def nomeCursos(self):
        nomesCursos = []
        for curso in self.listaCursos:
            nomesCursos.append(curso.getNome())
        return nomesCursos

    def nomeDiscs(self):
        nomesDiscs = []
        for disc in self.listaDisc:
            nomesDiscs.append(disc.getNome())
        return nomesDiscs

    #Pegar instancia de disciplina
    # def instanciaDisc(self, discCod):
    #     ins = None
    #     for disc in self.listaDisc:
    #         if discCod == disc.getCodigo():
    #             ins = disc
    #     return ins

    def insertGradeHandler(self, event):
        curso = self.gradeView.escolha.get()
        ano = self.gradeView.EnterAno.get()
        gradeInsert = model.Grade(ano, curso, self.listaDiscGrade)
        # for d in gradeInsert.getDiscs():
        #     print(d + "\n")
        count = 0
        #Procura por elementos iguais antes da inserção
        if not self.listaGrades:
            self.listaGrades.append(gradeInsert)
            view.showMsg("Grade inserida 0!")
        else:
            for grd in self.listaGrades:
                if curso == grd.getCurso() and ano == grd.getAno():
                    count += 1
                    break
            try:
                if count > 0:
                    raise gradeExistente()
                else:
                    self.listaGrades.append(gradeInsert)
                    print("Grade inserida!")
                    view.showMsg("Grade inserida!")

            except gradeExistente:
                print(count)
                print("Grade já existente!\nTente outra...")
                view.showMsg("Grade já existente!\nTente outra...")


    def insertDisciplina(self, event):
        escolha = self.gradeView.listbox.get(tk.ACTIVE)
        # discIns = self.instanciaDisc(escolha)
        self.listaDiscGrade.append(escolha)
        view.showMsg("Disciplina inserida!")
        self.gradeView.listbox.delete(tk.ACTIVE)

    def closeGradeView(self, event):
        #Para salvar as grades no arquivo, sempre quando fechar a tela de inserção
        if len(self.listaGrades) != 0:
            with open("Grades.pickle", "wb") as arq:
                pickle.dump(self.listaGrades, arq)
        self.gradeView.destroy()
    #--------------------------------------------------------------------
    

class discControl():
    def __init__(self, event):
        self.view = view.discView(self)
        #Cria ou carrega o arquivo das disciplinas
        if not os.path.isfile("Discs.pickle"):
            self.listaDisc = []
        else:
            with open("Discs.pickle", "rb") as arq:
                self.listaDisc = pickle.load(arq)
        

    def closeMainHandler(self, event):
        self.view.destroy()

    #INSERÇÃO-----------------------------------------------------------
    def insertDisc(self, event):
        self.insertView = view.insertDiscView(self)

    def insertHandler(self, event):
        nome = self.insertView.EnterName.get()
        cod = self.insertView.EnterCod.get()
        CH = self.insertView.EnterCH.get()
        discInsert = model.Disciplinas(cod, nome, CH)
        count = 0
        #Se não tiver nada na lista ele vai inserir, se tiver ele procura por elementos iguais
        if not self.listaDisc:
            self.listaDisc.append(discInsert)
            view.showMsg("Disciplina inserida!")
        else:
            for disc in self.listaDisc:
                if discInsert.getNome() != disc.getNome():
                    count += 1
            try:
                if count < len(self.listaDisc):
                    raise discExistente()
                else:
                    self.listaDisc.append(discInsert)
                    print("Disc inserida!")
                    view.showMsg("Disciplina inserida!")

            except discExistente:
                print("Disc já existente!\nTente outra...")
                view.showMsg("Disciplina já existente!\nTente outra...")

    def closeHandler(self, event):
        #Para salvar as disciplinas no arquivo, sempre quando fechar a tela de inserção
        if len(self.listaDisc) != 0:
            with open("Discs.pickle", "wb") as arq:
                pickle.dump(self.listaDisc, arq)
        self.insertView.destroy()
    #-------------------------------------------------------------------

    #BUSCA--------------------------------------------------------------
    def searchDisc(self, event):
        self.searchView = view.searchDiscView(self)

    def searchHandler(self, event):
        cod = self.searchView.EnterCod.get()
        print(cod)
        string = ""
        if not self.listaDisc:
            string = "Nenhuma Disciplina cadastrada!"
        else:
            for d in self.listaDisc:
                if cod == d.getCodigo():
                    string = "Código: " + d.getCodigo() + "\nNome: " + d.getNome() + "\nCarga Horária: " + d.getCargaHoraria()
                    break
                else:
                    string = "Disciplina Não encontrada!"
        #A busca acima monta uma string com o resultado e é passada pra uma messagebox
        view.showMsg(string)

    def searchAllHandler(self, event):
        string = ""
        for d in self.listaDisc:
            string += d.getNome() + "(" + d.getCodigo() + ")\n\n"
        view.showMsg(string)

    def closeSearchHandler(self, event):
        self.searchView.destroy()
    #-------------------------------------------------------------------


# class gradeControl()
# class historicoControl()