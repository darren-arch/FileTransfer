import socket, json, glob, os, tarfile

SERVER = "127.0.0.1"
PORT = 7284
BUFFER = 1024

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

files = client.recv(BUFFER).decode('utf-8')
files = json.loads(files)
c = 0
print("Pick a file by entering the number coresponding to it:")
for i in files["files"]:
    print(f"{c}: {i}")
    c += 1

print("Enter: ")
file = int(input())

file = files['files'][file]
print(file)

client.send(str(file).encode('utf-8'))

file = file.split("/")

file = file[len(file)-1]

filename = file

file = open(filename, 'xb')

contents = client.recv(BUFFER)

while (contents):
    #print("Recieving...")
    file.write(contents)
    contents = client.recv(BUFFER)
file.close()

print("Recieved")

cfile = "cfile.tar.gz"

os.rename(filename, cfile)

file = tarfile.open(cfile, "r:gz")
file.extractall(".", filter="data")
file.close()

os.remove("cfile.tar.gz")

#print(f"files:\n {files}")