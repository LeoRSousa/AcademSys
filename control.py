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
    #CONSTRUTOR---------------------------------------------------------
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
        self.listaC = []

        #Cria a view para as operações do aluno
        self.view = view.alunoView(self)
    #-------------------------------------------------------------------

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
        self.listaC = self.nomeCursos()
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
            self.clear()
            mensagemIns = view.showMsg("Aluno inserido!")
            #Se já puver aulguma coisa na lista
        else:
            #Tratamento de inserção, caso já exista a matrícula
            count = 0
            for mat in self.listaAlunos:
                if alunoInsert.getNroMatric() != mat.getNroMatric():
                    count += 1
                    #Se o contador for menor que os itens na lista, então há um elemento igual
            try:
                if count < len(self.listaAlunos):
                    raise alunoExistente()
                else:
                    self.listaAlunos.append(alunoInsert)
                    self.clear()
                    mensagemIns = view.showMsg("Aluno inserido!")

            except alunoExistente:
                mensagemAlExst = view.showMsg("Matrícula já existente!\nTente outra...")

    #Mata a janela de inserção Alunos
    def closeHandler(self, event):
        #Para salvar os alunos no arquivo, sempre quando fechar a tela de inserção
        if len(self.listaAlunos) != 0:
            with open("Alunos.pickle", "wb") as arq:
                pickle.dump(self.listaAlunos, arq)
        self.insertView.destroy()

    def clear(self):
        self.insertView.EnterMat.delete(0, len(self.insertView.EnterMat.get()))
        self.insertView.EnterName.delete(0, len(self.insertView.EnterName.get())) 
    #--------------------------------------------------------------------

    #BUSCA---------------------------------------------------------------
    def searchAluno(self, event):
        self.searchView = view.searchAlunoView(self)
        
    def searchHandler(self, event):
        mat = self.searchView.EnterMat.get()
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
    #CONSTRUTOR---------------------------------------------------------
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
        
        self.listaC = []

        self.view = view.cursoView(self)
    #-------------------------------------------------------------------

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
            self.clear()
            view.showMsg("Curso inserido!")
        else:
            for curso in self.listaCursos:
                if cursoInsert.getNome() != curso.getNome():
                    count += 1
            try:
                if count < len(self.listaCursos):
                    raise cursoExistente()
                else:
                    self.listaCursos.append(cursoInsert)
                    self.clear()
                    view.showMsg("Curso inserido!")

            except cursoExistente:
                view.showMsg("Curso já existente!\nTente outro...")

    def closeHandler(self, event):
        #Para salvar os cursos no arquivo, sempre quando fechar a tela de inserção
        if len(self.listaCursos) != 0:
            with open("Cursos.pickle", "wb") as arq:
                pickle.dump(self.listaCursos, arq)
        self.insertView.destroy()

    def clear(self):
        self.insertView.EnterName.delete(0, len(self.insertView.EnterName.get()))
    #--------------------------------------------------------------------

    #BUSCA---------------------------------------------------------------
    def searchCurso(self, event):
        self.listaC = self.nomeCursos()
        self.searchView = view.searchCursoView(self, self.listaC)

    def searchHandler(self, event):
        #Cria ou carrega o arquivo contendo as grades
        if not os.path.isfile("Grades.pickle"):
            self.listaGrades = []
        else:
            with open("Grades.pickle", "rb") as arq:
                self.listaGrades = pickle.load(arq)
        nome = self.searchView.escolha.get()
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
    #CONSTRUTOR---------------------------------------------------------
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
    #-------------------------------------------------------------------

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

    #INSERÇÃO-----------------------------------------------------------
    def insertGradeHandler(self, event):
        curso = self.gradeView.escolha.get()
        ano = self.gradeView.EnterAno.get()
        gradeInsert = model.Grade(ano, curso, self.listaDiscGrade)
        count = 0
        #Procura por elementos iguais antes da inserção
        if not self.listaGrades:
            self.listaGrades.append(gradeInsert)
            self.clear()
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
                    self.clear()
                    view.showMsg("Grade inserida!")

            except gradeExistente:
                view.showMsg("Grade já existente!\nTente outra...")


    def insertDisciplina(self, event):
        escolha = self.gradeView.listbox.get(tk.ACTIVE)
        self.listaDiscGrade.append(escolha)
        view.showMsg("Disciplina inserida!")
        self.gradeView.listbox.delete(tk.ACTIVE)

    def closeGradeView(self, event):
        #Para salvar as grades no arquivo, sempre quando fechar a tela de inserção
        if len(self.listaGrades) != 0:
            with open("Grades.pickle", "wb") as arq:
                pickle.dump(self.listaGrades, arq)
        self.gradeView.destroy()

    def clear(self):
        self.gradeView.EnterAno.delete(0, len(self.gradeView.EnterAno.get()))
    #--------------------------------------------------------------------
    

