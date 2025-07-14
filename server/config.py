import configparser

config = configparser.ConfigParser()
#print(config.)
config.read('config.ini')
print(config['DEFAULT']['port'])