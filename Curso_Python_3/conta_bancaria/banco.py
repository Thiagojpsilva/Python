import pessoas
import contas


class Banco:
    """_summary_
    """

    def __init__(self,
                 agencias: list[int] | None = None,
                 clientes: list[pessoas.Pessoa] | None = None,
                 contas: list[contas.Conta] | None = None
                 ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta):
        """_summary_

        Args:
            conta (_type_): _description_

        Returns:
            _type_: _description_
        """
        if conta.agencia in self.agencias:
            print('_checa_agencia: True')
            return True
        print('_checa_agencia: False')
        return False

    def _checa_cliente(self, cliente):
        """_summary_

        Args:
            cliente (_type_): _description_

        Returns:
            _type_: _description_
        """
        if cliente in self.clientes:
            print('_checa_cliente: True')
            return True
        print('_checa_cliente: False')
        return False

    def _checa_conta(self, conta):
        """_summary_

        Args:
            conta (_type_): _description_

        Returns:
            _type_: _description_
        """
        if conta in self.contas:
            print('_checa_conta: True')
            return True
        print('_checa_conta: False')
        return False

    def _checa_se_conta_cliente(self, cliente, conta):
        """_summary_

        Args:
            cliente (_type_): _description_
            conta (_type_): _description_

        Returns:
            _type_: _description_
        """
        if conta is cliente.conta:
            print('_checa_se_conta_cliente: True')
            return True
        print('_checa_se_conta_cliente: False')
        return False

    def autenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta):
        """_summary_

        Args:
            cliente (pessoas.Pessoa): _description_
            conta (contas.Conta): _description_

        Returns:
            _type_: _description_
        """
        return self._checa_agencia(conta) and \
            self._checa_conta(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_se_conta_cliente(cliente, conta)

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    #    p1 = Pessoa('Thiago', 37)
    #    print(p1.nome, p1.idade)
    c1 = pessoas.Cliente('Luiz', 30)
    cc1 = contas.ContaCorrente(1212, 1220)
    c1.conta = cc1

    c2 = pessoas.Cliente('Jose', 20)
    cp1 = contas.ContaPoupanca(1020, 1111)
    c2.conta = cp1
    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp1])
    banco.agencias.extend([1212, 1020])

    print(banco.autenticar(c1, c1.conta))

    if banco.autenticar(c1, cc1):
        cc1.deposito(10000)
        print(c1.conta)
