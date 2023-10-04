"""
Exercício com abstração, herança, encapsulamento e polimorfismo
Criar um sistema bancario simples que tem clientes, contas e 
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente)'
e que possa sacar/depositar nessa conta. Contas corrente tem um limite extra

Conta(ABC):
    ContaCorrente
    ContaPoupanca

Pessoa(ABC):
    Cliente
        Cliente -> Conta

Banco:
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (herança)
    Pessoa tem nome e idade (com getter)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)

Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas tem agencia, numero da conta e saldo
    Contas devem ter método para depósito
    Conta (superclass) deve ter método sacar abstrato (Abstraçao e polimorfismo
    - as subclasses que implementam o método sacar)

Criar classe Banco para AGREGAR classes de clientes e de contas (AGREGAÇÃO)

Banco será responsavel, por autenticar o cliente e as contas do seguinte modo:
    Banco tem contas e clientes (agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco

Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método
"""
