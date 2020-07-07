#Classe Aluno
class Aluno:
    def __init__(self, nroMatric, nome, curso):
        self.__nroMatric = nroMatric
        self.__nome = nome
        self.__curso = curso

    def getNroMatric(self):
        return self.__nroMatric

    def getNome(self):
        return self.__nome

    def getCurso(self):
        return self.__curso

#Classe Curso
class Curso:
    def __init__(self, nome):
        self.__nome = nome

        self.__alunos = [] #Criar uma lista de alunos

    def getNome(self):
        return self.__nome

    def getAlunos(self):
        self.__alunos

    def getGrades(self):
        return self.__grades

    def addAluno(self, aluno):
        self.__alunos.append(aluno)

#Classe Grade
class Grade:
    def __init__(self, ano, curso, disciplinas):
        self.__ano = ano
        self.__curso = curso
        self.disciplinas = disciplinas

    def getAno(self):
        return self.__ano

    def getCurso(self):
        return self.__curso

    def getDiscs(self):
        return self.disciplinas

#Classe Disciplina
class Disciplinas:
    def __init__(self, codigo, nome, cargaHoraria):
        self.__codigo = codigo
        self.__nome = nome
        self.__cargaHoraria = cargaHoraria

    def getCodigo(self):
        return self.__codigo

    def getNome(self):
        return self.__nome

    def getCargaHoraria(self):
        return self.__cargaHoraria


#Classe Histórico
class Historico:
    def __init__(self, aluno, ano, semestre, disc, nota):
        self.__aluno = aluno
        self.__ano = ano
        self.__semestre = semestre
        self.__disc = disc
        self.__nota = nota

    def getAluno(self):
        return self.__aluno

    def getAno(self):
        return self.__ano

    def getSemestre(self):
        return self.__semestre
    
    def getDisc(self):
        return self.__disc

    def getNota(self):
        return self.__nota