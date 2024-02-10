#!/bin/bash

# - A variável `VENV_ACTIVATED` no script `run.sh` é uma variável de controle personalizada que criei para manter o controle do estado do ambiente virtual dentro do script. Aqui está como ela funciona e por que é útil: 
# 1. **Propósito da Variável** : O objetivo principal da `VENV_ACTIVATED` é rastrear se o script ativou o ambiente virtual (`venv`) ou não. Isso é importante porque se o ambiente virtual já estiver ativado antes de iniciar o script, geralmente você não quer que o script o desative ao terminar. Desativar um ambiente virtual previamente ativado pode interferir em outros processos ou scripts que dependem desse ambiente. 
# 2. **Como Funciona** : 
# - Quando o script começa, ele verifica se o ambiente virtual está ativo verificando a variável de ambiente `VIRTUAL_ENV`. 
# - Se `VIRTUAL_ENV` não estiver definida (ou seja, o ambiente virtual não está ativo), o script ativa o ambiente virtual e define `VENV_ACTIVATED=1`. Isso indica que o script foi responsável por ativar o ambiente. 
# - Se `VIRTUAL_ENV` já estiver definida (o que significa que o ambiente virtual já está ativo), `VENV_ACTIVATED` é definida como `0`. Isso indica que o ambiente já estava ativo antes do script iniciar e, portanto, o script não deve desativá-lo. 
# 3. **Usando a Variável** : 
# - No final do script, antes de terminar, ele verifica o valor de `VENV_ACTIVATED`. 
# - Se `VENV_ACTIVATED` for `1`, o script desativa o ambiente virtual, pois foi ele que o ativou. 
# - Se `VENV_ACTIVATED` for `0`, o script não faz nada em relação ao ambiente virtual, deixando-o como estava.

# Verificar se o ambiente virtual já está ativado
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Ativando o ambiente virtual..."
    source venv/arch/venv/bin/activate
    VENV_ACTIVATED=1
else
    echo "Ambiente virtual já está ativo."
    VENV_ACTIVATED=0
fi

# Fazer a build do projeto
# Esta etapa compila ou prepara o projeto para execução
echo "Fazendo a build do projeto..."
# Adicione aqui os comandos necessários para buildar seu projeto, exemplo:
# make build ou ./build.sh

# Executar testes (opcional)
# Executa testes automatizados para garantir a integridade do código
echo "Executando testes..."
python -m unittest discover

# Executar o script principal do projeto para mapeamento de arquivos
# Este script realiza o mapeamento de arquivos na rede
echo "Iniciando o script de mapeamento de arquivos da rede..."
python app.py

# Desativar o ambiente virtual, se foi ativado pelo script
# Isso é feito para manter o ambiente conforme estava antes da execução do script
if [ "$VENV_ACTIVATED" -eq 1 ]; then
    deactivate
fi

# Mensagem de finalização do script
echo "Script de mapeamento de arquivos da rede finalizado."
