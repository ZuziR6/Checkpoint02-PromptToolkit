class PromptTechniques:
    def __init__(self, llm_client):
        self.llm = llm_client

    def apply_zero_shot(self, task_instruction, input_data):
        # Técnica 1: Zero-Shot (Direto ao ponto)
        prompt = f"{task_instruction}\n\nTexto: {input_data}"
        return self.llm.chat(prompt)

    def apply_few_shot(self, task_instruction, input_data, examples):
        # Técnica 2: Few-Shot (Com exemplos do data/examples.json)
        example_str = "\n".join([f"Exemplo: {ex['exemplo_input']}\nSaída: {ex['exemplo_output']}" for ex in examples])
        prompt = f"{task_instruction}\n\n{example_str}\n\nTexto real: {input_data}\nSaída:"
        return self.llm.chat(prompt)

    def apply_cot(self, task_instruction, input_data):
        # Técnica 3: Chain of Thought (Passo a passo lógico)
        prompt = f"{task_instruction}\n\nPense passo a passo sobre o problema antes de fornecer a resposta final.\n\nTexto: {input_data}"
        return self.llm.chat(prompt)

    def apply_role_prompting(self, task_instruction, input_data):
        # Técnica 4: Role Prompting (Persona de especialista)
        system_prompt = "Você é um Analista de Suporte ao Cliente Sênior com 10 anos de experiência em resolução de conflitos e análise técnica."
        prompt = f"{task_instruction}\n\nTexto: {input_data}"
        return self.llm.chat(prompt, system_prompt=system_prompt)
