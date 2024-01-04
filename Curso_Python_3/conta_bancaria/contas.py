import abc
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


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
        print(f'O seu saldo é: {locale.currency(self.saldo, grouping=True)}',
              f'{msg}',
              '\nLimite disponível de:',
              f'{locale.currency(self.limite, grouping=True)}')
        return None

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.num_conta!r},{self.saldo!r})'
        return f'{class_name}{attrs}'


class ContaPoupanca(Conta):
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

        print('Saldo insuficiente.')
        self.detalhes(
            f'(SAQUE NEGADO {locale.currency(valor, grouping=True)})')
        return None


class ContaCorrente(Conta):
    """_summary_

    Args:
        Conta (_type_): _description_
    """

    def __init__(self, agencia: int,
                 num_conta: int, saldo: float = 0,
                 limite: float = 0):
        super().__init__(agencia, num_conta, saldo)
        self.limite = limite
        self.limite_inicial = limite

    def deposito(self, valor):
        if (self.limite != self.limite_inicial) and \
                ((self.saldo + valor) >= 0):
            self.limite = self.limite_inicial
            return super().deposito(valor)
        super().deposito(valor)
        return None

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
        if valor_pos_s_limite >= 0 and self.limite == self.limite_inicial:
            self.saldo -= valor
            self.limite += self.saldo
            self.detalhes(
                f'(SAQUE DE {locale.currency(valor, grouping=True)})')
            return self.saldo
        if valor_pos_s_limite >= 0 and self.limite != self.limite_inicial:
            self.saldo -= valor
            self.limite -= valor
            self.detalhes(
                f'(SAQUE DE {locale.currency(valor, grouping=True)})')
            return self.saldo

        self.detalhes(
            f'(SAQUE NEGADO {locale.currency(valor, grouping=True)})')
        print('Saldo insuficiente.')
        return None

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.num_conta!r},{self.saldo!r},'\
            f'{self.limite!r})'
        return f'{class_name}{attrs}'


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
    cc1.sacar(10000)
    cc1.sacar(400)
    cc1.deposito(1000)
    # cc1.deposito(900)
    # cc1.sacar(500)
    print(cc1.__dict__)
