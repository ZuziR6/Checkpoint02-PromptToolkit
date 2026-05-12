from src.llm_client import LLMClient
from src.techniques import PromptTechniques
from src.tasks import TaskManager

def print_result(task_name, results):
    print(f"\n--- Processando Tarefa: {task_name} ---")
    for technique, data in results.items():
        print(f"[{technique}] Resposta: {data['resposta'][:100]}... | Tempo: {data['tempo_ms']}ms")

def main():
    print("=== INICIANDO TOOLKIT DE PROMPTING (SAC) ===")
    
    # Inicializa componentes
    client = LLMClient()
    techniques = PromptTechniques(client)
    manager = TaskManager(techniques, "data/inputs.json", "data/examples.json")

    # Executa as tarefas
    try:
        sentimento = manager.run_sentiment_analysis()
        print_result("Classificação de Sentimento", sentimento)

        extracao = manager.run_ticket_extraction()
        print_result("Extração de Dados de Ticket", extracao)

        geracao = manager.run_empathetic_response()
        print_result("Geração de Resposta Empática", geracao)

        print("\n=== EXECUÇÃO CONCLUÍDA COM SUCESSO ===")
    except Exception as e:
        print(f"\n[ERRO] Falha na execução: {e}")

if __name__ == "__main__":
    main()
