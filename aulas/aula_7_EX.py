"""
Exercício - Salve sua classe em JSON
Salve os dados da sua classe em JSON e depois
crie novamente as instâncias da classe com os dados salvos.
Faça isso em arquivos separados.
"""

# PARTE 1


import json


class Pessoa:
    def __init__(self, nome, sobrenome, idade, endereco):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.endereco = endereco

    def salva_dados(caminho, *args):

        with open(
            caminho,
            'w',
            encoding='utf8',
        ) as arquivo:

            json.dump(
                *args,
                arquivo,
                indent=2,
                ensure_ascii=False
            )
            return


p1 = Pessoa('Vitória', 'Romano', 23, 'Nova Iguaçu')
p2 = Pessoa('Gustavo', 'Mioto', 35, 'Goiânia')
p3 = Pessoa('Diego', 'Araujo', 42, 'Minas Gerais')
p4 = Pessoa('Bruna', 'Cerquilho', 18, 'Salvador')
p5 = Pessoa('Roberto', 'José', 65, 'Amapá')


Pessoa.salva_dados(
    '.\\jsons\\aula_7_dados.json',
    (
        vars(p1),
        vars(p2),
        vars(p3),
        vars(p4),
        vars(p5),
    ))
