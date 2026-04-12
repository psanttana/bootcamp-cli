# FoodBridge CLI - Gerenciador de Doações de Alimentos

## 🎯 Visão Geral

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

## 👥 Público-Alvo

*   Pequenos e médios restaurantes, padarias, mercados e hortifrutis que desejam doar alimentos.
*   Organizações não governamentais (ONGs), abrigos, cozinhas comunitárias e bancos de alimentos que buscam doações.
*   Voluntários e indivíduos que atuam na logística de coleta e distribuição de alimentos.

## ✨ Funcionalidades Principais

*   **Registro de Doações:** Permite que doadores adicionem novos itens, especificando nome do doador, item, quantidade e data de validade.
*   **Listagem de Doações:** Exibe todas as doações disponíveis, com detalhes como ID, item, quantidade, validade e doador.
*   **Coleta de Doações:** Permite que entidades receptoras marquem uma doação como coletada, registrando o nome da entidade.
*   **Armazenamento Persistente:** Utiliza um arquivo JSON (`donations.json`) para armazenar os dados das doações, garantindo que as informações não sejam perdidas ao encerrar a aplicação.

## 🛠️ Tecnologias Utilizadas

*   **Linguagem:** Python 3.x
*   **Gerenciamento de Dependências:** `pip` e `requirements.txt`
*   **Testes:** `pytest`
*   **Análise Estática de Código (Linting):** `ruff`
*   **Integração Contínua:** GitHub Actions

## 🚀 Instalação

Para configurar e executar o FoodBridge CLI em sua máquina local, siga os passos abaixo:

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/psanttana/bootcamp-cli.git
    cd foodbridge
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

## 🏃 Como Executar

Após a instalação das dependências, você pode iniciar a aplicação:

```bash
python src/app.py
```

## 🧪 Como Rodar os Testes

Para executar os testes automatizados do projeto, certifique-se de que as dependências estão instaladas e execute:

```bash
pytest
```

## 🧹 Como Rodar o Lint

Para verificar a qualidade do código e aderência a padrões de estilo com `ruff`:

```bash
ruff check .
```

Para corrigir automaticamente alguns problemas de linting:

```bash
ruff check . --fix
```

## 📄 Versão Atual

`1.0.0`

## ✍️ Autor

Desenvolvedor Manus

## 🔗 Link do Repositório Público

[https://github.com/psanttana/bootcamp-cli](https://github.com/psanttana/bootcamp-cli)

---

## 🖼️ Exemplos de Uso (Saída do Terminal)

```
=== FoodBridge CLI - Gerenciador de Doações de Alimentos ===
1. Adicionar Doação
2. Listar Doações Disponíveis
3. Coletar Doação
4. Sair

Escolha uma opção: 1
Nome do Doador: Padaria Central
Item Alimentar: Pães
Quantidade (ex: 5kg, 10 unidades): 20 unidades
Data de Validade (AAAA-MM-DD): 2026-04-15
✅ Doação registrada com sucesso!

Escolha uma opção: 2
[1] Pães - 20 unidades (Validade: 2026-04-15) | Doador: Padaria Central

Escolha uma opção: 3
ID da doação para coletar: 1
Nome da Entidade Receptora: Abrigo Esperança
✅ Doação marcada como coletada!

Escolha uma opção: 2
Nenhuma doação disponível no momento.

Escolha uma opção: 4
Saindo... Até logo!
```
