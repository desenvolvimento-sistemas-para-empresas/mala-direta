#!/bin/bash

# Script para automatizar tarefas comuns do Git

# Configurar suas informações de usuário (ajuste conforme necessário)
GIT_USERNAME="Seu Nome"
GIT_EMAIL="seu@email.com"

# Função para configurar suas informações de usuário
configurar_usuario() {
  git config --global user.name "$GIT_USERNAME"
  git config --global user.email "$GIT_EMAIL"
  echo "Configurado usuário: $GIT_USERNAME <$GIT_EMAIL>"
}

# Função para inicializar um repositório Git
inicializar_repositorio() {
  git init
  echo "Repositório Git inicializado."
}

# Função para fazer o commit de todas as mudanças
fazer_commit() {
  git add .
  git commit -m "Commit automático: $(date +'%Y-%m-%d %H:%M:%S')"
  echo "Commit realizado."
}

# Função para fazer push das mudanças para o repositório remoto
fazer_push() {
  git push origin master
  echo "Push realizado para o repositório remoto."
}

# Exibir menu de opções
menu() {
  echo "Selecione uma opção:"
  echo "1. Configurar usuário"
  echo "2. Inicializar repositório"
  echo "3. Fazer commit"
  echo "4. Fazer push"
  echo "5. Sair"
}

# Loop do menu
while true; do
  menu
  read -p "Opção: " opcao
  case $opcao in
    1) configurar_usuario ;;
    2) inicializar_repositorio ;;
    3) fazer_commit ;;
    4) fazer_push ;;
    5) exit ;;
    *) echo "Opção inválida." ;;
  esac
done