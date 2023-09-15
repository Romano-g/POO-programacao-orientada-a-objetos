"""
Exercício - Salve sua classe em JSON
Salve os dados da sua classe em JSON e depois
crie novamente as instâncias da classe com os dados salvos.
Faça isso em arquivos separados.
"""
import json


class Pessoa:
    def __init__(self, nome, sobrenome, idade, endereco):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.endereco = endereco

    def salva_dados(*args):

        with open(
            '.\\jsons\\aula_7_dados.json',
            'w',
            encoding='utf8'
        ) as arquivo:

            json.dump(
                *args,
                arquivo,
                indent=2,
            )

    def dados_salvos(file):

        with open(
            file,
            'r',
            encoding='utf8',
        ) as arquivo:

            pessoas_salvas = json.load(arquivo)
            print(*pessoas_salvas, sep='\n')


p1 = Pessoa('Vitória', 'Romano', 23, 'Nova Iguaçu')
p2 = Pessoa('Gustavo', 'Mioto', 35, 'Goiânia')
p3 = Pessoa('Diego', 'Araujo', 42, 'Minas Gerais')
p4 = Pessoa('Bruna', 'Cerquilho', 18, 'Salvador')
p5 = Pessoa('Roberto', 'José', 65, 'Amapá')


Pessoa.salva_dados((
    p1.__dict__,
    p2.__dict__,
    p3.__dict__,
    p4.__dict__,
    p5.__dict__,
))


Pessoa.dados_salvos('.\\jsons\\aula_7_dados.json')
