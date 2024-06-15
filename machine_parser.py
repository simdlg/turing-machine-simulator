from machine import TuringMachine;


def parse(file_name: str) -> TuringMachine:
    initial: str = None
    accept: str = None
    rules: dict = {}
    lines: list = []
    with open(file_name, "r") as f:
        lines = f.readlines()
    for line in lines:
        if line.strip() == "": continue
        if line.startswith("@init "):
            initial = line.split(" ")[1].strip()
        elif line.startswith("@accept "):
            accept = line.split(" ")[1].strip()
        elif not line.startswith("#"):
            print(line.split(","))
            init_state, start_symbol, end_state, new_symbol, move = map(lambda x: x.strip(), line.split(","))
            rules[(init_state, start_symbol)] = (end_state, new_symbol, move)
    turing_machine = TuringMachine(initial, accept, rules)
    return turing_machine
