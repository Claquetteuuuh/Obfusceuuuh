from sys import argv
from modules.rename import rename as rename
from modules.boolean import bool_edit as bool_edit
import re

def get_file_content(path):
	f = open(path, 'r')
	content = f.read()
	f.close()
	return content
	
def obfuscation(payload):
    payload = rename(payload)
    if '$True' in payload or '$true' in payload or '$False' in payload or '$false' in payload:
        payload = bool_edit(payload)
    
    print(payload)

if __name__ == "__main__":
    p = get_file_content(argv[1])
    obfuscation(p)