# auto_powershell_obfuscation

## Description

An automated tool for obfuscation of a powershell script.
This tool is for experimental purposes, I am not responsible for your actions.

## Usage

```
python3 obfuscator.py <YOUR_PAYLOAD>
```

```powershell
PS C:\obfuscator> python3 .\obfuscator.py .\test_payload.txt
Payload 

$var = $True;$var2 = $False;

New Payload 

$f75fc1bb5c6b4553a485859901a9128f = (9999 -eq 9999);$34a7d89f45c847fc8527e8c646d0f69b = !![bool]$null;
```
