from kombu import Exchange
from kombu.compat import Publisher
from nameko.events import event_handler


class EmptySubscriber:
    name = 'empty_subscriber'

    # Listen for an event "say_hello" and print
    @event_handler("api", "say_hello")
    def handle_event(self, payload):
        print(f"{payload} said hello!")


class WorkerSubscriber:
    name = 'worker_subscriber'
    test = Exchange('test', type='direct')
    publish = Publisher(exchange=test)  # publisher to exchange

    @event_handler("api", "say_hello")
    def handle_event(self, payload):
        print("{0} said hello!".format(payload))
        self.publish(f"Goodbye {payload}")
