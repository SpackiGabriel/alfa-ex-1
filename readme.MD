# Instalação e uso do projeto

Este projeto foi desenvolvido utilizando Django para criar uma API para gerenciamento de tickets de suporte. Abaixo, você encontrará instruções para instalar as dependências usando Poetry e uma rápida visão geral de como usar as rotas disponíveis.

## Instalação de dependências

1. Certifique-se de ter o Python e o Poetry instalados em seu sistema. Se não tiver, você pode instalá-los seguindo as instruções em [Python](https://www.python.org/downloads/) e [Poetry](https://python-poetry.org/docs/#installation).

2. Clone este repositório para o seu ambiente local:

    ```bash
    git clone https://github.com/SpackiGabriel/alfa-ex-1
    ```

3. Navegue até o diretório do projeto:

    ```bash
    cd alfa-ex-1
    ```

4. Dentro do diretório do projeto, instale as dependências usando Poetry:

    ```bash
    poetry install
    ```

Isso instalará todas as dependências necessárias para executar o projeto.


## Uso das Rotas

**/dashboard/**

- **GET**: Retorna os tickets de suporte registrados, agrupados por cliente e módulo, para um determinado mês e ano.

    - **Parâmetros**:
        - `month` (obrigatório): O mês para o qual deseja visualizar os tickets.
        - `year` (obrigatório): O mês para o qual deseja visualizar os tickets.

    - **Exemplo de Uso**:

        ```bash
        GET /dashboard/?month=6&year=2024
        ```

- **POST**: Abre um novo ticket de suporte.

    - **Corpo da requisição (JSON)**:

        ```json
        {
            "title": "Título do Ticket",
            "client": 1,
            "module": 2
        }
        ```

    - **Exemplo de Uso**:

        ```bash
        POST /dashboard/
        ```

Sendo assim, você pode facilmente interagir com a API para visualizar e gerenciar tickets de suporte.