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

    def salva_dados(caminho, *args):

        with open(
            caminho,
            'w',
            encoding='utf8'
        ) as arquivo:

            json.dump(
                *args,
                arquivo,
                indent=2,
            )
            return

    def dados_salvos(file):  # < só serve para ver todos arquivos que estão na base de dados

        with open(
            file,
            'r',
            encoding='utf8',
        ) as arquivo:

            pessoas_salvas = json.load(arquivo)
            print(*pessoas_salvas, sep='\n')
            print()
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


Pessoa.dados_salvos('.\\jsons\\aula_7_dados.json')


with open('.\\jsons\\aula_7_dados.json', 'r', encoding='utf8') as arquivo:
    pessoas = json.load(arquivo)


p6 = Pessoa(pessoas[0]['nome'], pessoas[1]['sobrenome'],
            pessoas[2]['idade'], pessoas[3]['endereco'])


print(vars(p6))
