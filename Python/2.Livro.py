import os
os.system("cls || clear")

class Livro:
    def __init__(self,titulo:str,autor:str,numeroDePaginas:int,preco:float):
        self.titulo = titulo
        self.autor = autor
        self.numeroDePaginas = numeroDePaginas
        self.preco = preco

    #Criando uma função para exibir os resultados
    def exibir_resultados(self) -> str:
        return f"Titulo do livro: {self.titulo} \nAutor do livro: {self.autor} \nNumero de paginas: {self.numeroDePaginas} \nPreço: {self.preco}"


#Instanciar a class
#Criando uma variavel para puxar dos dados da classe
conteudo = Livro("O poder do Habito","Charles Duhigg",350,75.5)
conteudo1 = Livro("O segredo da mente milionaria","dwqdq",270,75.5)

print(f"=== Exibindo Resultados ===")
#Exibindo da forma antiga
#print(f"Titulo do livro: {conteudo.titulo}")
#print(f"Autor do livro: {conteudo.autor}")
#print(f"Numero de paginas: {conteudo.numeroDePaginas}")
#print(f"Preço: {conteudo.preco}")

print(conteudo.exibir_resultados())
print(f"\n")
print(conteudo1.exibir_resultados())

