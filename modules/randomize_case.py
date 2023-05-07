import random
import re

def randomize_case(payload: str):
    stop = False
    separator = [" ", ";", "'", '"', "`", "=", ","]
    new_p = ""
    stop_quote = False
    stop_quote_2 = False
    for i in range(len(payload)):
        if payload[i] == "$":
            stop = True
        elif payload[i] in separator:
                stop = False
        elif payload[i] == "'":
            if stop_quote:
                stop_quote = False
            else:
                stop_quote = True
        elif payload[i] == '"':
            if stop_quote_2:
                stop_quote_2 = False
            else:
                stop_quote_2 = True

        if re.match("[a-zA-Z]", payload[i]) and stop == False and stop_quote == True and stop_quote_2 == True:
            new_p += random.choice([payload[i].lower(), payload[i].upper()])
        else:
            new_p += payload[i]
    
    return new_p

if __name__ == "__main__":
    pass