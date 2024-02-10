#!/bin/bash

# Função para imprimir mensagens
log() {
    echo "[$(date +'%Y-%m-%dT%H:%M:%S%z')] $1"
}

# Parar a execução se ocorrer algum erro
set -e

# Mensagem de boas-vindas
log "Iniciando a instalação do projeto..."

# Detecta o sistema operacional
OS=$(uname -s)
log "Sistema Operacional detectado: $OS"

if [[ "$OS" == "Linux" ]] || [[ "$OS" == "Darwin" ]]; then
    # Fluxo de instalação para Linux e MacOS

    # Verifica se o Python está instalado
    if ! command -v python3 &> /dev/null; then
        log "Python 3 não encontrado. Por favor, instale o Python 3."
        exit 1
    fi

    # Verifica se o git está instalado (opcional)
    if ! command -v git &> /dev/null; then
        log "Git não encontrado. Por favor, instale o Git."
        exit 1
    fi

    # Criar e ativar ambiente virtual
    log "Criando e ativando um ambiente virtual..."
    python3 -m venv venv
    source venv/bin/activate

elif [[ "$OS" == "MINGW"* ]] || [[ "$OS" == "CYGWIN"* ]] || [[ "$OS" == "MSYS"* ]]; then
    # Fluxo de instalação para Windows

    log "Preparando instalação para Windows..."

    # Verifica se o Python está instalado
    if ! command -v python &> /dev/null; then
        log "Python não encontrado. Por favor, instale o Python."
        exit 1
    fi

    # Verifica se o git está instalado (opcional)
    if ! command -v git &> /dev/null; then
        log "Git não encontrado. Por favor, instale o Git."
        exit 1
    fi

    # Criar e ativar ambiente virtual
    log "Criando e ativando um ambiente virtual..."
    python -m venv venvTest
    source venvTest/Scripts/activate

else
    log "Sistema Operacional não reconhecido ou não suportado."
    exit 1
fi

# Instalação comum para todos os sistemas operacionais
log "Instalando dependências..."
pip install -r requirements.txt

# Mensagem finalizando a instalação
log "Instalação concluída com sucesso."

# Desativa o ambiente virtual
deactivate
