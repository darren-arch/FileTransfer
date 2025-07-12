import socket, json, glob, os, tarfile

SERVER = "127.0.0.1"
PORT = 7284
BUFFER = 1024

#creates the client socket making it an IP socket using TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client connects to the server using the server address and port
client.connect((SERVER, PORT))
#prints a message saying connected
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

#client recieves the file list from the server
files = client.recv(BUFFER).decode('utf-8')
#loads the json that it just recieved
files = json.loads(files)

# command line, loops through each entry in files['files'] and displays them in the console with a number 
print("Pick a file by entering the number coresponding to it:")
for i in range(0, len(files["files"])):
    #separates the file path into its distinct parts
    filename = files["files"][i].split("/")
    #choses the last part which is the file name
    filename = filename[len(filename)-1]
    #prints it to the console
    print(f"{i}: {filename}")

#takes in the input from the user a number which coresponds to the file in files['files']
print("Enter: ")
file = int(input())

#makes file = the file in that location in files['files']
file = files['files'][file]
print(file)

#sends that file path back to the server
client.send(str(file).encode('utf-8'))

#separates the file path into its distinct parts
#filename = file.split("/")
#choses the last part which is the file name
#filename = filename[len(filename)-1]

#creates the name of the file that is being copied
#which the file is a compressed tar file compressed with gunzip
cfile = "cfile.tar.gz"

#creates a new file in the current directory, x=create b=binary for binary translation
file = open(cfile, 'xb')

# recieves the first set of bites from the server which is the copied file
contents = client.recv(BUFFER)

#while the client continues to recieve the binary contents from the server
while (contents):
    #print("Recieving...")
    #writes the binary to the file
    file.write(contents)
    #recieves more binary
    contents = client.recv(BUFFER)
#closes thus creates the file
file.close()

print("Recieved")

#os.rename(filename, cfile)

#opens the file with tarfile and prepares it with r=read gz=gunzip read with gunzip
file = tarfile.open(cfile, "r:gz")
#extracts all of the contents to the current directory and filters the information as just dat
file.extractall(".", filter="data")
#closes the file thus creating the uncompressed file
file.close()

#removes the old compressed file
os.remove("cfile.tar.gz")

#print(f"files:\n {files}")