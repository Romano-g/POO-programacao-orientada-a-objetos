from aulas.aula_36.contas import SavingsAccount, ChekingAccount, Bank, NUBANK
from clientes import Customer

c = Customer('Caio', 19)
a = Customer('Arthur', 25)
p = Customer('Pedro', 21)

c1, c2, c3 = c, a, p

BANCO_DO_BRASIL = Bank('Banco do Brasil', 2)

NUBANK.customers(c1, c2, c3)

c.addaccount(SavingsAccount('S1'))
c.addaccount(ChekingAccount('C2'))
a.addaccount(ChekingAccount('C1'))
p.addaccount(SavingsAccount('S2'))

NUBANK.accounts(c.account, a.account, p.account)
NUBANK.show()
print()
BANCO_DO_BRASIL.customers(c1, c2, c3)
BANCO_DO_BRASIL.accounts(c.account, a.account, p.account)
BANCO_DO_BRASIL.show()
