from abc import ABC,abstractmethod
import os
os.system("cls || clear")

class Endereco:
    def __init__(self, logradouro: str, numero : str, complemento: str,cep:str, cidade:str):
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade


    def exibir_endereco(self) -> str:
        return f"Logradouro: {self.logradouro}\nNumero:{self.numero}\nComplemento: {self.complemento}\nCEP: {self.cep}\nCidade: {self.cidade}"




class Funcionario(ABC):
    def __init__(self, nome:str ,telefone: str,email:str, endereco : Endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
    @abstractmethod
    def calcular_salario(self) -> float:
        pass



class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, salario_base: float, crm : str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crm=crm
        self.salario_base = salario_base
    def calcular_salario(self) -> float:
        return self.salario_base
    def __str__(self) -> str:
        return f"\n== Dados Medico == \nNome: {self.nome}\nTelefone: {self.telefone}\nEmail: {self.email}\n{self.endereco.exibir_endereco()}\nSalario base: {self.salario_base}\nCRM: {self.crm}"

class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, salario_base: float, crea: str)-> None:
        super().__init__(nome, telefone, email, endereco)
        self.crea = crea
        self.salario_base = salario_base

    def __str__(self) -> str:
        return (f"== Dados Engenheiro == \nNome: {self.nome}\nTelefone: {self.telefone}\nEmail: {self.email}\n{self.endereco.exibir_endereco()}\nSalario base: {self.salario_base}\nCREA: {self.crea}")

engenheiro = Engenheiro("Silvestre", "71983169204", "ducorte99@gmail.com", Endereco("Rua A", 7, "casa", "41180600","Salvador",),5000, "422")
medico = Medico("Silvestre", "5484984","dmwqomdwq@dmwqodm,wqo", Endereco("Rua B", 77,"dqwdwq","321321","Salvador"),5000,"321")

print(engenheiro)
print(medico)


        

