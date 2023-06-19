import random


class DiskEmulator:
    def __init__(self, disk_space):
        self.disk_space = disk_space
        self.available_space = disk_space

    def read_write(self, file_size):
        operation = random.choice(['leitura', 'escrita'])

        if operation == 'leitura':
            if self.available_space + file_size > self.disk_space:
                return f"Erro: Não há espaço suficiente no disco para ler um arquivo de tamanho {file_size}. Espaço disponível: {self.available_space}/{self.disk_space}"
            else:
                self.available_space += file_size
                return f"Leitura de arquivo de tamanho {file_size} realizada. Espaço disponível no disco: {self.available_space}/{self.disk_space}"
        else:
            if file_size <= self.available_space:
                self.available_space -= file_size
                return f"Escrita de arquivo de tamanho {file_size} realizada. Espaço disponível no disco: {self.available_space}/{self.disk_space}"
            else:
                return f"Não há espaço suficiente no disco para escrever um arquivo de tamanho {file_size}. Espaço disponível: {self.available_space}/{self.disk_space}"

    def get_available_space(self):
        return self.available_space

    def clean_disk(self):
        self.available_space = self.disk_space
        return "Disco limpo. Espaço disponível: {}/{}".format(self.available_space, self.disk_space)
