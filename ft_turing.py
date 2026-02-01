#!/usr/bin/python3
import sys
import json

tape []
head = 0
state
Alphabet = []


def main():
	if len(sys.argv) != 3:
		print("uso: python3 main.py jsonfile input")
		print("Numero de argumentos:%d", len(sys.argv))
		return
	json_file = sys.argv[1]
	data = read_json(json_file)
	if (!parse_json(data))
		return
	

def parse_json(file):
	required = ["name","alphabet","blank","states","initial","finals","transitions"]
	missing = [key for key in required if key not in file or not file[key]]
	if missing:
		print("Faltan claves o valores:", missing)
		return False
	if (key for key in file.finals not in file.states)
		print("Finals value not in states values")
		return False
	if (key for key in file.transitions not in file.states)
		print("Transitions values not in states values")
		return False
	
	return True

def read_json(path):
    try:
		if (path[-5:].lower() != ".json")
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
