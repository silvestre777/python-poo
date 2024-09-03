import os

os.system("cls || clear")

#Criando sua propria exceção.
class ValorNegativoError (Exception):
    pass
class SaldoInsuficienteError(Exception):
    pass
    

class Conta:
    def __init__(self, numero_da_conta:int,agencia: int) -> None:
        self.numero_da_conta = numero_da_conta
        self.agencia = agencia
        self._saldo = 0 #Atributo protegido "_"
    
    @property # puxa o metodo sem precisar do ()
    def saldo(self): # Metodo para nao acessar diretamente da class init
        return self._saldo
    
    def sacar(self, valor) -> float:
        # if valor > self.saldo:
        #     return f"Saldo insuficiente."
        #try - except - Tratamento de excessões
        #Lançando um erro na tela do usuario. Raise # Lançador de erros, caiu em uma excessao de uma regra estabelecida.
        try: 
            self.__verificar_saque(valor)
        except SaldoInsuficienteError as error:
            return f"Erro: {error}"
        self._saldo -= valor
        return self._saldo
    #Criar metodo para verificar saldo
    def __verificar_saque(self,valor): #Método privado. Quando tem 2 __ na frente o metodo é privado.
        if valor > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente.")
        else: 
            return f"Saque concluido!"
    

    def depositar(self, valor:float):
        try:
            self.__verificar_depositar(valor)
        except ValorNegativoError as error:
            return f"Erro: {error}"
        
        self._saldo += valor
        return self._saldo
    def __verificar_depositar(self,valor):
        if valor < 0 or valor <= 0:
            raise ValorNegativoError(f"Não é possivel depositar valor negativo ou igual a 0.")
class ContaCorrente(Conta):
    pass
class ContaPoupanca(Conta):
    pass

#intanciar classes

conta_corrente = ContaCorrente(2222, 2222)
conta_poupanca = ContaPoupanca(2222,2222)


print(f"Saldo: {conta_corrente.saldo}")

# print(conta_corrente.sacar(200))
print(conta_corrente.depositar(-10))

