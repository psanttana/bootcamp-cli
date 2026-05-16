# FoodBridge CLI - Gerenciador de Doações de Alimentos

## 🚀 Etapa Intermediária - Bootcamp
Esta versão inclui a integração com a API pública **ViaCEP** para validação de endereços e testes de integração automatizados.

## 📋 Visão Geral

O **FoodBridge CLI** é uma aplicação de linha de comando desenvolvida em Python para conectar doadores de alimentos (como restaurantes e supermercados) a entidades receptoras (ONGs, abrigos, bancos de alimentos). Seu objetivo principal é combater o desperdício de alimentos e a insegurança alimentar, facilitando o registro, a listagem e a coleta de doações de forma eficiente e organizada.

## 💡 Problema Real e Proposta da Solução

### Qual problema estou tentando resolver?

O Brasil enfrenta um paradoxo alarmante: enquanto milhões de pessoas sofrem com a fome, uma quantidade significativa de alimentos é desperdiçada diariamente. Restaurantes, supermercados e outros estabelecimentos frequentemente descartam alimentos que ainda estão em boas condições para consumo, seja por proximidade da data de validade, pequenos defeitos estéticos ou excesso de estoque. A falta de um sistema eficiente para gerenciar e direcionar essas sobras contribui para o agravamento da insegurança alimentar e para o impacto ambiental do descarte de orgânicos.

### Quem é afetado por esse problema?

*   **Pessoas em situação de vulnerabilidade social:** São as principais vítimas da insegurança alimentar, sem acesso regular a alimentos nutritivos.
*   **Doadores (restaurantes, supermercados):** Enfrentam custos com descarte, perda de valor de produtos e, muitas vezes, o desejo de contribuir socialmente, mas sem ferramentas adequadas.
*   **Entidades receptoras (ONGs, abrigos):** Têm dificuldade em encontrar fontes consistentes de doações e em gerenciar a logística de coleta.
*   **Meio ambiente:** O descarte de alimentos contribui para a emissão de gases de efeito estufa em aterros sanitários.

### Como minha aplicação ajuda, mesmo que de forma simples?

O FoodBridge CLI atua como uma ponte digital, simplificando o processo de doação e coleta de alimentos. Ele permite que doadores registrem facilmente os itens disponíveis, suas quantidades e datas de validade. As entidades receptoras podem visualizar as doações disponíveis e marcá-las como coletadas, garantindo que os alimentos cheguem a quem precisa de forma ágil. Embora seja uma solução simples, ela oferece uma ferramenta prática para organizar e otimizar o fluxo de doações, reduzindo o desperdício e alimentando pessoas.

## 🎯 Público-Alvo

*   Pequenos e médios restaurantes, padarias, mercados e hortifrutis que desejam doar alimentos.
*   Organizações não governamentais (ONGs), abrigos, cozinhas comunitárias e bancos de alimentos que buscam doações.
*   Voluntários e indivíduos que atuam na logística de coleta e distribuição de alimentos.

## ✨ Funcionalidades Principais

*   **Registro de Doações com Endereço:** Permite que doadores adicionem novos itens, especificando nome do doador, item, quantidade, data de validade e endereço (validado via CEP).
*   **Integração com ViaCEP:** Busca automática de endereço a partir do CEP informado.
*   **Listagem de Doações:** Exibe todas as doações disponíveis, com detalhes como ID, item, quantidade, validade, doador e endereço.
*   **Coleta de Doações:** Permite que entidades receptoras marquem uma doação como coletada, registrando o nome da entidade.
*   **Armazenamento Persistente:** Utiliza um arquivo JSON (`donations.json`) para armazenar os dados das doações.

## 🛠 Tecnologias Utilizadas

*   **Linguagem:** Python 3.x
*   **Bibliotecas Externas:** `requests` (para integração com API)
*   **Gerenciamento de Dependências:** `pip` e `requirements.txt`
*   **Testes:** `pytest` (incluindo testes de integração)
*   **Análise Estática de Código (Linting):** `ruff`
*   **Integração Contínua:** GitHub Actions

## ⚙️ Instalação

Para configurar e executar o FoodBridge CLI em sua máquina local, siga os passos abaixo:

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/psanttana/bootcamp-cli.git
    cd bootcamp-cli
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows: .\venv\Scripts\activate
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Como Executar

Após a instalação das dependências, você pode iniciar a aplicação:

```bash
python src/app.py
```

## 🧪 Como Rodar os Testes

Para executar os testes automatizados (unitários e de integração):

```bash
pytest
```

## 🧹 Como Rodar o Lint

Para verificar a qualidade do código com `ruff`:

```bash
ruff check .
```

## 📦 Deploy

Como esta é uma aplicação CLI, o "deploy" consiste na disponibilização do código no GitHub. Para aplicações que necessitam de execução em nuvem, recomenda-se o uso de plataformas como **Render** ou **Heroku** para scripts Python, ou simplesmente a execução via **Docker**.

## 📄 Versão Atual

`1.1.0` (Etapa Intermediária)

## 👤 Autor

**Pedro Saldanha Santana**

## 🔗 Link do Repositório Público

[https://github.com/psanttana/bootcamp-cli](https://github.com/psanttana/bootcamp-cli)

---

## 🖥 Exemplos de Uso (Saída do Terminal)

```
=== FoodBridge CLI - Gerenciador de Doações de Alimentos ===
1. Adicionar Doação
2. Listar Doações Disponíveis
3. Coletar Doação
4. Buscar Endereço por CEP
5. Sair

Escolha uma opção: 4
Digite o CEP para buscar o endereço: 01001000
📍 Endereço encontrado: Praça da Sé, Sé, São Paulo - SP

Escolha uma opção: 1
Nome do Doador: Padaria Central
Item Alimentar: Pães
Quantidade: 20 unidades
Data de Validade (AAAA-MM-DD): 2026-04-15
Deseja informar o CEP para o endereço? (s/n): s
Digite o CEP: 01001000
✅ Doação registrada com sucesso!
```
