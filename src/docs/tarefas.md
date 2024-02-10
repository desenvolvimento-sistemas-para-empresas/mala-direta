# Tasks

## Fácil

[] Deixar tudo documentado **`Em desenvolvimento`**

## Médio

* A ideia seria pegar o dado resultante dessas tabelas/gráficos e utilizar, em duas formas:
 
  - [] - 1° É usar esse reporte por e-mail para as agências do IBGE (como um resumo de fechamento de mês deles) **`A forma do app está funcionando`**  **`Só que precisa da senha de e-mail do IBGE`**
  - [] - 2° Mais pra frente, seria apresentar esse dado em um dashboard que eles mesmos pudessem acessar, sem precisar ficar populando por e-mail **`Utilizar Streamlit`**

## Difício

"Comecei a fuçar um pouco o streamlit, mas pra mim é tudo novo pois não sei fazer nada em servidor etc, sempre rodo tudo localmente aqui".

[] O principal objetivo era utilizar a caixa de e-mail do ibge mandando para destinatário dentro e fora do ibge **`Objetivo maior`**

* Pegar a senha de aplicativo para ter acesso ao envio de e-mails

- A primeira saida por e-mail é a mais imediata,
então se existir essa forma de fazer mala direta via py com a nossa caixa do ibge,
"tu vai abrir uns trocentos caminhos legais pra gente"

Então, aí acho que talvez fossem dois caminhos:

  * 1° caso:

    [] - Se for pra geração de envio de email utillizando as bases de CSV que temos aqui, poderia ter tudo localmente mesmo, eu acho. **`Dúvida maior`** 
    **`Seria para não usar um servidor mas sim os dados do arquivo CSV`**

  * Outro caso:

    [] - Se for esse outro passo de dash, acho que precisaria hostear em algum lugar pra ficar independente do meu pc né, senão eu desligo e cai tudo rs
  
  * Melhor caso:

    - Utilizar um servidor

* Envios de teste se quiser, felipe.teixeira@ibge.gov.br

## FaQ

1. Como posso pegar uma senha para envio de e-mail?
2. Vai precisar usar o Streamlit para a construção de dashboard elegante?
3. Como iremos colocar o projeto em um servidor?

---

# O que já foi implementado

1. Desenvolvimento da arquitetura do projeto
2. Uso de senha de aplicativo usando o Outlook e o gmail (Funcionando)

---

# O que falta

---

# Ideias

1. Usar uma nova versão para usar banco de dados, Versão 2 do app
2. Usar uma nova versão para usar streamlit, Versão 3 do app