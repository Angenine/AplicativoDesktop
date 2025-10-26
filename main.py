from colecao.repository import JsonRepository
from colecao.service import ColecaoService
from colecao.cli import start

DB_FILE = "colecao.json"

def run():
    repository = JsonRepository(file_path=DB_FILE)

    service = ColecaoService(repository=repository)

    try:
        service.carregar_colecao()
    except Exception as e:
        print(f"Erro crítico ao carregar a coleção: {e}")
        return 

    start(service=service)

    try:
        service.salvar_colecao()
    except Exception as e:
        print(f"Erro crítico ao salvar a coleção: {e}")

    print("Saindo. Até logo!")

if __name__ == "__main__":
    run()