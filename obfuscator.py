import argparse
import re
import random

from modules.rename import rename as rename
from modules.boolean import bool_edit as bool_edit
from modules.entropy_calc import entropy as entropy_calc
from modules.quote_inter import interrupt as quote_interrupt
from modules.gcm import gcm as gcm
from modules.encode_string import encode as encode_string
from modules.commentropy import commentropy
from modules.cmd_sub import sub as cmd_sub
from modules.randomize_case import randomize_case

def get_file_content(path: str):
    f = open(path, 'r')
    content = f.read()
    f.close()
    return content


def obfuscation(payload: str):
    if '$True' in payload or '$true' in payload or '$False' in payload or '$false' in payload:
        payload = bool_edit(payload)
    payload = rename(payload)
    payload = cmd_sub(payload)
    # bug hoaxshell
    payload = random.choice([quote_interrupt(payload), gcm(payload)])
    payload = commentropy(payload)
    payload = randomize_case(payload)
    payload = encode_string(payload)

    print(payload)
    print(f'\nNew payload entropy: {entropy_calc(payload)}')


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="A command line tool that you can use to make your payload undetectable to anti-virus software. \nhttps://github.com/Claquetteuuuh/auto_powershell_obfuscation")
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
        help="Enter the mode, Default=ALL"
    )
    parser.add_argument(
        "-p"
        "--payload",
        type=str,
        help="Enter your payload string"
    )
    args = parser.parse_args()
    if args.file_name == None and args.payload == None:
        print("Any payload specified. Use -f <FILE_NAME> or -p <PAYLOAD>")
    else:
        p = ""
        if args.file_name != None:
            p = get_file_content(args.file_name)
        else:
            p = args.payload
       
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

        elif re.match("[gG][cC][mM]", args.mode):
            print(gcm(p))

        elif re.match("[sS][tT][rR]64", args.mode):
            print(encode_string(p))

        elif re.match("[cC][oO][mM][mM][eE][nN][tT]", args.mode):
            print(commentropy(p))

        elif re.match("[sS][uU][bB]", args.mode):
            print(cmd_sub(p))

        elif re.match("[rR][cC][aA][sS][eE]", args.mode):
            print(randomize_case(p))

        elif re.match("[eE][nN][tT][rR][oO][pP][yY]", args.mode):
            print(entropy_calc(p))