from setuptools import setup, find_packages

setup(
    name='sendEmail',
    version='0.1.0',
    author='Estevam Souza',
    author_email='estevamsouzalaureth@gmail.com',
    description='Envio de e-mail em massa automaticamente',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://link-para-seu-projeto.com',
    packages=find_packages(),
    install_requires=[
        'openpyxl',
        'python-dotenv',
        'schedule',
        'et-xmlfile'
        # Adicione outras dependências necessárias aqui
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'meuapp = meu_pacote.app:main',
        ],
    },
    classifiers=[
        # Classificadores adicionais
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        # Classificadores de Intenção de Público
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Classificadores de Licença
        'License :: OSI Approved :: MIT License',

        # Classificadores de Sistema Operacional
        'Operating System :: OS Independent',

        # Classificadores de Versão Python
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.6'
)


"""
Este é um exemplo básico e você deve adaptá-lo para as especificações do seu projeto. Por exemplo, substitua 'SeuProjeto', 'Seu Nome', 'seu.email@example.com',
e 'https://link-para-seu-projeto.com' pelas informações reais do seu projeto.

Além disso, na seção install_requires, liste todas as bibliotecas externas que seu projeto depende, como openpyxl, python-dotenv, e schedule.

Depois de criar o arquivo setup.py, você pode instalar seu projeto em outro ambiente usando pip. Isso pode ser útil para testes em ambientes diferentes ou para preparar o projeto para distribuição.
"""


"""
Definição de Metadados do Projeto: Inclui o nome do projeto, versão, autor, descrição, etc.

Inclusão de Pacotes: Usa find_packages() para incluir automaticamente todos os pacotes Python do projeto.

Dependências: Lista todas as dependências necessárias no install_requires. Estas serão instaladas automaticamente quando alguém instalar seu pacote.

Classificadores: Fornece metadados adicionais sobre o seu pacote.

Versão Python Requerida: Especifica a versão mínima do Python necessária.

Antes de executar este script, certifique-se de que o arquivo README.md exista, pois ele é referenciado para a descrição longa. Adapte os valores dos metadados para refletir as informações do seu projeto. Depois, você pode instalar seu projeto e suas dependências executando python setup.py install.
"""



"""
- Após configurar o `setup.py` para o seu projeto Python, o próximo passo é instalar o projeto e suas dependências e, em seguida, verificar se está tudo funcionando corretamente. Aqui estão as etapas detalhadas:
### 1. Instalar o Projeto 
- **No diretório do projeto**  (onde o arquivo `setup.py` está localizado), execute o seguinte comando:

```bash
python setup.py install
```

Isso instalará o projeto junto com todas as dependências listadas em `install_requires` no `setup.py`.
### 2. Testar a Instalação 
- Após a instalação, teste se o seu projeto está funcionando conforme esperado. Como você testará depende da natureza do seu projeto. Por exemplo:
- Se for uma biblioteca, tente importá-la em um script Python para verificar se está funcionando.
- Se o seu projeto incluir um script executável ou uma aplicação de linha de comando, tente executá-lo.
### 3. Uso em Ambiente Virtual (Recomendado) 
- É uma boa prática usar ambientes virtuais em projetos Python para evitar conflitos de dependência. Você pode criar um ambiente virtual e instalar seu projeto nele:

```bash
python -m venv venv
source venv/bin/activate  # No Windows use 'venv\Scripts\activate'
python setup.py install
```

Isso isola as dependências do seu projeto das bibliotecas globais do Python.
### 4. Desenvolvimento e Testes Contínuos 
- Se você estiver em fase de desenvolvimento, pode querer instalar o projeto em modo de edição:

```bash
python setup.py develop
```

Ou usando pip:

```bash
pip install -e .
```

Isso permite que você faça mudanças no código e veja os efeitos dessas mudanças sem precisar reinstalar o pacote após cada alteração.
### 5. Documentação
- Se ainda não o fez, é uma boa ideia criar uma documentação para o seu projeto. Isso inclui instruções de instalação, uso, e descrição de qualquer funcionalidade importante.
### 6. Versionamento e Controle de Fonte
- Se você estiver usando controle de versão (como git), lembre-se de fazer commit e push das suas alterações no repositório.
### 7. Distribuição (Opcional) 
- Se você planeja compartilhar seu projeto com outros usuários ou desenvolvedores, pode considerar distribuí-lo através do PyPI. Isso envolve criar um arquivo `MANIFEST.in` para incluir arquivos não-Python e usar `twine` para fazer o upload do seu pacote para o PyPI.
"""



"""
- Depois de instalar seu projeto usando `setup.py`, a maneira de executá-lo depende de como você configurou a distribuição e o ponto de entrada do projeto. Vou cobrir alguns cenários comuns, incluindo o caso de ter um arquivo `app.py` como ponto de entrada do seu projeto.
### 1. Script Executável Direto

Se o `app.py` for um script executável (com uma linha `if __name__ == "__main__":` no final), e você não definiu nenhum ponto de entrada no `setup.py`, você pode simplesmente executar o script diretamente após a instalação. Navegue até o diretório onde o `app.py` está localizado e execute:

```bash
python app.py
```


### 2. Ponto de Entrada Definido no `setup.py`

Se você definiu um ponto de entrada no seu `setup.py`, por exemplo, algo assim:

```python
setup(
    # ... outras configurações ...
    entry_points={
        'console_scripts': [
            'meuapp = meu_pacote.app:main',
        ],
    },
)
```



Neste caso, após a instalação, você pode executar o seu aplicativo diretamente a partir da linha de comando, independentemente de onde você estiver no sistema de arquivos:

```bash
meuapp
```



Aqui, `meuapp` seria o comando que você definiu, e `meu_pacote.app:main` indica que o Python deve executar a função `main()` no módulo `app.py` dentro do pacote `meu_pacote`.
### 3. Executando via Python -m

Se o seu pacote foi instalado corretamente e é um módulo Python importável, você pode executá-lo usando:

```bash
python -m meu_pacote.app
```



Neste comando, `meu_pacote.app` deve ser substituído pelo caminho importável para o seu script `app.py`.
### Dicas Adicionais
- Certifique-se de que o ambiente virtual no qual você instalou o seu pacote está ativado ao tentar executar o aplicativo. 
- Se você encontrar problemas, verifique se o `app.py` está no caminho certo e é parte do pacote que você definiu no `setup.py`. 
- Lembre-se de substituir `meuapp`, `meu_pacote`, e `app` pelos nomes reais usados no seu projeto. 
- Se você tiver dependências no `requirements.txt` que não estão no `install_requires` do `setup.py`, você precisará instalá-las separadamente usando `pip install -r requirements.txt`.
"""