# PromptToolkit SAC - Checkpoint 02

## 1. Descrição do Projeto
Este projeto consiste em um toolkit desenvolvido em Python para automação de tarefas de Atendimento ao Cliente (SAC) utilizando Inteligência Artificial Generativa local. O sistema aplica automaticamente quatro técnicas de prompting a mensagens reais de clientes, compara o desempenho (latência e qualidade) e gera logs estruturados para análise.

## 2. Domínio e Tarefas
O domínio escolhido foi **Atendimento ao Cliente**. O toolkit realiza três tarefas principais:
* **Classificação de Sentimento:** Identifica se a mensagem é Positiva, Negativa, Neutra ou Mista.
* **Extração de Entidades:** Converte reclamações em texto livre para o formato JSON (Produto, Problema e Prioridade).
* **Geração de Resposta:** Cria respostas empáticas e resolutivas para os clientes.

## 3. Técnicas de Prompting Implementadas
O sistema valida a eficácia das seguintes estratégias:
1.  **Zero-Shot:** Inferência direta sem exemplos.
2.  **Few-Shot:** Uso de exemplos de referência (armazenados em `data/examples.json`).
3.  **Chain of Thought (CoT):** Indução de raciocínio lógico passo a passo.
4.  **Role Prompting:** Atribuição de uma persona especializada (Analista de Suporte Sênior).

## 4. Stack Técnica
* **Linguagem:** Python 3.10+
* **Motor de IA:** Ollama (Execução Local)
* **Modelo:** Llama 3 (8B)
* **Bibliotecas:** `requests` para comunicação com API e `python-dotenv` para variáveis de ambiente.

## 5. Estrutura do Repositório
* `main.py`: Coordenador da execução do projeto.
* `src/`: Módulos de lógica (Cliente LLM, Builder de Prompts e Técnicas).
* `data/`: Arquivos JSON com inputs reais e exemplos para Few-Shot.
* `prompts/`: Configurações de System Prompts.

## 6. Resultados e Performance
Com base nos testes realizados localmente, foram observadas as seguintes métricas:

| Técnica | Latência Média | Observação |
| :--- | :--- | :--- |
| Zero-Shot | ~2500ms | Rápido, ideal para triagem simples. |
| Few-Shot | ~3000ms | Alta precisão na formatação de dados. |
| CoT | ~5500ms | Mais lento, porém evita erros em casos complexos. |
| Role | ~3200ms | Melhor tom de voz para respostas ao cliente. |

## 7. Como Executar
1. Certifique-se de ter o **Ollama** instalado e rodando.
2. Baixe o modelo: `ollama pull llama3`.
3. Instale as dependências: `pip install requests python-dotenv`.
4. Execute o projeto: `python main.py`.
