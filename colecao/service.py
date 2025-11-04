from uuid import UUID
from .models import ItemColecao
from .repository import MySQLRepository

class ColecaoService:
    
    def __init__(self, repository: MySQLRepository): 
        self._repository = repository
        self._colecao: dict[UUID, ItemColecao] = {}

    def carregar_colecao(self):
        self._colecao = self._repository.carregar()

    def atualizar_item(self, item: ItemColecao):
        self._repository.atualizar(item)

    def adicionar_item(self, item: ItemColecao):
        self._colecao[item.get_id()] = item
        self._repository.adicionar(item) 
        print(f"\nItem '{item.get_titulo()}' adicionado ao acervo.")

    def buscar_item_por_id_ou_titulo(self, termo_busca: str) -> ItemColecao | None:
        for item in self._colecao.values():
            if str(item.get_id()).startswith(termo_busca):
                return item
        
        for item in self._colecao.values():
            if item.get_titulo().lower() == termo_busca.lower():
                return item
            
        return None

    def remover_item(self, termo_busca: str) -> bool:      
        item_encontrado = self.buscar_item_por_id_ou_titulo(termo_busca)
        if item_encontrado:
            id_item = item_encontrado.get_id()
            item_removido = self._colecao.pop(id_item)
            self._repository.remover(id_item) 
            print(f"\nItem '{item_removido.get_titulo()}' removido.")
            return True
    
        print(f"\nItem com ID ou Título '{termo_busca}' não encontrado.")
        return False

    def buscar_por_id_str(self, id_str: str) -> ItemColecao | None:
        if not id_str:
            return None
        for item in self._colecao.values():
            if str(item.get_id()).startswith(id_str):
                return item
        return None

    def buscar_por_titulo(self, titulo: str) -> ItemColecao | None:
        if not titulo:
            return None
        for item in self._colecao.values():
            if item.get_titulo().lower() == titulo.lower():
                return item
        return None

    def listar_todos(self):
        if not self._colecao:
            print("\nO acervo está vazio.")
            return
        print("\n--- COLEÇÃO COMPLETA ---")
        for item in self._colecao.values():
            print(item)

    def listar_favoritos(self):
        favoritos = [item for item in self._colecao.values() if item.is_favorito()]
        if not favoritos:
            print("\nNenhum item favorito encontrado.")
            return
        print("\n--- ITENS FAVORITOS ---")
        for item in favoritos:
            print(item)