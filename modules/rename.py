#!/bin/python3

import re
from sys import argv
from uuid import uuid4

def rename(p: str):

	payload = p
	used_var_names = []

	# Identify variables definitions in script
	variable_definitions = re.findall('\$[a-zA-Z0-9_]*[\ ]{0,}=', payload)
	variable_definitions.sort(key=len)
	variable_definitions.reverse()

	# Replace variable names
	for var in variable_definitions:
		
		var = var.strip("\n \r\t=")

		while True:
			
			new_var_name = uuid4().hex
			
			if (new_var_name in used_var_names) or (re.search(new_var_name, payload)):
				continue
				
			else:
				used_var_names.append(new_var_name)
				break	
						
		payload = payload.replace(var, f'${new_var_name}')
	return payload
