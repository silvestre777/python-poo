import os

os.system("cls || clear")

class Endereco:
    def __init__(self,logradouro: str, numero: int):
        self.logradouro = logradouro
        self.numero = numero
    
    # def exibir_endereco(self) -> str:
    #     return f"Logradouro: {self.logradouro} \nNumero: {self.numero}"

    def __str__(self) -> str:
        return f"Logradouro: {self.logradouro} \nNumero: {self.numero}"
    
#Puxando uma class para a outra, basicamente como o java
class Aluno:
    def __init__(self,nome: str,idade: int, endereco: Endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco


    # def exibir_dados(self) -> str:
    #     # return f"Nome: {self.nome} \nIdade: {self.idade}\n{self.endereco.exibir_endereco()}"
    #     return f"Nome: {self.nome} \nIdade: {self.idade}\n{self.endereco}"

    def __str__(self) -> str:
        return f"Nome: {self.nome} \nIdade: {self.idade}\n{self.endereco}"
    

#Instanciar

#Metodo 1 para fazer
#endereco1 = Endereco("Rua A",12)
#aluno = Aluno ("Silvestre", 23)
#print(aluno.exibir_dados())
#print(endereco.exibir_endereco())


aluno = Aluno("Silvestre",23,Endereco("Rua A",12))
aluno1 = Aluno("Ferreira",23,Endereco("Rua B",13))

# print(f"== DADOS DO ALUNO 1 ==")
# print(aluno.exibir_dados())
# print(f"\n")
# print(f"== DADOS DO ALUNO 2 ==")
# print(aluno1.exibir_dados())

print(f"== DADOS DO ALUNO 1 ==")
print(aluno)
print(f"\n")
print(f"== DADOS DO ALUNO 2 ==")
print(aluno1)