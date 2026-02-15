#!/usr/bin/python3
import sys
import json
from tools import *
# tape []
# head = 0
# state
# Alphabet = []


def main():
	if len(sys.argv) == 2 and sys.argv[1] in ("--help", "-h"):
		return help_message()
	if len(sys.argv) != 3:
		print("uso: python3 main.py jsonfile input")
		print("Numero de argumentos:", len(sys.argv))
		return
	for i,arg in enumerate(sys.argv):
		if len(arg) == 0:
			print(f"Argumento {i} inválido, string vacío.")
			return
	json_file = sys.argv[1]
	f_input = sys.argv[2]
	data = read_json(json_file)
	if not parse_json(data, f_input):
		return
	tape = list(f_input)
	index = 0
	print_orders = format_transitions(data["transitions"])
	#draw_json(data, print_orders)
	draw(tape, index, print_orders[('scanright', '.')], data["blank"])
	

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
	if (file["blank"] in input):
		print(f"Blank value: {file['blank']} can not be in the Input")
		return False
	for key, value in file["transitions"].items():
		for t in value:
			if t["read"] not in file["alphabet"] or t["write"] not in file["alphabet"]:
				print ("Read or Write Values not in Alphabet")
				return False
			if t["to_state"] not in file["states"]:
				print ("to_state Value not in states")
				return False
			if t["action"] not in ("RIGHT","LEFT"):
				print ("action value is nor LEFT/RIGHT")
				return False
	return True

def help_message():
	print("usage: ft_turing [-h] jsonfile input\n")
	print("positional arguments:")
	print("\tjsonfile	json description of the machine\n")
	print("\tinput		input of the machine\n")
	print("optional arguments:")
	print("\t-h, --help	show this help message and exit\n")

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


if __name__ == "__main__":
	main()
