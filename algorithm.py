from tools import *

def execute(index, tape, data):
	state = data["initial"]
	while(state not in data["finals"]):
		transition = read_pos(index, tape, data["transitions"][state])
		draw(tape, index, format_transition(transition, state), data["blank"])
		tape[index] = transition["write"]
		index = action(index, transition["action"])
		state = transition["to_state"]

def action(index, move):
	if(move == "LEFT"):
		index -= 1
	if(move == "RIGHT"):
		index += 1

	return index
	# else
def read_pos(index, tape, transitions_list):
	for transition in transitions_list:
		if(transition["read"] == tape[index]):
			return transition
	return None
