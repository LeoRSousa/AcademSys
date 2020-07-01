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