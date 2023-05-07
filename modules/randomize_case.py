import random
import re

def randomize_case(payload: str):
    stop = False
    separator = [" ", ";", "'", '"', "`", "=", ","]
    new_p = ""
    for i in range(len(payload)):
        if payload[i] == "$":
            stop = True
        elif payload[i] in separator:
                stop = False

        if re.match("[a-zA-Z]", payload[i]) and stop == False:
            new_p += random.choice([payload[i].lower(), payload[i].upper()])
        else:
            new_p += payload[i]
    
    return new_p

if __name__ == "__main__":
    pass