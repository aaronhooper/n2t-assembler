import logging

logging.basicConfig(level=logging.DEBUG)


def load_file(filename: str) -> str:
    """Load the assembly file"""

    fh = open(filename, "r")
    text = fh.read()
    return text


def trim(assembly_text: str) -> str:
    """Remove whitespace and comments"""

    def remove_inline_comments(line):
        index = line.find("//")
        if index != -1:
            return line[:index]
        return line

    lines = assembly_text.splitlines()
    stripped_lines = map(lambda line: line.strip(), lines)
    without_blanks = filter(lambda line: line != '', stripped_lines)
    without_comments = filter(lambda line: line[:2] != '//',
        without_blanks)
    without_inline_comments = map(remove_inline_comments,
        without_comments)
    out = "\n".join(without_inline_comments)
    return out


def parse_commands(assembly_text: str) -> list:
    """Parse commands from assembly file text"""

    def parse_line(line: str) -> dict:
        """Parse a single line of trimmed text"""

        parsed_command = {}

        if line[0] == '@':
            address = int(line[1:])
            parsed_command['type'] = 'A'
            parsed_command['address'] = address
        else:
            sc_index = line.find(';')
            eq_index = line.find('=')
            parsed_command['type'] = 'C'

            if sc_index != -1:
                line_split = line.split(";")
                rest = line_split[0]
                jump_code = line_split[1]
                parsed_command['jump'] = jump_code
                line = rest
            if eq_index != -1:
                line_split = line.split("=")
                destination = line_split[0]
                computation = line_split[1]
                parsed_command['computation'] = computation
                parsed_command['destination'] = destination
            else:
                # It is a computation
                parsed_command['computation'] = line[0]

        return parsed_command

    trimmed = trim(assembly_text)
    lines = trimmed.splitlines()
    parsed = map(parse_line, lines)
    out = list(parsed)
    return out
