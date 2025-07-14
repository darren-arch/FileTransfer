import socket, json, glob, tarfile, os, time

HOST = "127.0.0.1"
PORT = 7284
FILE_PATH = "/home/darren/Pictures/*"
BUFFER = 1024

'''
file = tarfile.open("Screenshots1", "x:gz")
file.add("../../../Pictures/Screenshots", arcname="Screenshots")
file.close()


file = tarfile.open("./Screenshots1", "r:gz")
file.extractall(path=".", filter="data")


os.remove("/home/darren/Documents/projects/fileTransfer/Screenshots1")
'''



#creates the server socket, using IP and TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Binds the server to the Host IP and the Port
server.bind((HOST, PORT))

#Server listens for incoming connections
server.listen(5)

while True:

    #server accepts incomming connection
    communication_socket, address = server.accept()
    print(f"connected to: {address[0]}")

    try:
        #server reads the files in the given file path
        files = {
            "files": glob.glob(FILE_PATH),
        }

        #print(files["files"])
        # server turns the files object into json to be transmitted
        files = json.dumps(files)
        #print("files parsed")
        #print(files)
    except Exception as e:
        print(e)

    try: 
        #print("sending files")
        #server sends the list of files to the client
        communication_socket.send(files.encode('utf-8'))
        print("file info sent")
    except Exception as e:
        print(e)

    try:
        #server recieves which file the client wants to copy
        print("waiting for response from client")
        file = communication_socket.recv(BUFFER).decode('utf-8')
        #print(f"file: {file}")
    except Exception as e:
        print(f"Error: {e}")

    try:
        #defines the name of the compressed file
        cfile = "cfile.tar.gz"
        #gets the name of the file spcifically so that it calls the file the correct name
        #splits it at the /
        filename = file.split('/')
        #then gets the last directory path which is the file
        filename = str(filename[len(filename)-1])
        print(f"file: {file}")
        print(f"filename: {filename}")
        #saves the file path
        filepath = file
        #turns the file into a tar file with gz compression
        file = tarfile.open(cfile, 'x:gz')
        #adds the chosen file
        file.add(filepath, arcname=filename)
        #closes the file and compresses it
        file.close()
        #opens the file to read in binary
        file = open(cfile, "rb")
        #reads the first part of the file
        contents = file.read(BUFFER)
    except Exception as e:
        print(f"Error: {e}")

    try:
        #while buffer is not null, sends the contents of the file
        while(contents):
            #print("Sending...")
            #sends the data
            communication_socket.send(contents)
            #reads more binary from the file
            contents = file.read(BUFFER)
    except Exception as e:
        print(f"Error: {e}")

    try:
        #deletes the cfile
        os.remove(cfile)
    except Exception as e:
        print(f"Error: {e}")

    print("sent")

    communication_socket.close()


#server.shutdown()
