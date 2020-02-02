from nameko.events import event_handler


class SimpleSubscriber:
    name = 'Simple_subscriber'

    # Listen for an event "say_hello" and print
    @event_handler("api", "say_hello")
    def handle_event(self, payload):
        print(f"{payload} said hello!")
