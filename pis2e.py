import json
import sys
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket


class MarudaClub(WebSocket):
   
    def handleMessage(self):
        payload = json.loads(self.data)
        print(payload)
        client_cmd = payload['command']
        if client_cmd == 'sendmsg':
            msg = payload['msg']
            print(msg)
        elif client_cmd == 'ready':
            pass
        else:
            print("Unknown command received", client_cmd)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')


def run_server():
    server = SimpleWebSocketServer('', 9000, MarudaClub)
    server.serveforever()


if __name__ == "__main__":
    try:
        run_server()
    except KeyboardInterrupt:
        sys.exit(0)

