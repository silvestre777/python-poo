from enum import Enum
import os

os.system("cls || clear")
class Sexo(Enum):

    MASCULINO = "Masculino"
    FEMININO = "Feminino"


class Pessoa:

    def __init__(self, nome : str, idade : int, sexo: Sexo) -> None:
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def __str__(self) -> str:
        return (f"\n None: {self.nome}"
                f"\n Idade: {self.idade}"
                """"value ele define o valor que foi colocado no enum, caso vc queira que apareca a primeira opcao, coloca self.sexo.name caso queira que apareca o que aparece depois do igual, colocar value"""
                f"\n Sexo: {self.sexo.value}")
    

#instanciando a pessoa


pessoa1= Pessoa("Silvestre", 23, Sexo.MASCULINO)

print(pessoa1)


