from abc import ABC, abstractmethod
import os

os.system("cls || clear")
class SalarioNaoPermitidoError (Exception):
    pass
class Endereco:
    def __init__(self, logradouro : str, numero:int, cidade : str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade
    
    def __str__(self) -> str:
        return (f"Logradouro: {self.logradouro}"
                f"Numero: {self.numero}"
                f"Cidade: {self.cidade}")
    
class Funcionario(ABC):
    def __init__(self, nome: str, email : str, salario : float, endereco : Endereco) -> None:
        self.nome = nome
        self.email = email
        self.salario = salario
        self.endereco = endereco

    def __str__(self) -> str:
        return (f"Nome: {self.nome}"
                f"Email: {self.email}"
                f"Salario: {self.salario}"
                f"Endereço: {self.endereco}")
    
    @abstractmethod
    def salario_final(self) -> None:
        pass
    def __verificar_Salario_Negativo(self, salario):
        if salario <0 or salario <=0:
            raise SalarioNaoPermitidoError("Salario nao pode ser negativo!")
        
class Motoboy(Funcionario):
    def __init__(self, nome: str, email: str, salario: float, endereco: Endereco, cnh: str) -> None:
        super().__init__(nome, email, salario, endereco)
        self.cnh = cnh

    def __str__(self) -> str:
        return (f"{super().__str__()}f\n CNH: {self.cnh}")
    def salario_final(self):
        try: 
            self.__verificar_Salario_Negativo(salario)
        except SalarioNaoPermitidoError as error:
            return f"Erro: {error}"
        return self.salario
    

motoboy = Motoboy("Silvestre","dwqdwq",-100,
                  Endereco("Rua A",  7, "Salvador"),"A")

print(motoboy)