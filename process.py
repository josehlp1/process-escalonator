import threading
import time
import random
import uuid

class Process(threading.Thread):
    def __init__(self, priority):
        threading.Thread.__init__(self)
        self.id = str(uuid.uuid4())[:6]
        self.priority = priority
        self.start_time = None
        self.end_time = None
        self.disk_usage = None
        self.mmu_usage = None

    def run(self):
        self.start_time = time.time()
        time_to_complete = random.randint(2, 5)
        time.sleep(time_to_complete)
        self.end_time = time.time()

    def use_disk(self, disk_emulator, file_size):
        self.disk_usage = disk_emulator.read_write(file_size)

    def use_mmu(self, mmu, virtual_address):
        self.mmu_usage = mmu.translate_address(virtual_address)

    def use_cpu(self, cpu):
        self.cpu_usage = cpu.execute_instruction()

    def __lt__(self, other):
        return self.priority < other.priority
