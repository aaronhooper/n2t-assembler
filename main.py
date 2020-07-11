from parser import load_file, parse_commands
from code import encode_command
import sys

def main():
    filename_in = sys.argv[1]
    parsed = parse_commands(load_file(filename_in))
    machine_instructions = list(map(encode_command, parsed))
    out = '\n'.join(machine_instructions)
    filename_out = filename_in.split('.')[0] + '.hack'
    fh = open(filename_out, 'w')
    fh.write(out)
    fh.close()

if __name__ == '__main__':
    main()
