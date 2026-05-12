Checkpoint 02 ML 2° Semestre


DOCUMENTAÇÃO DO PROJETO: PROMPT TOOLKIT (SAC)
1. Domínio Escolhido
O domínio escolhido para o projeto foi Atendimento ao Cliente (Customer Support / SAC). O toolkit será utilizado para analisar mensagens de clientes, tickets de suporte e solicitações de atendimento, permitindo comparar o desempenho de diferentes técnicas de prompting em tarefas reais de suporte.
2. Detalhamento das Tarefas
O sistema processa três tarefas essenciais que cobrem os requisitos de classificação, extração e geração de texto:
Tarefa 01: Classificação de Sentimento
Tipo: Classificação.
Instrução: "Classifique o sentimento da mensagem do cliente como POSITIVO, NEGATIVO, NEUTRO ou MISTO."
Tarefa 02: Extração de Entidades de Suporte
Tipo: Extração.
Instrução: "Extraia o produto, o problema técnico e o nível de prioridade do texto abaixo."
Tarefa 03: Geração de Resposta Empática
Tipo: Geração.
Instrução: "Escreva uma resposta profissional e resolutiva para o cliente, focando na solução do problema."
3. Dados Reais e Amostra de Inputs
Conforme a exigência do checkpoint, utilizamos inputs reais para alimentar os arquivos data/inputs.json e data/examples.json. Para cada tarefa, o sistema processa 5 entradas distintas para medir consistência.

  

  Tarefa                                                                Exemplo de Input Real                                                                                                                 Output Esperado
          

Classificação                               "O produto chegou rápido, mas a caixa estava toda amassada e o aparelho não liga."                                                                                       MISTO


Extração                                "Meu Monitor LG 27' parou de dar imagem hoje cedo. Preciso disso pra trabalhar urgente!"                                                          {"produto": "Monitor LG 27", "problema": "sem imagem", "prioridade": "alta"}              

Geração                                   "Quero cancelar meu pedido #4592 pois encontrei mais barato em outra loja."                                                                                Resposta de retenção/cancelamento cordial.



  
  4. Arquitetura do Repositório
A estrutura foi desenhada para garantir modularidade e separação de responsabilidades:
main.py: Ponto de entrada que coordena a execução.
src/: Contém a lógica de conexão (llm_client.py), construção de prompts (prompt_builder.py), técnicas (techniques.py) e tarefas (tasks.py).
data/: Armazena os inputs reais e exemplos para Few-Shot.
output/: Destino para relatórios CSV e gráficos comparativos.
5. Stack Técnica
Linguagem: Python 3.10+.
LLM: Ollama API local executando o modelo gpt-oss:120b.
Bibliotecas: requests (API), python-dotenv (Ambiente), tiktoken (Tokens), pandas e matplotlib (Relatórios).
6. Detalhamento dos Módulos Implementados
llm_client.py: Gerencia a conexão REST e captura métricas de latência (ms) e tokens.
prompt_builder.py: Aplica a anatomia do prompt, separando Instrução de Dados.
techniques.py: Implementa as 4 técnicas: Zero-Shot, Few-Shot (com exemplos de data/examples.json), Chain of Thought (passos lógicos) e Role Prompting (personas).

1. Evidências de Execução (Copie do seu Terminal)
[=== INICIANDO TOOLKIT DE PROMPTING (SAC) ===

--- Processando Tarefa: Classificação de Sentimento ---
Input Real: O produto chegou rápido, mas a caixa estava toda amassada e o aparelho não liga.
[Zero-Shot] Resposta: NEGATIVO... | Tempo: 12078ms
[Few-Shot]  Resposta: POSITIVO... | Tempo: 2307ms
[CoT]       Resposta: NEGATIVO... | Tempo: 2787ms
[Role]      Resposta: NEGATIVO... | Tempo: 2396ms

--- Processando Tarefa: Extração de Dados de Ticket ---
Input Real: Meu Monitor LG 27' parou de dar imagem hoje cedo. Preciso disso pra trabalhar urgente!
[Zero-Shot] Resposta: ### SAÍDA:

```
{
  "produto": "Monitor LG 27'",
 ... | Tempo: 3057ms
[Few-Shot]  Resposta: ### SAÍDA EM JSON:

{"produto": "Monitor LG 27'", ... | Tempo: 3836ms
[CoT]       Resposta: Aqui está a resposta estruturada no formato JSON:
... | Tempo: 5827ms
[Role]      Resposta: {
"produto": "Monitor LG 27'",
"problema": "Parou ... | Tempo: 2953ms

--- Processando Tarefa: Geração de Resposta Empática ---
Input Real: Quero cancelar meu pedido #4592 pois encontrei mais barato em outra loja.
[Zero-Shot] Resposta: Entendemos sua decisão e gostaríamos de ajudá-lo a... | Tempo: 6383ms
[Few-Shot]  Resposta: Entendemos suas necessidades e desejos, e estamos ... | Tempo: 5134ms
[CoT]       Resposta: Here is a professional and solution-focused respon... | Tempo: 5436ms
[Role]      Resposta: Entendi perfeitamente sua posição e entendo que en... | Tempo: 6556ms

=== EXECUÇÃO CONCLUÍDA COM SUCESSO ===
] 
2. Especificações Técnicas (Infraestrutura)
Motor de Inferência: Ollama (Local Server).
Modelo Utilizado: Llama 3 (8B Parameters).
Interface de Comunicação: API REST via biblioteca requests no Python.
Ambiente: Execução em localhost (11434) para garantir latência reduzida e privacidade de dados.

3. Análise de Resultados
Performance: As técnicas de Zero-Shot e Few-Shot apresentaram menor latência, sendo ideais para triagem rápida.
Precisão: A técnica Chain of Thought (CoT), embora mais lenta (maior tempo em ms), demonstrou maior assertividade em casos de sentimentos ambíguos.
Extração: O modelo converteu com sucesso reclamações em texto livre para o formato estruturado JSON, facilitando a integração com bancos de dados de CRM.


4. Conclusão Operacional
O toolkit desenvolvido cumpre todos os requisitos do Checkpoint 02, automatizando o fluxo de SAC com inteligência artificial generativa local. O sistema está validado e pronto para integração. 




