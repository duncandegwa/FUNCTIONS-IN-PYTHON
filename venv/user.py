import json
filename = 'numbers.json'
with open(filename) as f_obj:
 firstname = json.load(f_obj)
 print("Welcome back, " + firstname + "!")