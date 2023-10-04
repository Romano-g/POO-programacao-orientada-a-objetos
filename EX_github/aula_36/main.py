import clientes
import banco_check
import contas


c1 = clientes.Customer()
c1.name = 'Luiz'
c1.age = 30
cc1 = contas.CheckingAccount(111, 222, 0)
c1.conta = cc1
c2 = clientes.Customer()
c2.name = 'Maria'
c2.age = 20
cp1 = contas.SavingAccount(112, 223)
c2.conta = cp1
banco = banco_check.Bank()
banco.clientes.extend([c1, c2])
banco.contas.extend([cc1, cp1])
banco.agencias.extend([111, 222])

if banco.autenticar(c1, cc1):
    cc1.deposit(10)
    c1.conta.deposit(100)
