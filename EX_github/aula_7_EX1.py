# PARTE 2


from aula_7_EX import Pessoa, CAMINHO_DADOS
import json


with open(CAMINHO_DADOS, 'r', encoding='utf8') as arquivo:
    pessoas = json.load(arquivo)


p6 = Pessoa(**pessoas[0])
p7 = Pessoa(**pessoas[1])
p8 = Pessoa(**pessoas[2])
p9 = Pessoa(**pessoas[3])
p0 = Pessoa(**pessoas[4])


print(p6.nome, p6.sobrenome, p6.idade, p6.endereco)
print(p7.nome, p7.sobrenome, p7.idade, p7.endereco)
print(p8.nome, p8.sobrenome, p8.idade, p8.endereco)
print(p9.nome, p9.sobrenome, p9.idade, p9.endereco)
print(p0.nome, p0.sobrenome, p0.idade, p0.endereco)
