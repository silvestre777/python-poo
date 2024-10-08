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
        return (f"\nLogradouro: {self.logradouro}"
                f"\nNumero: {self.numero}"
                f"\nCidade: {self.cidade}")
    
class Funcionario(ABC):
    def __init__(self, nome: str, email : str, salario : float, endereco : Endereco) -> None:
        self.nome = nome
        self.email = email
        self.salario = salario
        self.endereco = endereco

    def __str__(self) -> str:
        return (f"\nNome: {self.nome}"
                f"\nEmail: {self.email}"
                f"\nSalario: {self.salario}"
                f"\nEndereço: {self.endereco}")
    
    @abstractmethod
    def salario_final(self) -> float:
        pass
        
class Motoboy(Funcionario):
    def __init__(self, nome: str, email: str, salario: float, endereco: Endereco, cnh: str) -> None:
        super().__init__(nome, email, salario, endereco)
        self.cnh = cnh

    def __str__(self) -> str:
        return (f"{super().__str__()}\n CNH: {self.cnh}")
    
        
    def salario_final(self) -> float:
        try: 
            self.salario = self.__verificar_Salario_Negativo(self.salario)
            return self.salario
        except SalarioNaoPermitidoError as error:
            return print(f"Erro: {error}")  # Retorna 0.0 em caso de erro, ajuste conforme necessário)
            
    def __verificar_Salario_Negativo(self, salario: float) -> float:
        if salario <0:
            raise SalarioNaoPermitidoError("Salario nao pode ser negativo!")
    
motoboy = Motoboy("Silvestre","dwqdwq",-1, 
                  Endereco("Rua A",  7, "Salvador"),"A")
motoboy.salario_final()
print(motoboy)