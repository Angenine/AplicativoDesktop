from abc import ABC, abstractmethod
from uuid import UUID, uuid4

class ItemColecao(ABC):

    #Legenda - STATUS
    STATUS_MAP = {
        0: "Pendente",      # Quero Ler/Assistir/Jogar
        1: "Em Progresso",  # Lendo/Assistindo/Jogando
        2: "Finalizado",
        3: "Pausado"
    }

    def __init__(self, titulo: str, ano: int, status: int = 0):
        self._id: UUID = uuid4()
        self._titulo = titulo
        self._ano = ano
        self._status = status
        self._avaliacao = 0
        self._favorito = False

    def get_id(self) -> UUID:
        return self._id

    def get_titulo(self) -> str:
        return self._titulo

    def get_ano(self) -> int:
        return self._ano

    def set_status(self, novo_status: int):
        if not isinstance(novo_status, int):
            print(f"Erro: O status deve ser um número inteiro. (Valor recebido: {novo_status})")
            return
        if novo_status in self.STATUS_MAP:
            self._status = novo_status
            print(f"Status de '{self._titulo}' atualizado para: {self.get_status()}")
        else:
            print(f"Erro: Status '{novo_status}' é inválido.")

    def get_status(self) -> str:
        return self.STATUS_MAP.get(self._status, "Desconhecido")

    def get_avaliacao(self) -> int:
        return self._avaliacao

    def set_avaliacao(self, nova_avaliacao: int):
        if not isinstance(nova_avaliacao, int):
            print(f"Erro: A avaliação deve ser um número inteiro. (Valor recebido: {nova_avaliacao})")
            return
        if 0 <= nova_avaliacao <= 5:
            self._avaliacao = nova_avaliacao
            print(f"Avaliação de '{self._titulo}' atualizada para: {self._avaliacao}/5")
        else:
            print("Erro: A avaliação deve ser entre 0 e 5.")

    def is_favorito(self) -> bool:
        return self._favorito

    def marcar_favorito(self, eh_favorito: bool):
        self._favorito = eh_favorito
        status_fav = "marcado como favorito" if eh_favorito else "desmarcado como favorito"
        print(f"Item '{self._titulo}' {status_fav}.")

    @abstractmethod
    def exibir_detalhes(self):
        pass
    
    def _base_to_dict(self) -> dict:
        """Converte os dados comuns da classe base para um dicionário."""
        return {
            "id": str(self._id),
            "titulo": self._titulo,
            "ano": self._ano,
            "status": self._status,
            "avaliacao": self._avaliacao,
            "favorito": self._favorito
        }
    
    @abstractmethod
    def to_dict(self) -> dict:
        """Método abstrato para forçar classes filhas a implementar a serialização."""
        pass

    def __str__(self) -> str:
        favorito_str = "⭐" if self._favorito else ""
        id_curto = str(self._id).split('-')[0]
        return f"[{id_curto}] '{self.get_titulo()}' ({self.get_ano()}) - Status: {self.get_status()} | {self.get_avaliacao()}/5 estrelas {favorito_str}"

class Filme(ItemColecao):
    def __init__(self, titulo: str, ano: int, diretor: str, status: int = 0):
        super().__init__(titulo, ano, status)
        self._diretor = diretor

    def get_diretor(self) -> str:
        return self._diretor
    
    def exibir_detalhes(self):
        print("\n--- Detalhes do Filme ---")
        print(self)
        print(f"   Diretor: {self._diretor}")

    def to_dict(self) -> dict:
        dados = super()._base_to_dict()
        dados["tipo"] = "Filme"
        dados["diretor"] = self._diretor
        return dados

class Livro(ItemColecao):
    def __init__(self, titulo: str, ano: int, autor: str, status: int = 0):
        super().__init__(titulo, ano, status)
        self._autor = autor

    def get_autor(self) -> str:
        return self._autor

    def exibir_detalhes(self):
        print("\n--- Detalhes do Livro ---")
        print(self)
        print(f"   Autor: {self._autor}")

    def to_dict(self) -> dict:
        dados = super()._base_to_dict()
        dados["tipo"] = "Livro"
        dados["autor"] = self._autor
        return dados

class Jogo(ItemColecao):
    def __init__(self, titulo: str, ano: int, desenvolvedora: str, plataforma: str, status: int = 0):
        super().__init__(titulo, ano, status)
        self._desenvolvedora = desenvolvedora
        self._plataforma = plataforma

    def get_desenvolvedora(self) -> str:
        return self._desenvolvedora
    
    def get_plataforma(self) -> str:
        return self._plataforma

    def exibir_detalhes(self):
        print("\n--- Detalhes do Jogo ---")
        print(self)
        print(f"   Desenvolvedora: {self._desenvolvedora}")
        print(f"   Plataforma: {self._plataforma}")

    def to_dict(self) -> dict:
        dados = super()._base_to_dict()
        dados["tipo"] = "Jogo"
        dados["desenvolvedora"] = self._desenvolvedora
        dados["plataforma"] = self._plataforma
        return dados