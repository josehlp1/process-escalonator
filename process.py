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

    def run(self):
        self.start_time = time.time()
        time_to_complete = random.randint(2,5)
        time.sleep(time_to_complete)
        self.end_time = time.time()

    def __lt__(self, other):
        return self.priority < other.priority
