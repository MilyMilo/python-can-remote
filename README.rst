CAN over network bridge for Python
==================================

Creates a CAN over TCP/IP bridge for use with python-can_.


Installation
------------

Install using pip::

    $ pip install python-can-remote


Usage
-----

Basic CLI with a single bus::

    $ python3 -m can_remote

Will create a bus at root directory, bound to channel 0

To do more advanced customization of routes import the RemoteServer:

.. code-block:: python

    from can_remote.server import RemoteServer

    routes = {
        "/": 0,
    }

    RemoteServer(host="0.0.0.0", port=DEFAULT_PORT, routes=routes, bustype="virtual").serve_forever()


Create python-can bus:

.. code-block:: python

    import can

    # Create a connection to server. Any config is passed to server.
    bus = can.Bus('ws://localhost:54701/',
                  bustype='remote',
                  bitrate=500000,
                  receive_own_messages=True)

    # Send messages
    msg = can.Message(arbitration_id=0x12345, data=[1,2,3,4,5,6,7,8])
    bus.send(msg)

    # Receive messages
    msg2 = bus.recv(1)
    print(msg2)

    # Disconnect
    bus.shutdown()


Web interface
-------------

There is also a basic web interface for inspecting the CAN traffic
using a browser.
It is available on the same address using HTTP, e.g. http://localhost:54701/.


.. _python-can: https://python-can.readthedocs.org/en/stable/
