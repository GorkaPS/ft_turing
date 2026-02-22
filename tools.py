import json

def read_json(path):
	try:
		if (path[-5:].lower() != ".json"):
			raise ValueError("Formato de archivo invalido")
		with open(path, "r", encoding="utf-8") as f:
			return json.load(f)
	except FileNotFoundError:
		print(f"Error: no existe el archivo {path}")
	except PermissionError:
		print(f"Error: sin permisos para {path}")
	return None

def parse_json(file, input):
	required = ["name","alphabet","blank","states","initial","finals","transitions"]
	missing = [key for key in required if key not in file or not file[key]]
	if missing:
		print("Faltan claves o valores:", missing)
		return False
	if file["initial"] not in file["states"]:
		print (f"initial state {file['initial']} not in states")
		return False
	for f in file["finals"]:
		if f not in file["states"]:
			print(f"Final '{f}' not in states values")
			return False
	for f in file["transitions"]:
		if f not in file["states"]:
			print(f"Transition value {f} not in states values")
			return False
	for f in file["alphabet"]:
		if len(f) != 1:
			print ("Alphabet characters' length can't be bigger than 1")
			return False
	if (file["blank"] not in file["alphabet"]):
		print(f"Blank value: {file['blank']} is not in alphabet")
		return False
	for i in input:
		if i not in file["alphabet"]:
			print (f"Input character '{i}' not in alphabet")
			return False
	# if (file["blank"] in input):
	# 	print(f"Blank value: {file['blank']} can not be in the Input")
	# 	return False
	for key, value in file["transitions"].items():
		for t in value:
			if t["read"] not in file["alphabet"] or t["write"] not in file["alphabet"]:
				print ("Read or Write Values not in Alphabet")
				return False
			if t["to_state"] not in file["states"]:
				print ("to_state Value not in states")
				return False
			if t["action"] not in ("RIGHT","LEFT"):
				print ("action value is not LEFT/RIGHT")
				return False
	return True

def format_transition(transition, state):
	
	value = f"({state}, {transition['read']}) -> ({transition['to_state']}, {transition['write']}, {transition['action']})"
	return value

def draw_json(data):	
	print(f"\n***************** {data['name']} *******************\n")

	print(f"Alphabet: {data['alphabet']}")
	print(f"States: {data['states']}")
	print(f"Initial: {data['initial']}")
	print(f"Finals: {data['finals']}\n")

	print ("INSTRUCTIONS:")
	for state_name, transitions_list in data["transitions"].items():
		for t in transitions_list:
			print(format_transition(t, state_name))
	print("\n***********************************************\n")

def draw(tape, index, trans_value, blank):
	tape_cpy = tape.copy()
	tape_cpy.insert(index, "<")
	tape_cpy.insert(index+2, ">")
	tape_str = "".join(tape_cpy)
	if len(tape_str) < 22:
		tape_str += blank * (22 - len(tape_str))
	print(f"[{tape_str}] {trans_value}")

