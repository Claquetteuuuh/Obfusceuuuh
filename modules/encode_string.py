from base64 import b64encode

def encode(string: str):
    words = []
    exp = ""
    is_in = 0
    for i in range(len(string)):
        if (string[i] == '"' or string[i] == "'") and is_in == 0:
            is_in += 1
        elif (string[i] == '"' or string[i] == "'") and is_in == 1:
            words.append(exp)
            exp = ""
            is_in -= 1
        elif is_in == 1:
            exp += string[i]

    for y in range(len(words)):
        if words[y] != "":
            encoded_w = b64encode(words[y].encode('UTF-8')).decode("UTF-8")
            string = string.replace(f"'{words[y]}'", f"[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('{encoded_w}'))")

    return string


if __name__ == "__main__":
    encoded_w = b64encode("127.0.0.1".encode('UTF-8')).decode("UTF-8")
    print(encoded_w)