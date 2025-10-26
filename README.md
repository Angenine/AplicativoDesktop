# Gerenciador de Coleção Pessoal - ESTANTE VIRTUAL

Um script de console (CLI) para gerenciar uma coleção pessoal de mídias (filmes, livros e jogos), desenvolvido como um projeto acadêmico para matéria de Orientação a Objetos da Universidade de Brasília (UNB).

## Descrição do Projeto

Este projeto é um sistema de gerenciamento de coleção pessoal desenvolvido em Python. Ele permite ao usuário catalogar, avaliar e acompanhar o status de seus filmes, livros e jogos através de um menu de console simples e interativo.

O sistema foi desenhado para atender aos requisitos de um projeto de faculdade, com foco em:

  * **Programação Orientada a Objetos (POO):** Utilização de classes, herança e abstração para modelar os itens da coleção.
  * **Menu Funcional:** Um menu de interface de linha de comando (CLI) que permite acesso a todas as funcionalidades do sistema.

## Funcionalidades 

  * **Adicionar Itens:** Registre novos filmes, livros ou jogos no seu acervo.
  * **Listar Itens:** Visualize todos os itens da sua coleção ou apenas os seus favoritos.
  * **Buscar Itens:** Encontre um item específico pelo seu título exato ou pelo seu ID único.
  * **Atualizar Itens:** Modifique um item existente para:
      * Mudar o status (Pendente, Em Progresso, Finalizado, Pausado).
      * Dar uma avaliação (de 0 a 5 estrelas).
      * Marcar ou desmarcar como favorito.
  * **Remover Itens:** Exclua um item da sua coleção usando o ID ou título exato.
  * **Salvar e Carregar:** O acervo é salvo automaticamente em `colecao.json` ao sair e carregado ao iniciar.

## Arquitetura

O projeto é estruturado em uma arquitetura limpa e em camadas para promover a **Separação de Responsabilidades**. Isso torna o código mais fácil de manter, testar e expandir.

O código-fonte está organizado dentro do pacote `colecao/`:
  * **`models.py` (Camada de Domínio):**
    Contém as classes que representam os dados da aplicação (`ItemColecao`, `Filme`, `Livro`, `Jogo`).
  * **`repository.py` (Camada de Persistência):**
    Responsável por "traduzir" os objetos Python para o formato JSON e vice-versa. É a única camada que sabe como ler e escrever no arquivo `colecao.json`.
  * **`service.py` (Camada de Lógica de Negócio):**
    O "cérebro" da aplicação. Contém a classe `ColecaoService`, que gerencia a coleção em memória e coordena as ações entre a interface e o repositório (ex: "buscar item", "adicionar item").
  * **`cli.py` (Camada de Apresentação):**
    Responsável pela interface do usuário (UI). Contém todas as funções de `print` e `input` para desenhar os menus, coletar dados do usuário e chamar os métodos do `service`.

O arquivo `main.py` na raiz do projeto é o **Ponto de Entrada**, responsável por "montar" essas camadas (injetar o `repository` no `service`, e o `service` no `cli`) e iniciar a aplicação.

## Como Executar

**Pré-requisitos:**
  * **Python 3.10** ou superior.

**Instruções:**
1.  Clone este repositório (ou tenha os arquivos do projeto em uma pasta).
2.  Abra um terminal e navegue até a pasta raiz do projeto (`aplicativodesktop/`).

    ```bash
    cd /caminho/para/aplicativodesktop
    ```
3.  Execute o ponto de entrada `main.py`:

    ```bash
    python main.py
    ```

    *(Se o comando acima não funcionar no Windows, tente `py main.py` ou `python3 main.py` no macOS/Linux)*
4..  O menu interativo será iniciado no seu terminal.

## 📁 Estrutura de Pastas

```
aplicativodesktop/
│
├── colecao/                  # Pacote principal do código-fonte
│   ├── __init__.py           # Marca a pasta como um pacote Python
│   ├── models.py             # Camada de Domínio (Dados)
│   ├── repository.py         # Camada de Persistência (JSON)
│   ├── service.py            # Camada de Lógica de Negócio
│   └── cli.py                # Camada de Apresentação (UI/Menu)
│
├── main.py                   # Ponto de entrada da aplicação
├── colecao.json              # "Banco de dados" onde os dados são salvos
└── README.md                 # Este arquivo
```
-----

## Autor

  * **Angeline Izaura de Lima Melo**