from enum import Enum
import os


os.system("cls || clear")

class Setor(Enum):
    FINANCEIRO = "Financeiro"
    RECRSOS_HUMANOS = "Recursos Humanos"
    VENDAS = "Vendas"
    MARKETING = "Marketing"

class Sexo (Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"


class Funcionario:
    def __init__(self, id:int, nome:str, idade:int, salario:float, setor: Setor, sexo: Sexo) -> None:
        self.id = id
        self.nome= nome
        self.idade = idade
        self.salario = salario
        self.setor = setor
        self.sexo = sexo
    
    def __str__(self) -> str:
        return (f"\n== Dados do Funcionario ==="
                f"\nID: {self.id}"
                f"\nNome: {self.nome}"
                f"\nIdade:{self.idade}"
                f"\nSalario: {self.salario}"
                f"\nSetor: {self.setor.value}"
                f"\nSexo: {self.sexo.value}")


funcionario = Funcionario(22,"Silvestre",23,5200,Setor.FINANCEIRO, Sexo.MASCULINO)

print(funcionario)