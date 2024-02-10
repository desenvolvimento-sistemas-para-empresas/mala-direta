import pandas as pd
from abc import ABC, abstractmethod

class FuncionarioDataObserver(ABC):
    @abstractmethod
    def update(self, data):
        pass

class CSVFuncionarioDataCreator(FuncionarioDataObserver):
    def __init__(self, filepath):
        self.filepath = filepath

    def update(self, data):
        data.to_csv(self.filepath, index=False)
        print(f"Dados salvos em {self.filepath}")

class FuncionarioData(ABC):
    def __init__(self):
        self.observers = []
        self._data = None

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self._data)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()

    @abstractmethod
    def create_data(self):
        pass

class MyFuncionarioData(FuncionarioData):
    def create_data(self):
        data = {
            "id": [1, 2, 3, 4, 5],
            "nomeFuncionario": ["João Silva", "Maria Oliveira", "Pedro Costa", "Ana Santos", "Luiz Pereira"],
            "email": ["joao.silva@example.com", "maria.oliveira@example.com", "pedro.costa@example.com", 
                      "ana.santos@example.com", "luiz.pereira@example.com"],
            "cargo": ["Analista de Sistemas", "Gerente de Projetos", "Desenvolvedor Web", 
                      "Analista de Dados", "Designer Gráfico"]
        }
        self.data = pd.DataFrame(data)

# Caminho para salvar o arquivo CSV
csv_file_path = '/home/estevam/Área de trabalho/Projetos/send-email/src/data/dados_funcionarios.csv'

# Criação e uso das classes
creator = CSVFuncionarioDataCreator(csv_file_path)
funcionario_data = MyFuncionarioData()
funcionario_data.attach(creator)
funcionario_data.create_data()
