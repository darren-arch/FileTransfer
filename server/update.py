from urllib.request import urlretrieve
import zipfile, os, shutil

filename = "code.zip"

urlretrieve("https://github.com/darren-arch/FileTransfer/archive/refs/heads/main.zip", filename)

with zipfile.ZipFile(f"./{filename}", 'r') as zip_ref:
    zip_ref.extractall(".")

os.remove(filename)
os.replace("./FileTransfer-main/server/server.py", "./server.py")
shutil.rmtree('./FileTransfer-main')