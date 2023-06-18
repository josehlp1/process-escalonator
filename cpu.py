import random

class CPU:
    def __init__(self, register_count):
        self.register_count = register_count
        self.available_registers = list(range(register_count))

    def execute_instruction(self):
        register = self.allocate_register()

        if register is not None:
            return f"Instrução executada no registrador R{register}"
        else:
            return "Erro: Nenhum registrador disponível para executar a instrução"

    def allocate_register(self):
        if self.available_registers:
            return self.available_registers.pop(0)
        else:
            return None
