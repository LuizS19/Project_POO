import contas #importa o módulo contas
class Pessoa: #definindo a classe Pessoa
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade
        
    @property 
    def nome(self) -> str:
        return self._nome
    
    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome.title()
    
    @property
    def idade(self) -> int:
        return self._idade
    
    @idade.setter
    def idade(self, idade: int) -> None:
        self._idade = idade
        
    def __repr__(self): #representação oficial do objeto
        class_name = type(self).__name__
        attrs = f'(nome={self._nome!r}, idade={self._idade!r})'
        return f"{class_name}{attrs}"
        
class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self._conta: contas.Conta | None = None
        
if __name__ == '__main__':
    c1 = Cliente('ana silva', 28)
    c1._conta = contas.ContaCorrente('0001', '1234-5', 1000, 500)
    print(c1.nome)
    
    