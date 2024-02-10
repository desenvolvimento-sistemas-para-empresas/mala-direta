# # Importa as bibliotecas necessárias
# from faker import Faker
# import json

# # Cria uma instância do Faker
# fake = Faker()

# # Função para gerar um registro de dados
# def gerar_dados(id):
#     return {
#         "id": id,
#         "nome": fake.name(),
#         "email": fake.email(),
#         "cargo": fake.job()
#     }

# # Lista para armazenar todos os registros
# dados = []

# # Gera 39 registros
# for i in range(1, 40):
#     dados.append(gerar_dados(i))

# # Escreve os dados em um arquivo JSON
# with open('dados_funcionarios.json', 'w', encoding='utf-8') as arquivo:
#     json.dump(dados, arquivo, ensure_ascii=False, indent=4)

# print("Dados gerados e salvos em 'dados_funcionarios.json'")

# -----------------------------------------------------------------------------------------------------------


# Importa as bibliotecas necessárias
from faker import Faker
import csv

# Cria uma instância do Faker
fake = Faker()

# Função para gerar um registro de dados
def gerar_dados(id):
    return {
        "id": id,
        "nomeFuncionario": fake.name(),
        "email": fake.email(),
        "cargo": fake.job()
    }

# Cabeçalhos das colunas para o arquivo CSV
cabecalhos = ['id', 'nomeFuncionario', 'email', 'cargo']

# Abre um arquivo CSV para escrita
with open('dados_funcionarios2.csv', 'w', newline='', encoding='utf-8') as arquivo:
    # Cria um objeto writer
    writer = csv.DictWriter(arquivo, fieldnames=cabecalhos)

    # Escreve os cabeçalhos no arquivo
    writer.writeheader()

    # Gera e escreve os dados de 39 funcionários
    for i in range(1, 40):
        writer.writerow(gerar_dados(i))

print("Dados gerados e salvos em 'dados_funcionarios2.csv'")
