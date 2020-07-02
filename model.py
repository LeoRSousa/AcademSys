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
        self.__grades = [] #Criar uma lista de grades

    def getNome(self):
        return self.__nome

    def getAlunos(self):
        self.__alunos

    def getGrades(self):
        return self.__grades

    def addAluno(self, aluno):
        self.__alunos.append(aluno)

    def addGrade(self, grade):
        self.__grades.append(grade)

#Classe Grade
class Grade:
    def __init__(self, ano, curso):
        self.__ano = ano
        self.__curso = curso
        
        self.__disciplinas = []

        curso.addGrade(self)

    def getAno(self):
        return self.__ano

    def getCurso(self):
        return self.__curso


#Classe Histórico
# class Historico:
#     def __init__(self, aluno):
#         self.__aluno = aluno

#         self.__disciplinas = []

#     def getAluno(self):
#         return self.__aluno
    
#     def getDisciplinas(self):
#         return self.__disciplinas

#     def addDisciplina(self, disciplina):
#         self.__disciplinas.append(disciplina)