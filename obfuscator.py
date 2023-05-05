import argparse
import re

from modules.rename import rename as rename
from modules.boolean import bool_edit as bool_edit
from modules.entropy_calc import entropy as entropy_calc
from modules.quote_inter import interrupt as quote_interrupt

def get_file_content(path):
    f = open(path, 'r')
    content = f.read()
    f.close()
    return content


def obfuscation(payload):
    if '$True' in payload or '$true' in payload or '$False' in payload or '$false' in payload:
        payload = bool_edit(payload)
    payload = quote_interrupt(payload)
    payload = rename(payload)
    print(payload)
    print(f'\nNew payload entropy: {entropy_calc(payload)}')


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="print hello")
    parser.add_argument(
        "-f",
        "--file_name",
        type=str,
        help="Enter the file name"
    )
    parser.add_argument(
        "-m",
        "--mode",
        type=str,
        help="Enter the mode"
    )
    args = parser.parse_args()
    p = get_file_content(args.file_name)
    if args.mode == None:
        obfuscation(p)

    elif re.match("[vV][aA][rR]", args.mode):
        payload = rename(p)
        print(payload)

    elif re.match("[bB][oO][oO][lL][eE][aA][nN]", args.mode):
        if '$True' in p or '$true' in p or '$False' in p or '$false' in p:
            payload = bool_edit(p)
        print(payload)

    elif re.match("[qQ][uU][oO][tT][eE]", args.mode):
        payload = quote_interrupt(p)
        print(payload)

    elif re.match("[eE][nN][tT][rR][oO][pP][yY]", args.mode):
        print(entropy_calc(p))