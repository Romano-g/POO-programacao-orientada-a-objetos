from abc import ABC, abstractmethod
import contas


class Person(ABC):
    def __init__(self) -> None:
        self._name = None
        self._age = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age


class Customer(Person):
    def __init__(self) -> None:
        super().__init__()
        self.accounts = []

    def insertacc(self, *accounts):
        for acc in accounts:
            self.accounts.append(acc)

    def showaccs(self):
        print(f'Cliente: {self.name}, Idade: {self.age}')
        for acc in self.accounts:
            print(
                f'Banco: , Agência: {acc.agency}, Conta: {acc.accnumber}')


if __name__ == '__main__':  # testes
    c1 = Customer()
    c1.name = 'Caio'
    c1.age = 21
    conta1, conta2 = contas.CheckingAccount(
        1, 'C1', 250), contas.SavingAccount(1, 'S3')
    c1.insertacc(conta1, conta2)
    c1.showaccs()
