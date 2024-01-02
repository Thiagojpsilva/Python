import abc
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
# locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


class Conta(abc.ABC):
    """_summary_

    Args:
        abc (_type_): _description_
    """

    def __init__(self, agencia: int, num_conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.num_conta = num_conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor: float) -> float:
        """_summary_

        Args:
            valor (float): _description_

        Returns:
            float: _description_
        """
        ...

    def deposito(self, valor: float) -> None:
        """_summary_

        Args:
            valor (float): _description_
        """
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO DE {locale.currency(valor, grouping=True)})')

    def detalhes(self, msg: str = '') -> None:
        """_summary_

        Args:
            msg (str, optional): _description_. Defaults to ''.

        Returns:
            _type_: _description_
        """
        if self.__class__.__name__ == 'ContaPoupanca':
            print(f'O seu saldo é: {locale.currency(
                self.saldo, grouping=True)} {msg}')
            return None
        print(f'O seu saldo é: {locale.currency(self.saldo, grouping=True)} {
              msg} \nLimite disponivel de: {locale.currency(self.limite,
                                                            grouping=True)}')


class ContaPoupanca (Conta):
    """_summary_

    Args:
        Conta (_type_): _description_
    """

    def sacar(self, valor):

        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(
                f'(SAQUE DE {locale.currency(valor, grouping=True)})')
            return self.saldo

        print(f'Saldo insuficiente.')
        self.detalhes(
            f'(SAQUE NEGADO {locale.currency(valor, grouping=True)})')


class ContaCorrente(Conta):
    """_summary_

    Args:
        Conta (_type_): _description_
    """

    def __init__(self, agencia: int, num_conta: int, saldo: float = 0, limite: float = 0):
        """_summary_

        Args:
            agencia (int): _description_
            num_conta (int): _description_
            saldo (float, optional): _description_. Defaults to 0.
            limite (float, optional): _description_. Defaults to 0.
        """
        super().__init__(agencia, num_conta, saldo)
        self.limite = limite
        self.limite_inicial = limite

    def deposito(self, valor):
        """_summary_

        Args:
            valor (_type_): _description_

        Returns:
            _type_: _description_
        """
        if (self.limite != self.limite_inicial) and ((self.saldo + valor) >= 0):
            self.limite = self.limite_inicial
            return super().deposito(valor)
        super().deposito(valor)

    def sacar(self, valor):
        """_summary_

        Args:
            valor (_type_): _description_

        Returns:
            _type_: _description_
        """
        valor_pos_saque = self.saldo - valor
        valor_pos_s_limite = self.limite - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(
                f'(SAQUE DE {locale.currency(valor, grouping=True)})')
            return self.saldo

        elif valor_pos_s_limite >= 0 and self.limite == self.limite_inicial:
            self.saldo -= valor
            self.limite += self.saldo
            self.detalhes(
                f'(SAQUE DE {locale.currency(valor, grouping=True)})')
            return self.saldo

        elif valor_pos_s_limite >= 0 and self.limite != self.limite_inicial:
            self.saldo -= valor
            self.limite -= valor
            self.detalhes(
                f'(SAQUE DE {locale.currency(valor, grouping=True)})')
            return self.saldo

        else:
            self.detalhes(
                f'(SAQUE NEGADO {locale.currency(valor, grouping=True)})')
            print(f'Saldo insuficiente.')


if __name__ == '__main__':
    # cp1 = ContaPoupanca(111,222)
    # cp1.sacar(100)
    # cp1.deposito(1000)
    # cp1.deposito(900)
    # cp1.sacar(500)
    # print(cp1.__dict__)

    print('#'*10, 'CONTA CORRENTE', '#'*10)

    cc1 = ContaCorrente(111, 333, 0, 800)
    # cc1.sacar(1000)
    cc1.sacar(300)
    cc1.sacar(400)
    cc1.deposito(1000)
    # cc1.deposito(900)
    # cc1.sacar(500)
    print(cc1.__dict__)
