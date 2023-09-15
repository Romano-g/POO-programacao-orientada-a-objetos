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

    def salva_dados(dict):

        with open(
            '.\\jsons\\aula_7_dados.json',
            'w',
            encoding='utf8'
        ) as arquivo:

            json.dump(
                dict,
                arquivo,
                indent=2,
            )


p1 = Pessoa('Vitória', 'Romano', 23, 'Nova Iguaçu')
Pessoa.salva_dados(p1.__dict__)
