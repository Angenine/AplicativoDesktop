"""
Ponto de entrada principal para o Gerenciador de Coleção.
"""
from colecao.repository import JsonRepository
from colecao.service import ColecaoService
from colecao.cli import start

# Define o nome do arquivo que será usado como "banco de dados"
DB_FILE = "colecao.json"

def run():
    """
    Função principal que configura e executa a aplicação.
    """
    
    # 1. Cria o Repositório (que sabe falar com o JSON)
    repository = JsonRepository(file_path=DB_FILE)

    # 2. Cria o Serviço (o cérebro) e injeta o repositório nele
    service = ColecaoService(repository=repository)

    # 3. Carrega os dados do disco para a memória
    try:
        service.carregar_colecao()
    except Exception as e:
        print(f"Erro crítico ao carregar a coleção: {e}")
        return # Não continua se não puder carregar

    # 4. Inicia a interface do usuário (os menus) e entrega o serviço para ela
    start(service=service)

    # 5. (O loop do 'start' terminou) Salva tudo antes de sair
    try:
        service.salvar_colecao()
    except Exception as e:
        print(f"Erro crítico ao salvar a coleção: {e}")

    print("Saindo. Até logo!")

# Padrão Python para executar o script
if __name__ == "__main__":
    run()