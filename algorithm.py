from tools import *

def execute(index, tape, data):
	state = data["initial"]
	while(state not in data["finals"]):
		transition = read_pos(index, tape, data["transitions"][state])
		draw(tape, index, format_transition(transition, state), data["blank"])
		write_pos(tape, index, transition["write"], data["blank"])
		index = action(index, transition["action"])
		state = transition["to_state"]
	draw(tape, index, format_transition(transition, state), data["blank"])

def write_pos(tape, index, value, blank):
	if (index + 2 > len(tape)):
		tape.append(blank)
	tape[index] = value


def action(index, move):
	if(move == "LEFT"):
		index -= 1
	if(move == "RIGHT"):
		index += 1
	return index

def read_pos(index, tape, transitions_list):
	if index + 1 > len(tape):
		print("Logic Error: infinite loop")
		exit()
	for transition in transitions_list:
		if(transition["read"] == tape[index]):
			return transition
	print("Logic Error: Transition not available")
	exit()
