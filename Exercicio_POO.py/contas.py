import abc
class Conta(abc.ABC): #Classe abstrata Conta
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo
        
    @abc.abstractmethod #Método abstrato sacar
    def sacar(self, valor: float) -> float: ...
    
    def depositar(self, valor: float) -> float: #Método depositar
        self._saldo += valor
        self.detalhes(f'(DEPÓSITO {valor})')
        return self._saldo
        
    def detalhes(self, msg: str='') -> None: #Método detalhes para mostrar saldo
        print(f'O seu saldo é {self._saldo:.2f} {msg}')
        
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'(nome={self._agencia!r}, idade={self._conta!r}, saldo={self._saldo!r}), {self.limite!r}'
        return f"{class_name}{attrs}"
        
class ContaPoupanca(Conta): #Conta Poupança herda de Conta
    def sacar(self, valor):
        valor_pos_saque = self._saldo - valor
        
        if valor_pos_saque >= 0: #Verifica se há saldo suficiente
            self._saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self._saldo
        
        print('Saldo insuficiente')
        self.detalhes(f'(SAQUE {valor} NEGADO)')
        return self._saldo
    
class ContaCorrente(Conta):  #Conta Corrente herda de Conta
    def __init__(self, agencia: int, conta: int, saldo: int= 0, limite: int =0):
        super().__init__(agencia, conta, saldo)
        self._limite = limite
    
    def sacar(self, valor: float): #Método sacar com limite extra
        valor_pos_saque = self._saldo - valor
        limite_maximo = -self._limite
        
        if valor_pos_saque >= limite_maximo: #Verifica se há saldo suficiente
            self._saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self._saldo
        
        print('Não foi possivel sacar o valor solicitado, limite excedido') 
        print(f'Seu limite é {-self._limite:.2f}')
        self.detalhes(f'SAQUE {valor} NEGADO')
        return self._saldo

if __name__ == '__main__': #Testes
    cp1 = ContaPoupanca('0001','1234-5',1000) #Teste da Conta Poupança
    cp1.sacar(500) 
    cp1.sacar(600) 
    print('##')
    cc1 = ContaCorrente('0003','5432-1',2000,1000) #Teste da Conta Corrente
    cc1.sacar(300) 
    cc1.depositar(800) 
    cc1.sacar(1000) 
    cc1.sacar(2000) 
    print('##')
    
    
        
