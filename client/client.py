import socket, json, glob, os, tarfile, tkinter, configparser

config = configparser.ConfigParser()
config.read('config.ini')
SERVER = config["DEFAULT"]["serverip"]
PORT = int(config["DEFAULT"]["port"])
BUFFER = int(config["DEFAULT"]["buffer"])

#create a class for the client and server
class ClientConnect:

    #creates the client socket making it an IP socket using TCP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #creates the variable where all the files locations on the server is stored
    files = ""
    #creates the variable that will hold all the names of the files
    filenames = []
    #creates a list of all the files that are already downloaded
    downloadedFiles = []

    def __init__(self, server="127.0.0.1", port=7284, buffer=2024):
        #initializes the server IP
        self.server = server
        #initializes the server
        self.port = port
        #initializes how much data is sent between the server and client
        #do not change unless it is changed on the server side as well
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

        #temporary: closes the clinet
        self.close()

#creates the client class, this runs the main prgram
class Client():

    client = ClientConnect(server=SERVER, port=PORT, buffer=BUFFER)

    def __init__(self, title="Download Selector", geometry="500x500"):
        self.root = tkinter.Tk()
        self.root.title(title)
        self.root.geometry(geometry)
        self.listbox = tkinter.Listbox(self.root, height=10, width=100)
        self.client.connect()

        files = self.client.getFiles()
        for file in files:
            self.listbox.insert(tkinter.END, file)
        self.listbox.pack(pady=10)

        self.download_button = tkinter.Button(self.root, text="Download", command=self.click)
        self.download_button.pack(pady=5)

        self.settingsButton = tkinter.Button(self.root, text="Settings", command=settingsclick)
        self.settingsButton.pack(pady=5)

        self.root.mainloop()

    def settingsclick(self):
        settingswindow = tkinter.TopLevel(self.root)
        settingswindow.title("Settings")
        settingswindow.geometry("500x500")
        frame = tkinter.Frame(settingswindow)
    
    def click(self):
        selected_indices = self.listbox.curselection()
        if not selected_indices:
            tkinter.messagebox.showwarning("No selection", "Please select an item to download.")
            return
        selected_index = selected_indices[0]
        self.client.downloadFile(selected_index)

client = Client()

""" def click():
    selected_indices = listbox.curselection()
    if not selected_indices:
        tkinter.messagebox.showwarning("No selection", "Please select an item to download.")
        return
    selected_index = selected_indices[0]
    client.downloadFile(selected_index) """



""" #initializes the client
client = ClientConnect(server=SERVER, port=PORT, buffer=BUFFER)
# Set up the GUI
root = tkinter.Tk()
root.title("Download Selector")
root.geometry("500x500")

listbox = tkinter.Listbox(root, height=10, width=100)
client.connect()

files = client.getFiles()
for file in files:
    listbox.insert(tkinter.END, file)
listbox.pack(pady=10)

download_button = tkinter.Button(root, text="Download", command=click)
download_button.pack(pady=5)

root.mainloop() """

#infinitely runs the code
#while True:
    #connects to the server
    #client.connect()
    #gets the file name information
    #files = client.getFiles()
    #prints it to the console
    #for i in range(0,len(files)):
    #    print(f"{i}: {files[i]}")
    #print("choose the file corresponding to the number:")
    #takes the file the user wants to download
    #file = input()
    #print()
    #downloads the file
    #client.downloadFile(file)
    #closes the connection
    #client.close()


    
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
