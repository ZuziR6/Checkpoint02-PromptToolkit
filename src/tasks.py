import json

class TaskManager:
    def __init__(self, techniques, inputs_path, examples_path):
        self.techniques = techniques
        with open(inputs_path, 'r', encoding='utf-8') as f:
            self.inputs = json.load(f)
        with open(examples_path, 'r', encoding='utf-8') as f:
            self.examples = json.load(f)

    def run_sentiment_analysis(self):
        # Tarefa 01: Classificação de Sentimento [cite: 10, 11]
        instruction = "Classifique o sentimento da mensagem do cliente como POSITIVO, NEGATIVO, NEUTRO ou MISTO." [cite: 13, 14]
        input_text = self.inputs[0]['texto'] # Pega o primeiro input do JSON
        
        return {
            "Zero-Shot": self.techniques.apply_zero_shot(instruction, input_text),
            "Few-Shot": self.techniques.apply_few_shot(instruction, input_text, [ex for ex in self.examples if ex['tarefa'] == 'classificacao']),
            "CoT": self.techniques.apply_cot(instruction, input_text),
            "Role": self.techniques.apply_role_prompting(instruction, input_text)
        }

    def run_ticket_extraction(self):
        # Tarefa 02: Extração de Entidades [cite: 15, 16]
        instruction = "Extraia o produto, o problema técnico e o nível de prioridade do texto abaixo. Responda APENAS em JSON." [cite: 17]
        input_text = self.inputs[1]['texto'] # Pega o segundo input (Monitor LG)
        
        return {
            "Zero-Shot": self.techniques.apply_zero_shot(instruction, input_text),
            "Few-Shot": self.techniques.apply_few_shot(instruction, input_text, [ex for ex in self.examples if ex['tarefa'] == 'extracao']),
            "CoT": self.techniques.apply_cot(instruction, input_text),
            "Role": self.techniques.apply_role_prompting(instruction, input_text)
        }

    def run_empathetic_response(self):
        # Tarefa 03: Geração de Resposta [cite: 18, 19]
        instruction = "Escreva uma resposta profissional e resolutiva para o cliente, focando na solução do problema." [cite: 20]
        input_text = self.inputs[2]['texto'] # Pega o terceiro input (Cancelamento)
        
        return {
            "Zero-Shot": self.techniques.apply_zero_shot(instruction, input_text),
            "Few-Shot": self.techniques.apply_few_shot(instruction, input_text, [ex for ex in self.examples if ex['tarefa'] == 'geracao']),
            "CoT": self.techniques.apply_cot(instruction, input_text),
            "Role": self.techniques.apply_role_prompting(instruction, input_text)
        }