class discControl():
    #CONSTRUTOR---------------------------------------------------------
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
    #-------------------------------------------------------------------

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
            self.clear()
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
                    self.clear()
                    view.showMsg("Disciplina inserida!")

            except discExistente:
                view.showMsg("Disciplina já existente!\nTente outra...")

    def closeHandler(self, event):
        #Para salvar as disciplinas no arquivo, sempre quando fechar a tela de inserção
        if len(self.listaDisc) != 0:
            with open("Discs.pickle", "wb") as arq:
                pickle.dump(self.listaDisc, arq)
        self.insertView.destroy()

    def clear(self):
        self.insertView.EnterName.delete(0, len(self.insertView.EnterName.get()))
        self.insertView.EnterCod.delete(0, len(self.insertView.EnterCod.get()))
        self.insertView.EnterCH.delete(0, len(self.insertView.EnterCH.get()))
    #-------------------------------------------------------------------

    #BUSCA--------------------------------------------------------------
    def searchDisc(self, event):
        self.searchView = view.searchDiscView(self)

    def searchHandler(self, event):
        cod = self.searchView.EnterCod.get()
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


class historicoControl():
    #CONSTRUTOR---------------------------------------------------------
    def __init__(self, event):
        self.view = view.historicoView(self)
        #Cria ou carrega o arquivo dos históricos
        if not os.path.isfile("Hist.pickle"):
            self.listaHist = []
        else:
            with open("Hist.pickle", "rb") as arq:
                self.listaHist = pickle.load(arq)
        #Cria ou carrega o arquivo das disciplinas
        if not os.path.isfile("Discs.pickle"):
            self.listaDisc = []
        else:
            with open("Discs.pickle", "rb") as arq:
                self.listaDisc = pickle.load(arq)
        #Cria ou carrega o arquivo dos alunos
        if not os.path.isfile("Alunos.pickle"):
            self.listaAlunos = []
        else:
            with open("Alunos.pickle", "rb") as arq:
                self.listaAlunos = pickle.load(arq)
        #Cria ou carrega o arquivo contendo as grades
        if not os.path.isfile("Grades.pickle"):
            self.listaGrades = []
        else:
            with open("Grades.pickle", "rb") as arq:
                self.listaGrades = pickle.load(arq)
        
        #Lista dos nomes das disciplinas cadastradas no sistema
        self.listaD = []
    #-------------------------------------------------------------------

    def nomeDiscs(self):
        nomesDiscs = []
        for disc in self.listaDisc:
            nomesDiscs.append(disc.getNome())
        return nomesDiscs

    #Pegar instancia de disciplina
    def instanciaDisc(self, discNome):
        ins = None
        for disc in self.listaDisc:
            if discNome == disc.getNome():
                ins = disc
        return ins

    def closeView(self, event):
        self.view.destroy()

    #INSERÇÃO-----------------------------------------------------------
    def insertHistView(self, event):
        self.listaD = self.nomeDiscs()
        self.insertView = view.insertHist(self, self.listaD)

    def insertHistHandler(self, event):
        mat = self.insertView.EnterMat.get()
        disc = self.insertView.listbox.get(tk.ACTIVE)
        discIns = self.instanciaDisc(disc)
        ano = self.insertView.EnterAno.get()
        semestre = self.insertView.escolha.get()
        nota = self.insertView.EnterNota.get()
        histIns = model.Historico(mat, ano, semestre, discIns, nota)
        count = 0
        if not self.listaHist:
            self.listaHist.append(histIns)
            self.clear()
            view.showMsg("Disciplina inserida no histórico")
        else:
            for hist in self.listaHist:
                if mat == hist.getAluno() and discIns.getNome() == hist.getDisc().getNome():
                    count = 0
                    if float(hist.getNota()) < 6:
                        self.listaHist.append(histIns)
                        self.clear()
                        view.showMsg("Disciplina inserida no histórico!")
                        break
                    else:
                        self.clear()
                        view.showMsg("Disciplina já cursada com aprovação...\nNão é possível refaze-la!")
                        break
                else:
                    count = 1
            if count == 1:#Pq não há a combinação de matricula com disciplina
                self.listaHist.append(histIns)
                view.showMsg("Disciplina inserida no histórico!")

    def closeInsertHandler(self, event):
        if len(self.listaHist) != 0:
            with open("Hist.pickle", "wb") as arq:
                pickle.dump(self.listaHist, arq)
        self.insertView.destroy()

    def clear(self):
        self.insertView.EnterMat.delete(0, len(self.insertView.EnterMat.get()))
        self.insertView.EnterAno.delete(0, len(self.insertView.EnterAno.get()))
        self.insertView.EnterNota.delete(0, len(self.insertView.EnterNota.get()))
    #-------------------------------------------------------------------

    #BUSCA--------------------------------------------------------------
    def searchHandlerView(self, event):
        self.searchView = view.searchHist(self)

    def searchHandler(self, event):
        string = ""
        mat = self.searchView.EnterMat.get()
        insAluno = None
        lMA = []
        count = 0
        discObr = 0
        discOpt = 0
        CHTotal = 0
        for al in self.listaAlunos:
            if mat == al.getNroMatric():
                insAluno = al
                string += al.getNome() + "\n"
                break
        for hist in self.listaHist:
            if mat == hist.getAluno():
                lMA.append(hist)#Pega as disciplinas daquele aluno
            else: #Se não for aquele aluno
                count += 1
        if count < len(self.listaHist): #Se há um histórico para aquela matricula
            lMA2 = sorted(lMA, key = model.Historico.getAno)
            for alD in lMA2:
                string += alD.getAno() + "/" + alD.getSemestre() + " -- " + alD.getDisc().getNome() + ": \nNota: " + alD.getNota()
                if float(alD.getNota()) < 6:
                    string += " - Reprovado\n"
                else:
                    string += " - Aprovado\n\n"
            #Pega o nome do curso do aluno
            curso = al.getCurso().getNome()
            #Pega as grades do curso do aluno
            grdCurso = []
            for grd in self.listaGrades:
                if curso == grd.getCurso():
                    grdCurso.append(grd.getDiscs())
            #Busca se a disciplina cursada é obrigatória ou optativa
            for alD in lMA2:
                for d in grdCurso:
                    if alD.getDisc().getNome() in d:
                        discObr += int(alD.getDisc().getCargaHoraria())
                CHTotal += int(alD.getDisc().getCargaHoraria())
            discOpt = CHTotal - discObr
            discObr = CHTotal - discOpt
        else: #Se não há um histórico para aquela matricula
            string += "Sem histórico encontrado para o(a) mesmo(a)"
        string += "\nCH Obrigatória: {}h".format(discObr) + "\nCH Optativa: {}h\n".format(discOpt)
        view.showMsg(string)

    def closeSearchHandler(self, event):
        self.searchView.destroy()
    #-------------------------------------------------------------------