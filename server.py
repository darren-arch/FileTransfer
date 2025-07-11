import socket, json, glob

HOST = "127.0.0.1"
PORT = 7284
FILE_PATH = "/home/darren/Pictures/*"

#server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server.bind((HOST, PORT))

#server.listen(5)

#communication_socket, address = server.accept()
#print(f"connected to: {address[0]}")

#hi = communication_socket.recv(1024).decode('utf-8')
#print(hi)

try:
    files = {
        "files": glob.glob(FILE_PATH),
    }
    print(files["files"])
    files = json.dumps(files)
    #print("files parsed")
    #print(files)
except Exception as e:
    print(e)
'''
try: 
    #print("sending files")
    communication_socket.send(files.encode('utf-8'))
    print("files sent")
except Exception as e:
    print(e)

try:
    file = communication_socket.recv(1024).decode('utf-8')
except Exception as e:
    print(e)
'''

#ommunication_socket.close()
#server.shutdown()

