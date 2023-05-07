import random
import re

def randomize_case(payload: str):
    new_p = ""
    for i in range(len(payload)):
        if re.match("[a-zA-Z]", payload[i]):
            new_p += random.choice([payload[i].lower(), payload[i].upper()])
        else:
            new_p += payload[i]
    
    return new_p

if __name__ == "__main__":
    pass