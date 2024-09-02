from abc import ABC,abstractmethod
import os
os.system("cls || clear") # Limpa terminal

#Metodo de fazer Herança coloca dentro do parentese importa o nome "ABC" o que torna ela abastrata
class Funcionario(ABC):
    #Construtor
    def __init__(self, nome: str, idade : int, salario: float) -> None:
        self.nome = nome
        self.idade = idade
        self.salario = salario

    @abstractmethod
    def calcular_salario(self)->float:
        pass

class Gerente(Funcionario):
    def calcular_salario(self) -> float:
        BONIFICACAO = 1.2 # Acrescimo de 20%
        salario_final = self.salario * BONIFICACAO
        return salario_final
    def __str__(self) -> str:
        return f"== Dados Gerente == \nNome: {self.nome}\nIdade: {self.idade} \nSalario: {self.calcular_salario()}"

class Motoboy(Funcionario):
    def __init__(self, nome: str, idade: int, salario: float, cnh: str) -> None:
        super().__init__(nome, idade, salario)
        self.cnh = cnh
    
    def calcular_salario(self) -> float:
        BONIFICACAO = 1.1
        salario_final = self.salario * BONIFICACAO
        return salario_final
    def __str__(self) -> str:
        return f"== Dados Motoboy == \nNome: {self.nome}\nIdade: {self.idade} \nCNH: {self.cnh} \nSalario: {self.calcular_salario()}"





#Instanciar

# motoboy = Motoboy("Revoada", 22,5.000)
# gerente = Gerente("Da revoada", 23,10.000)

gerente = Gerente ("Silvestre", 23, 5000)
motoboy = Motoboy ("Revoada", 22,5000, "A")

# print(f"== Dados Gerente == ")
# print(f"Nome: {gerente.nome}")
# print(f"Idade: {gerente.idade}")
# print(f"Salario: {gerente.calcular_salario()}")
# print(f"== Dados Motoboy ==")
# print(f"Nome: {motoboy.nome}")
# print(f"Idade: {motoboy.idade}")
# print(f"CNH: {motoboy.cnh}")
# print(f"Salario: {motoboy.calcular_salario()}")

print(gerente)
print(motoboy)