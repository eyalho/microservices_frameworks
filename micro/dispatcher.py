import json

from nameko.events import EventDispatcher
from nameko.web.handlers import http


class API:
    name = 'api'
    dispatch = EventDispatcher()  # Event dispatcher method via dependency injection

    # Just return the json html
    @http('GET', '/hello')
    def get_method(self, *args):
        return json.dumps({'hello': 'world'})

    # Here, dispatcher will publish the name to anyone who subscribes to “say_hello" through rabbitmq
    @http('POST', '/hello')
    def do_post(self, request):
        name = request.get_data(as_text=True)
        self.dispatch("say_hello", name)
        return json.dumps({'hello': name})
