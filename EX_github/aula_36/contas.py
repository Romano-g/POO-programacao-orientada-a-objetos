from abc import ABC, abstractmethod
import os


class Account(ABC):
    def __init__(self, agency, accnumber) -> None:
        self.agency = agency
        self.accnumber = accnumber
        self.balance = 0

    @abstractmethod
    def withdrawl(self, value): ...

    def deposit(self, value):
        os.system('cls')
        self.balance += value
        self.check(f'Você depositou {value}')
        return self.balance

    def check(self, msg=None):
        if msg is None:
            print(f'Seu saldo atual é de {self.balance:.2f}')
            return

        print(f'{msg}, seu saldo atual é de {self.balance:.2f} reais!')
        return


class SavingAccount(Account):
    def withdrawl(self, value):
        os.system('cls')

        if self.balance >= value:
            self.balance -= value
            self.check(f'Você sacou {value:.2f} reais')
            return self.balance

        print('Saldo insuficiente!')
        self.check(f'Saque negado no valor de {value:.2f} reais')


class CheckingAccount(Account):
    def __init__(self, agency, accnumber, limit=0) -> None:
        super().__init__(agency, accnumber)
        self.limit = limit

    def withdrawl(self, value):
        os.system('cls')

        if self.balance + self.limit >= value:
            self.balance -= value
            self.check(f'Você sacou {value:.2f} reais')
            return self.balance

        print('Saldo insuficiente!')
        self.check(f'Saque negado no valor de {value:.2f} reais')


if __name__ == '__main__':  # testes
    ca1 = CheckingAccount(1, 2, 120)
    ca1.check()
    ca1.deposit(10)
    ca1.deposit(120.50)
    ca1.deposit(10.50)
    ca1.withdrawl(261.0)
    print()
    sa1 = SavingAccount(1, 2)
    sa1.check()
    sa1.deposit(10)
    sa1.deposit(120.50)
    sa1.deposit(10.50)
    sa1.withdrawl(141)
