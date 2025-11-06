import contas
import pessoas

class Banco: #definindo a classe Banco
        def __init__(
            self,
            agencias: list[int] | None = None,
            clientes: list[pessoas.Pessoa] | None = None,
            contas: list[contas.Conta] | None = None,
        ):
            self.agencias = agencias or []
            self.clientes = clientes or []
            self.contas = contas or []
            
        def autenticar(self, cliente, conta): #método para autenticar cliente e conta
            if cliente not in self.clientes: #valida se o cliente pertence ao banco
                print('Cliente não é do banco')
                return False
            
            if conta not in self.contas: #valida se a conta pertence ao banco
                print('Conta não é do banco')
                return False
            
            if conta._agencia not in self.agencias: #valida se a agência pertence ao banco
                print('Agência não é do banco')
                return False
            return True #se todas as validações forem ok
        
        def checa_se_a_conta_e_do_cliente(self, cliente: pessoas.Cliente, conta: contas.Conta) -> bool:
            if cliente._conta is conta:
                return True
            return False

        def __repr__(self): #representação oficial do objeto
            class_name = type(self).__name__
            attrs = f'(nome={self.agencias!r}, idade={self._clientes!r}), {self._contas!r}'
            return f"{class_name}{attrs}"

if __name__ == '__main__': #Testes
    c1 = pessoas.Cliente('Maria Silva', 35)
    cc1 = contas.ContaCorrente('0001','9876-5',5000)
    c1.conta = cc1
    c2 = pessoas.Cliente('João Souza', 40)
    cp1 = contas.ContaPoupanca('0002','1234-5',3000)
    c2.conta = cp1
    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp1])
    banco.agencias.extend(['0001','0002'])
    
    if banco.autenticar(c1, cc1):
        c1.conta.sacar(6000)
        c1.conta.depositar(2000)
        c1.conta.sacar(6000)
        print(c1._conta)
        print('##')
    if banco.autenticar(c2, cp1):
        c2.conta.sacar(3500)
        c2.conta.depositar(1000)
        c2.conta.sacar(2500)
        print(c2._conta)
        print('##')