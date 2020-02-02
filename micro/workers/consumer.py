from kombu.messaging import Exchange, Queue
from nameko.messaging import consume


class Consumer:
    name = 'worker_consumer'
    test = Exchange('test', type='direct')
    tq = Queue('q1', exchange=test)

    @consume(tq)
    def handle_consume(self, body):
        print(f"Received message: {body}")
