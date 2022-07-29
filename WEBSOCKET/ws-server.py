from websocket_server import WebsocketServer

# Called for every client connecting (after handshake)
import json
users = {}


def new_client(client, server):
    message_new_client = {
        "status": "debug",
        "web_id": client['id'],
        "client_id": None,
        "data": "Success connect"
    }
    print("New client connected and was given id %d" % client['id'])
    server.send_message(client, json.dumps(message_new_client))
    global users
    users.update({client["id"]: client})


# Called for every client disconnecting
def client_left(client, server):
    print("Client(%d) disconnected" % client['id'])
    server.send_message_to_all("Client(%d) disconnected" % client['id'])


# Called when a client sends a message
def message_received(client, server, message):
    if len(message) > 200:
        message = message[:200] + '..'
    # print(message)


    # print("users = " + str(users))
    # users = client
    if(message) == "1":
        print(client)
        print(client['address'])
        print(f"Start for id=", client['id'])
    # server.send_message(users, message)
    try:
        message_data = json.loads(message)
        print(message_data)
        if(message_data["status"]) == "debug":
            for i in users.keys():
                print(i)
                if i == message_data["web_id"]:
                    print("We this")
                    server.send_message(users[i], json.dumps(message_data))
    except:
        print("Error")
    # if(message) == "2":
    #     print(client)
    #     # print(server)
    #     print(f"Start for id=", client['id'])
    #     # suka = "{'id': 2, 'handler': <websocket_server.websocket_server.WebSocketHandler object at 0x000001D1FE60E5E0>, 'address': ('192.168.1.40', 1094)}"
    #     server.send_message(message["web_client"], "dsadas")
    # print(message["web_client"])
    # server.send_message(message, "dsadas")

    # print("Client(%d) said: %s" % (client['id'], message))

    # server.send_message_to_all("Client(%d) said: %s" % (client['id'], message))
    # server.send_message(message,message)


PORT = 9090
# Prod
# HOST = '89.108.83.142'

# Test
HOST = '192.168.1.40'

server = WebsocketServer(host=HOST, port=PORT)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()
