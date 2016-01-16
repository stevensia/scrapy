#!/usr/bin/python
import json
with open('sammy.data','r') as FH:
	for i in FH:
		encodedjson=json.dumps(i,sort_keys=True,indent=4)
		print encodedjson
