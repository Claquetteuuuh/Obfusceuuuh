import argparse
import re
import random

from modules.rename import rename as rename
from modules.boolean import bool_edit as bool_edit
from modules.entropy_calc import entropy as entropy_calc
from modules.quote_inter import interrupt as quote_interrupt
from modules.gcm import gcm as gcm
from modules.encode_string import encode_str as encode_string, encode as base64encode
from modules.commentropy import commentropy
from modules.cmd_sub import sub as cmd_sub
from modules.randomize_case import randomize_case

def get_file_content(path: str):
    f = open(path, 'r')
    content = f.read()
    f.close()
    return content

def put_in_file(path: str, payload: str):
    f = open(path, 'w')
    f.write(payload)
    f.close()


def obfuscation(payload: str):
    if '$True' in payload or '$true' in payload or '$False' in payload or '$false' in payload:
        payload = bool_edit(payload)
    payload = rename(payload)
    payload = cmd_sub(payload)
    # bug hoaxshell
    payload = quote_interrupt(payload)
    # payload = random.choice([quote_interrupt(payload), gcm(payload)])
    payload = commentropy(payload)
    payload = randomize_case(payload)
    payload = encode_string(payload)
    payload = f"{base64encode(payload)}"

    print(payload)
    print(f'\nNew payload entropy: {entropy_calc(payload)}')
    return payload


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
        "-p",
        "--payload",
        type=str,
        help="Enter your payload string."
    )
    parser.add_argument(
        "-o",
        "--out_file",
        type=str,
        help="Enter the file to write your new payload."
    )
    args = parser.parse_args()
    if args.file_name == None and args.payload == None:
        print("Any payload specified. Use -f <FILE_NAME> or -p <PAYLOAD>")
    else:
        p = ""
        payload = ""
        if args.file_name != None:
            p = get_file_content(args.file_name)
        else:
            p = args.payload
       
        if args.mode == None:
            payload = obfuscation(p)
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
            payload = gcm(p)
            print(payload)

        elif re.match("[sS][tT][rR]64", args.mode):
            payload = encode_string(p)
            print(payload)

        elif re.match("[cC][oO][mM][mM][eE][nN][tT]", args.mode):
            payload = commentropy(p)
            print(payload)

        elif re.match("[sS][uU][bB]", args.mode):
            payload = cmd_sub(p)
            print(payload)

        elif re.match("[rR][cC][aA][sS][eE]", args.mode):
            payload = randomize_case(p)
            print(payload)
        
        elif re.match("[eE][nN][cC][oO][dD][eE]", args.mode):
            payload = base64encode(p)
            print(payload)

        elif re.match("[eE][nN][tT][rR][oO][pP][yY]", args.mode):
            payload = entropy_calc(p)
            print(payload)

        if args.out_file != None:
            put_in_file(args.out_file, payload)
            print(f"\nYour payload was written in {args.out_file}")