from machine import TuringMachine;


def parse(file_name: str) -> TuringMachine:
    initial: str = ""
    accept: str = ""
    rules: dict = {}
    lines: list = []
    tapes_num: int = 0
    with open(file_name, "r", encoding="utf-8") as f:
        lines = f.readlines()
    tapes_num = 0
    for line_num in range(len(lines)):
        if lines[line_num].strip() == "": continue
        if lines[line_num].startswith("@init "):
            initial = lines[line_num].split(" ")[1].strip()
        elif lines[line_num].startswith("@accept "):
            accept = lines[line_num].split(" ")[1].strip()
        elif not lines[line_num].startswith("#"):
            if tapes_num == 0: tapes_num = (len(lines[line_num].split(","))-2)//3
            if not (len(lines[line_num].split(","))-2)//3 == tapes_num:
                raise Exception(f"Line {line_num+1}: wrong number of arguments in rule")
            rule = [x.strip() for x in lines[line_num].split(",")]
            init_state = rule[0]
            start_symbols = rule[1:tapes_num+1]
            end_state = rule[tapes_num+1]
            new_symbols = rule[2+tapes_num:2+tapes_num*2]
            moves = rule[2+tapes_num*2:2+tapes_num*3]
            rules[(init_state, tuple(start_symbols))] = (end_state, tuple(new_symbols), tuple(moves))
    if initial == "" or accept == "": raise Exception("Missing @init and @accept lines")
    turing_machine = TuringMachine(initial, accept, rules)
    return turing_machine
