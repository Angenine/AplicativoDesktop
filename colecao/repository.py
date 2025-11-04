import mysql.connector
from uuid import UUID
from .models import ItemColecao, Filme, Livro, Jogo
from .db_config import DB_CONFIG 

class MySQLRepository:
    def __init__(self):
        pass

    def _get_connection(self):
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            return conn
        except mysql.connector.Error as err:
            print(f"Erro ao conectar ao MySQL: {err}")
            return None

    def _recriar_item_de_dict(self, dados_item: dict) -> ItemColecao | None:
        tipo = dados_item.get("tipo")
        
        id_val = dados_item.get('id')
        status_val = dados_item.get('status')
        avaliacao_val = dados_item.get('avaliacao')
        favorito_val = dados_item.get('favorito')

        item = None
        if tipo == "Filme":
            item = Filme(dados_item['titulo'], dados_item['ano'], dados_item['diretor'])
        elif tipo == "Livro":
            item = Livro(dados_item['titulo'], dados_item['ano'], dados_item['autor'])
        elif tipo == "Jogo":
            item = Jogo(dados_item['titulo'], dados_item['ano'], dados_item['desenvolvedora'], dados_item['plataforma'])

        if item:
            item._id = UUID(id_val) 
            item._status = status_val
            item._avaliacao = avaliacao_val
            item._favorito = bool(favorito_val) 
        return item

    def carregar(self) -> dict[UUID, ItemColecao]:
        colecao = {}
        conn = self._get_connection()
        if not conn:
            return colecao 

        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM itens_colecao")
                dados_carregados = cursor.fetchall()
            
            for dados_item in dados_carregados:
                item = self._recriar_item_de_dict(dados_item)
                if item:
                    colecao[item.get_id()] = item 
                    
            print(f"\nColeção carregada com sucesso do MySQL!")
        except Exception as e:
            print(f"\nErro ao carregar a coleção do MySQL: {e}")
        finally:
            if conn.is_connected():
                conn.close()
                
        return colecao

    def _obter_dados_para_db(self, item: ItemColecao) -> dict:
        dados = item.to_dict()
        dados.setdefault('diretor', None)
        dados.setdefault('autor', None)
        dados.setdefault('desenvolvedora', None)
        dados.setdefault('plataforma', None)
        return dados

    def adicionar(self, item: ItemColecao):
        """Adiciona um novo item ao banco de dados."""
        conn = self._get_connection()
        if not conn:
            return

        dados = self._obter_dados_para_db(item)

        sql = """
        INSERT INTO itens_colecao (
            id, tipo, titulo, ano, status, avaliacao, favorito,
            diretor, autor, desenvolvedora, plataforma
        ) VALUES (
            %(id)s, %(tipo)s, %(titulo)s, %(ano)s, %(status)s, %(avaliacao)s, %(favorito)s,
            %(diretor)s, %(autor)s, %(desenvolvedora)s, %(plataforma)s
        )
        """
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, dados)
            conn.commit() 
        except Exception as e:
            print(f"Erro ao adicionar item '{item.get_titulo()}' ao DB: {e}")
            conn.rollback() 
        finally:
            if conn.is_connected():
                conn.close()

    def atualizar(self, item: ItemColecao):
        conn = self._get_connection()
        if not conn:
            return

        dados = self._obter_dados_para_db(item)
        
        sql = """
        UPDATE itens_colecao SET
            tipo = %(tipo)s,
            titulo = %(titulo)s,
            ano = %(ano)s,
            status = %(status)s,
            avaliacao = %(avaliacao)s,
            favorito = %(favorito)s,
            diretor = %(diretor)s,
            autor = %(autor)s,
            desenvolvedora = %(desenvolvedora)s,
            plataforma = %(plataforma)s
        WHERE id = %(id)s
        """
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, dados)
            conn.commit()
            print(f"Item '{item.get_titulo()}' atualizado no DB.")
        except Exception as e:
            print(f"Erro ao atualizar item '{item.get_titulo()}' no DB: {e}")
            conn.rollback()
        finally:
            if conn.is_connected():
                conn.close()

    def remover(self, id_item: UUID):
        conn = self._get_connection()
        if not conn:
            return

        try:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM itens_colecao WHERE id = %(id)s", {'id': str(id_item)})
            conn.commit()
        except Exception as e:
            print(f"Erro ao remover item '{id_item}' do DB: {e}")
            conn.rollback()
        finally:
            if conn.is_connected():
                conn.close()