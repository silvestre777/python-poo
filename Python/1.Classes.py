import os

os.system("cls || clear") # Limpar a tela

class Aluno:
    #nome, idade
    #Construtor
    def __init__(self,nome: str,idade: int):
        #pass significa passe para proxima linha
        #Atributos da class
        self.nome = nome
        self.idade = idade

        #comando self significa que o objeto pertence a classe
    def exibir_dados(self) -> str:
        return f"Nome: {self.nome} \nIdade: {self.idade}"
#Instanciar classe:

aluno = Aluno("Silvestre",23)

# print(f"Nome: {aluno.nome} \nIdade: {aluno.idade}")

print(aluno.exibir_dados())