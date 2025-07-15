from urllib.request import urlretrieve
import zipfile, os, shutil

filename = "code.zip"

urlretrieve("https://api.github.com/repos/OWNER/REPO/contents/PATH", filename)

with zipfile.ZipFile(f"./{filename}", 'r') as zip_ref:
    zip_ref.extractall(".")

os.remove(filename)
os.replace("./FileTransfer-main/server/server.py", "./server.py")
shutil.rmtree('./FileTransfer-main')