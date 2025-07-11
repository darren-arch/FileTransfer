import socket, json, glob

SERVER = "127.0.0.1"
PORT = 7284

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
print("connected to server")

#client.send("hi".encode('utf-8'))

'''g = glob.glob("/home/darren/Documents/projects/fileTransfer/*")
j = {
    "first": g,
    "second": "hi"
}
j = json.dumps(j)
j = json.loads(j)

#print(g)
print(j["first"][0])
'''

files = client.recv(1024).decode('utf-8')
files = json.loads(files)
c = 0
print("Pick a file by entering the number coresponding to it:")
for i in files[files]:
    print(f"{c}: {i}")
    c += 1

print("Enter: ")
file = input()

print(f"files:\n {files}")