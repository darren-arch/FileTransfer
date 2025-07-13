import socket, json, glob, os, tarfile
import time

SERVER = "127.0.0.1"
PORT = 7284
BUFFER = 1024

#create a class for the client and server
class Client:

    #creates the client socket making it an IP socket using TCP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #creates the variable where all the files locations on the server is stored
    files = ""
    #creates the variable that will hold all the names of the files
    filenames = []
    #creates a list of all the files that are already downloaded
    downloadedFiles = []

    def __init__(self, server="10.0.0.59", port=7284, buffer=1024):
        self.server = server
        self.port = port
        self.buffer = buffer
    
    def connect(self):
        #creates the client socket making it an IP socket using TCP
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #connects to the server
        self.client.connect((self.server, self.port))
        #client recieves the file list from the server
        files = self.client.recv(self.buffer).decode('utf-8')
        #loads the json that it just recieved
        self.files = json.loads(files)
    
    def close(self):
        self.client.close()
        self.filenames = []
        self.files = ""
    
    def getFiles(self):
        for i in range(0, len(self.files["files"])):
            #separates the file path into its distinct parts
            filename = self.files["files"][i].split("/")
            #choses the last part which is the file name
            self.filenames.append(filename[len(filename)-1])
        return self.filenames

    def downloadFile(self, file):
        #clean the input
        file = int(file)
        #makes file = the file in that location in files['files']
        file = self.files['files'][file]
        #stores what files have been downloaded
        self.downloadedFiles.append(file)
        #sends that file path back to the server
        self.client.send(str(file).encode('utf-8'))

        #creates the name of the file that is being copied
        #which the file is a compressed tar file compressed with gunzip
        cfile = "cfile.tar.gz"

        #creates a new file in the current directory, x=create b=binary for binary translation
        file = open(cfile, 'xb')

        # recieves the first set of bites from the server which is the copied file
        contents = self.client.recv(self.buffer)

        #while the client continues to recieve the binary contents from the server
        while (contents):
            #print("Recieving...")
            #writes the binary to the file
            file.write(contents)
            #recieves more binary
            contents = self.client.recv(self.buffer)
        #closes thus creates the file
        file.close()

        #opens the file with tarfile and prepares it with r=read gz=gunzip read with gunzip
        file = tarfile.open(cfile, "r:gz")
        #extracts all of the contents to the current directory and filters the information as just dat
        file.extractall(".", filter="data")
        #closes the file thus creating the uncompressed file
        file.close()

        #removes the old compressed file
        os.remove("cfile.tar.gz")

#initializes the client
client = Client(server="127.0.0.1")

#infinitely runs the code
while True:
    #connects to the server
    client.connect()
    #gets the file name information
    files = client.getFiles()
    #prints it to the console
    for i in range(0,len(files)):
        print(f"{i}: {files[i]}")
    print("choose the file corresponding to the number:")
    #takes the file the user wants to download
    file = input()
    #downloads the file
    client.downloadFile(file)
    #closes the connection
    client.close()


    
'''
#creates the client socket making it an IP socket using TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client connects to the server using the server address and port
client.connect((SERVER, PORT))
#prints a message saying connected
print("connected to server")
'''
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
'''