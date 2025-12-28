from channels.routing import ProtocolTypeRouter, URLRouter
from mytodo.routing import websocket_urlpatterns
from django.core.asgi import get_asgi_application
import mytodo.routing

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(
        mytodo.routing.websocket_urlpatterns
    ),
})

