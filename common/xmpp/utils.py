from pyxmpp2.jid import JID
from pyxmpp2.client import Client
from pyxmpp2.settings import XMPPSettings
from pyxmpp2.message import Message
from pyxmpp2.interfaces import EventHandler, event_handler, QUIT
from pyxmpp2.streamevents import AuthorizedEvent, DisconnectedEvent
import logging


class MyHandler(EventHandler):

    def __init__(self, target_jid, message):
        self.target_jid = target_jid
        self.message = message

    @event_handler(AuthorizedEvent)
    def handle_authorized(self, event):
        message = Message(to_jid=self.target_jid, body=self.message)
        event.stream.send(message)
        event.stream.disconnect()

    @event_handler(DisconnectedEvent)
    def handle_disconnected(self):
        return QUIT

    @event_handler()
    def handle_all(self, event):
        logging.info(u"-- {0}".format(event))


logging.basicConfig(level=logging.DEBUG)
logging.getLogger("pyxmpp.tcp.out").setLevel(logging.DEBUG)
logging.getLogger("pyxmpp.tcp.in").setLevel(logging.DEBUG)

your_jid = "u110064@gzbeim.ejiahe.com"
target_jid = "uvm17002@vm1"
message = "Message test"

handler = MyHandler(JID(target_jid), message)
settings = XMPPSettings({
                            "password": '123456',
                            "starttls": True,
                            "tls_verify_peer": False,
                        })
client = Client(JID(your_jid), [handler], settings)
client.connect()
client.run()
