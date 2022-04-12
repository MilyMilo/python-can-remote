import logging

import can

from .server import RemoteServer
from . import DEFAULT_PORT

logging.basicConfig(format='%(asctime)-15s %(message)s', level=logging.DEBUG)
can.set_logging_level("DEBUG")

routes = {
    "/": 0,
    "/ac": 1,
    "/radio": 2,
    "/steering": 3
}

RemoteServer(host="0.0.0.0", port=DEFAULT_PORT, routes=routes, bustype="virtual").serve_forever()