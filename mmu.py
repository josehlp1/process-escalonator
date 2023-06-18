import random

class MMU:
    def __init__(self, memory_capacity):
        self.memory_capacity = memory_capacity
        self.page_table = {}

    def translate_address(self, virtual_address):
        if virtual_address in self.page_table:
            physical_address = self.page_table[virtual_address]
            return f"Endereço virtual {virtual_address} traduzido para endereço físico {physical_address}"
        else:
            physical_address = random.randint(0, self.memory_capacity)
            self.page_table[virtual_address] = physical_address
            return f"Endereço virtual {virtual_address} criado e traduzido para endereço físico {physical_address}"

    def generate_virtual_address(self):
        virtual_address = f"0x{''.join(str(random.randint(0, 9)) for _ in range(8))}"
        return self.translate_address(virtual_address)
