import queue
from process import Process

class ProcessManager:
    def __init__(self):
        self.process_queue = queue.PriorityQueue()

    def create_process(self, priority):
        process = Process(priority)
        self.process_queue.put((priority, process))
        return process.id

    def execute_process(self):
        if not self.process_queue.empty():
            _, process = self.process_queue.get()
            process.start()
            process.join()
            return process
        else:
            return None
