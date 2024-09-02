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




class Funcionario(ABC):
    def __init__(self, nome:str ,telefone: str,email:str, endereco : Endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        


        

