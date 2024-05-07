import queue
import threading
import time

class MessageQueue:
    def __init__(self):
        self.queue = queue.Queue()

    def send_message(self, message):
        self.queue.put(message)

    def receive_message(self):
        return self.queue.get()

def producer(queue):
    for i in range(5):
        message = f"Message {i}"
        print(f"Producing: {message}")
        queue.send_message(message)
        time.sleep(1)

def consumer(queue):
    while True:
        message = queue.receive_message()
        print(f"Consuming: {message}")
        time.sleep(2)

if __name__ == "__main__":
    mq = MessageQueue()

    producer_thread = threading.Thread(target=producer, args=(mq,))
    consumer_thread = threading.Thread(target=consumer, args=(mq,))

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()
