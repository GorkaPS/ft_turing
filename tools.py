#def read_pos():

#def write_pos():

#def move_pos(direction):
def format_transitions(data):
	transitions_map = {}
	for state_name, transitions_list in data.items():
		for t in transitions_list:
			key = (state_name, t["read"])
			#print (key)
			value = f"({state_name}, {t['read']}) -> ({t['to_state']}, {t['write']}, {t['action']})"
			transitions_map[key] = value
	return transitions_map

def draw_json(data,map):	
	print(f"\n***************** {data['name']} *******************\n")

	print(f"Alphabet: {data['alphabet']}")
	print(f"States: {data['states']}")
	print(f"Initial: {data['initial']}")
	print(f"Finals: {data['finals']}\n")

	print ("INSTRUCTIONS:")
	for i in map:
		print(map[i])
	print("\n***********************************************\n")

def draw(tape, index, trans_value, blank):
	tape_cpy = tape.copy()
	tape_cpy.insert(index, "<")
	tape_cpy.insert(index+2, ">")
	tape_str = "".join(tape_cpy)
	if len(tape_str) < 22:
		tape_str += blank * (22 - len(tape_str))
	print(f"[{tape_str}] {trans_value}")