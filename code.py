'''Contains functions for converting parsed assembly instructions into
Hack machine instructions.'''

comp_map = {
    '0':   '0101010',
    '1':   '0111111',
    '-1':  '0111010',
    'D':   '0001100',
    '!D':  '0111111',
    '-D':  '0111111',
    'D+1': '0111111',
    'D-1': '0111111',
    'A':   '0110000',
    '!A':  '0110001',
    '-A':  '0110011',
    'A+1': '0110111',
    'A-1': '0110010',
    'D+A': '0000010',
    'D-A': '0010011',
    'A-D': '0000111',
    'D&A': '0000000',
    'D|A': '0010101',
    'M':   '1110000',
    '!M':  '1110001',
    '-M':  '1110011',
    'M+1': '1110111',
    'M-1': '1110010',
    'D+M': '1000010',
    'D-M': '1010011',
    'M-D': '1000111',
    'D&M': '1000000',
    'D|M': '1010101'
}

dest_map = {
    'M':    '001',
    'D':    '010',
    'MD':   '011',
    'A':    '100',
    'AM':   '101',
    'AD':   '110',
    'AMD':  '111'
}

jump_map = {
    'JGT':  '001',
    'JEQ':  '010',
    'JGE':  '011',
    'JLT':  '100',
    'JNE':  '101',
    'JLE':  '110',
    'JMP':  '111'
}


def encode_a_instruction(parsed_command):
    '''Translate A-instruction into a Hack instruction'''

    instruction_bit = '0'
    address = parsed_command['address']
    bin_address = bin(address)[2:]
    zero_padded_address = '{0:0>15}'.format(bin_address)
    return instruction_bit + zero_padded_address


def encode_c_instruction(parsed_command):
    '''Translate C-instruction into a Hack instruction'''

    instruction_bit = '1'
    unused_bits = '11'
    null_bits = '000'
    comp_bits = comp_map[parsed_command['computation']]
    dest_bits = parsed_command['destination'] if 'destination' in dest_map else null_bits
    jump_bits = parsed_command['jump'] if 'jump' in jump_map else null_bits
    return instruction_bit + unused_bits + comp_bits + dest_bits + jump_bits


def encode_command(parsed_command):
    '''Translate assembly command into a Hack instruction'''

    hack_instruction = ''

    if parsed_command['type'] == 'A':
        hack_instruction = encode_a_instruction(parsed_command)
    elif parsed_command['type'] == 'C':
        hack_instruction = encode_c_instruction(parsed_command)

    return hack_instruction
