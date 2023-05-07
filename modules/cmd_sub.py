import random

def sub(payload: str):
    path_new_cmd = random.choice(["$($p = (split-path `\"$(pwd)\\\\0x00\`\");if ($p.trim() -eq ''){echo 'c:\'}else{echo $p})", "$(gl).path", "$(get-location)", "$(cmd.exe /c chdir)"])
    payload = payload.lower().replace("(pwd).path", path_new_cmd)

    return payload


if __name__ == "__main__":
    pass