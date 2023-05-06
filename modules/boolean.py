#!/bin/python3

import re
from sys import argv
from uuid import uuid4
import random

def bool_edit(p: str):

    bool_val = [
	    "[bool]1254",
	    "[bool]0x12AE",
		'[bool][convert]::ToInt32("111011", 2)',
	    "![bool]$null",
        "![bool]$False",
	    "[bool](-12354893)",
	    "[bool](12 + (3 * 6))",
	    '[bool](Get-ChildItem -Path Env: | Where-Object {$_.Name -eq "username"})',
	    "[bool]@(0x01BE)",
	    "[bool][System.Collections.ArrayList]",
	    "[bool][System.Collections.CaseInsensitiveComparer]",
	    "[bool][System.Collections.Hashtable]",
	    "[bool][bool]",
	    "[bool][char]",
	    "[bool][int]",
	    "[bool][string]",
	    "[bool][double]",
	    "[bool][short]",
	    "[bool][decimal]",
	    "[bool][byte]",
	    "[bool][timespan]",
	    "[bool][datetime]",
	    "(9999 -eq 9999)",
	    "([math]::Round([math]::PI) -eq (4583 - 4580))",
	    "[Math]::E -ne [Math]::PI",
	    "[bool](![bool]$null)",
	    "[System.Collections.CaseInsensitiveComparer] -ne [bool][datetime]'2023-01-01'",
	    "[bool]$(Get-LocalGroupMember Administrators)",
	    "!!!![bool][bool][bool][bool][bool][bool]"
	]

    payload = p
    used_var_names = []

    if "$True" in payload or "$true" in payload:
        payload = replace(bool_val, used_var_names, payload, "")
    if "$False" in payload or "$false" in payload:
        payload = replace(bool_val, used_var_names, payload, "!")

	
    return payload

def replace(bool_v: list, used_v_names: list, payload: str, char: str):
    # Identify variables definitions in script
    if char == "":
        boolean_definition = re.findall('\$[tT]rue', payload)
    else:
        boolean_definition = re.findall('\$[fF]alse', payload)
    boolean_definition.sort(key=len)
    boolean_definition.reverse()

	# Replace variable names
    for boolean in boolean_definition:
		
        while True:
			
            new_bool_name = random.choice(bool_v)
			
            if (new_bool_name in used_v_names) or (re.search(new_bool_name, payload)):
                continue
				
            else:
                used_v_names.append(new_bool_name)
                break	
						
        return payload.replace(boolean, f'{char}({new_bool_name})')
    
