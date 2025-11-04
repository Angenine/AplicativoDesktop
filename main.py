from colecao.repository import MySQLRepository 
from colecao.service import ColecaoService
from colecao.cli import start

def run():
    repository = MySQLRepository() 
    service = ColecaoService(repository=repository)
    try:
        service.carregar_colecao()
    except Exception as e:
        print(f"Erro crítico ao carregar a coleção: {e}")
        return 
    start(service=service)
    print("Saindo. Até logo!")
    
if __name__ == "__main__":
    run()