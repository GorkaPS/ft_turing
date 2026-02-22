#!/usr/bin/python3
import sys
from tools import *
from algorithm import execute

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
	tape = list(f_input + data["blank"])
	index = 0
	draw_json(data)
	execute(index, tape, data)

def help_message():
	print("usage: ft_turing [-h] jsonfile input\n")
	print("positional arguments:")
	print("\tjsonfile	json description of the machine\n")
	print("\tinput		input of the machine\n")
	print("optional arguments:")
	print("\t-h, --help	show this help message and exit\n")


if __name__ == "__main__":
	main()
