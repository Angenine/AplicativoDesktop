import json
import os
from uuid import UUID
from .models import ItemColecao, Filme, Livro, Jogo

class JsonRepository:
    def __init__(self, file_path: str):
        self._file_path = file_path

    def _recriar_item_de_dict(self, dados_item: dict) -> ItemColecao | None:
        tipo = dados_item.pop("tipo", None)

        id_val = dados_item.pop('id')
        status_val = dados_item.pop('status')
        avaliacao_val = dados_item.pop('avaliacao')
        favorito_val = dados_item.pop('favorito')

        item = None
        if tipo == "Filme":
            item = Filme(**dados_item) 
        elif tipo == "Livro":
            item = Livro(**dados_item) 
        elif tipo == "Jogo":
            item = Jogo(**dados_item) 

        if item:

            item._id = UUID(id_val)
            item._status = status_val
            item._avaliacao = avaliacao_val
            item._favorito = favorito_val
        return item

    def carregar(self) -> dict[UUID, ItemColecao]:
        colecao = {}
        if not os.path.exists(self._file_path):
            print("\nArquivo de coleção não encontrado. Começando com um acervo vazio.")
            return colecao

        try:
            with open(self._file_path, 'r', encoding='utf-8') as f:
                dados_carregados = json.load(f)
            
            for dados_item in dados_carregados:
                item = self._recriar_item_de_dict(dados_item)
                if item:
                    colecao[item.get_id()] = item 
                    
            print(f"\nColeção carregada com sucesso de '{self._file_path}'!")
        except Exception as e:
            print(f"\nErro ao carregar a coleção: {e}")
            
        return colecao

    def salvar(self, colecao: dict[UUID, ItemColecao]):
        dados_para_salvar = [item.to_dict() for item in colecao.values()]
        
        try:
            with open(self._file_path, 'w', encoding='utf-8') as f:
                json.dump(dados_para_salvar, f, indent=4, ensure_ascii=False)
            print(f"\nColeção salva com sucesso em '{self._file_path}'!")
        except IOError as e:
            print(f"\nErro ao salvar a coleção: {e}")