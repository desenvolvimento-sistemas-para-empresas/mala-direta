# Definições
PYTHON = python3
PIP = pip3

# Instalar dependências
install:
	@echo "Instalando dependências..."
	$(PIP) install -r requirements.txt

# Executar testes
test:
	@echo "Executando testes..."
	$(PYTHON) -m unittest discover

# Executar o script principal
run:
	@echo "Executando aplicação..."
	$(PYTHON) app/main.py

# Limpar arquivos Python compilados
clean:
	@echo "Limpando arquivos..."
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -r {} +

# Ajuda
help:
@echo "Comandos disponíveis:"
@echo " make install - Instala as dependências do projeto"
@echo " make test - Executa os testes unitários"
@echo " make run - Executa o script principal"
@echo " make clean - Limpa arquivos Python compilados"

.PHONY: install test run clean help