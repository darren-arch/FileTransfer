from urllib.request import urlretrieve
import configparser, os


filename = 'version.ini'

urlretrieve("https://raw.githubusercontent.com/darren-arch/FileTransfer/refs/heads/main/server/config.ini", filename)

version = configparser.ConfigParser()
version.read(filename)
os.remove(filename)

config = configparser.ConfigParser()
config.read('config.ini')

if version['DEFAULT']['version'] != config['DEFAULT']['version']:
    filename = "server.py"

    urlretrieve("https://raw.githubusercontent.com/darren-arch/FileTransfer/main/server/server.py", filename)