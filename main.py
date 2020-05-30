from parser import load_file, parse_commands
from code import encode_command

filename = "../max/MaxL.asm"
parsed = parse_commands(load_file(filename))
machine_instructions = list(map(encode_command, parsed))
print("\n".join(machine_instructions))
