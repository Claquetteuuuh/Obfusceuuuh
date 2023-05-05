# auto_powershell_obfuscation - Beta

## Description

An automated tool for obfuscation of a powershell script.
This tool is for experimental purposes, I am not responsible for your actions.

## Usage

```
python3 obfuscator.py -f <YOUR_PAYLOAD> -m <MODE>
```

```powershell
PS C:\obfuscator> python3 .\obfuscator.py -f .\test_payload.txt
Payload 

$var = $True;$var2 = $False;

New Payload 

$f75fc1bb5c6b4553a485859901a9128f = (9999 -eq 9999);$34a7d89f45c847fc8527e8c646d0f69b = !![bool]$null;
```

## Mode

### Var

**var** mode only changes the names of your variables according to the entropy rules.

```powershell
```

### Boolean

**boolean** mode replaces simple $True or $False with equivalent boolean expressions.

```powershell
```

### Quote - Beta

**quote** mode will sprinkle your code with quotation marks where they don't disturb the flow (/!\ beware /!\ this mode is not completely finished, check that it works properly before using it)

```powershell
```

### Entropy

**entropy** mode allows you to calculate the entropy of your payload.

```powershell
```
