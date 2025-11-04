from .service import ColecaoService
from .models import Filme, Livro, Jogo, ItemColecao

def _aguardar_enter():
    input("\nPressione ENTER para continuar...")

def _obter_input_ano() -> int:
    while True:
        try:
            ano_str = input("Ano: ")
            ano_int = int(ano_str)
            if ano_int > 0:
                return ano_int
            else:
                print("Por favor, insira um ano válido.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para o ano.")

def _obter_input_int(prompt: str, min_val: int, max_val: int) -> int:
    while True:
        try:
            valor_str = input(prompt)
            valor_int = int(valor_str)
            if min_val <= valor_int <= max_val:
                return valor_int
            else:
                print(f"Valor fora do intervalo. Insira um número entre {min_val} e {max_val}.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def _menu_adicionar_filme(service: ColecaoService):
    print("\n-- Adicionar Novo Filme --")
    titulo = input("Título: ")
    ano = _obter_input_ano()
    diretor = input("Diretor: ")
    filme = Filme(titulo=titulo, ano=ano, diretor=diretor)
    service.adicionar_item(filme)

def _menu_adicionar_livro(service: ColecaoService):
    print("\n-- Adicionar Novo Livro --")
    titulo = input("Título: ")
    ano = _obter_input_ano()
    autor = input("Autor: ")
    livro = Livro(titulo=titulo, ano=ano, autor=autor)
    service.adicionar_item(livro)

def _menu_adicionar_jogo(service: ColecaoService):
    print("\n-- Adicionar Novo Jogo --")
    titulo = input("Título: ")
    ano = _obter_input_ano()
    desenvolvedora = input("Desenvolvedora: ")
    plataforma = input("Plataforma: ")
    jogo = Jogo(titulo=titulo, ano=ano, desenvolvedora=desenvolvedora, plataforma=plataforma)
    service.adicionar_item(jogo)

def _menu_adicionar(service: ColecaoService):
    while True:
        print("\n--- Adicionar Item ---")
        print("1: Adicionar Filme")
        print("2: Adicionar Livro")
        print("3: Adicionar Jogo")
        print("0: Voltar ao menu principal")
        opcao = input("Escolha o tipo de item: ")

        if opcao == '1':
            _menu_adicionar_filme(service)
            _aguardar_enter()
            break
        elif opcao == '2':
            _menu_adicionar_livro(service)
            _aguardar_enter()
            break
        elif opcao == '3':
            _menu_adicionar_jogo(service)
            _aguardar_enter()
            break
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

def _menu_buscar(service: ColecaoService):
    print("\n--- Buscar Item ---")
    print("1: Buscar por Título")
    print("2: Buscar por ID (pode ser os 8 primeiros caracteres)")
    opcao = input("Escolha sua opção: ")

    item = None
    if opcao == '1':
        titulo = input("Digite o título exato: ")
        item = service.buscar_por_titulo(titulo)
    elif opcao == '2':
        id_str = input("Digite o ID (ou início do ID): ")
        item = service.buscar_por_id_str(id_str)
    else:
        print("Opção inválida.")
        return

    if item:
        item.exibir_detalhes()
    else:
        print("Nenhum item encontrado.")

def _menu_remover(service: ColecaoService):
    print("\n--- Remover Item ---")
    termo_busca = input("Digite o ID (ou Título exato) do item a ser removido: ")
    service.remover_item(termo_busca)

def _menu_atualizar_status(item: ItemColecao):
    print("\n-- Atualizar Status --")
    print(f"Status atual: {item.get_status()}")
    print("Opções de Status:")
    for key, value in ItemColecao.STATUS_MAP.items():
        print(f"  {key}: {value}")
    
    novo_status = _obter_input_int("Digite o novo status: ", 0, 3)
    item.set_status(novo_status)

# ... (mantenha todo o código acima desta função) ...

def _menu_atualizar_item(service: ColecaoService):
    print("\n--- Atualizar Item ---")
    termo_busca = input("Digite o ID (ou Título exato) do item que deseja atualizar: ")
    item = service.buscar_item_por_id_ou_titulo(termo_busca)

    if not item:
        print(f"Item com ID ou Título '{termo_busca}' não encontrado.")
        return

    item.exibir_detalhes()
    houve_mudanca = False

    while True:
        print("\nO que deseja atualizar?")
        print(f"1: Mudar Status (Atual: {item.get_status()})")
        print(f"2: Dar Avaliação (Atual: {item.get_avaliacao()}/5)")
        print(f"3: Marcar/Desmarcar Favorito (Atual: {'⭐' if item.is_favorito() else 'Não'})")
        print("0: Concluir atualização")
        
        opcao_atualizar = input("Escolha sua opção: ")

        if opcao_atualizar == '1':
            _menu_atualizar_status(item)
            houve_mudanca = True
        elif opcao_atualizar == '2':
            nova_avaliacao = _obter_input_int("Digite a nova avaliação (0 a 5): ", 0, 5)
            item.set_avaliacao(nova_avaliacao)
            houve_mudanca = True
        elif opcao_atualizar == '3':
            item.marcar_favorito(not item.is_favorito())
            houve_mudanca = True
        elif opcao_atualizar == '0':
            if houve_mudanca:
                service.atualizar_item(item)
            print(f"\nAtualizações de '{item.get_titulo()}' concluídas.")
            break
        else:
            print("Opção inválida.")


def imprimir_menu_principal():
    print("\n--- Gerenciador de Coleção Pessoal ---")
    print("1: Adicionar Novo Item (Filme, Livro, Jogo)")
    print("2: Listar Todos os Itens")
    print("3: Buscar Item (por Título ou ID)")
    print("4: Atualizar Item (Status, Avaliação, Favorito)")
    print("5: Remover Item (por ID)")
    print("6: Listar Itens Favoritos")
    print("0: Sair e Salvar")

def start(service: ColecaoService):
    """Função principal que executa o loop do menu."""
    
    _aguardar_enter() 

    while True:
        imprimir_menu_principal()
        opcao = input("Escolha sua opção: ")

        if opcao == '1':
            _menu_adicionar(service)
        elif opcao == '2':
            service.listar_todos()
            _aguardar_enter()
        elif opcao == '3':
            _menu_buscar(service)
            _aguardar_enter()
        elif opcao == '4':
            _menu_atualizar_item(service)
            _aguardar_enter()
        elif opcao == '5':
            _menu_remover(service)
            _aguardar_enter()
        elif opcao == '6':
            service.listar_favoritos()
            _aguardar_enter()
        elif opcao == '0':
            break 
        else:
            print("Opção inválida. Tente novamente.")
            _aguardar_enter()