from time import sleep
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class TuringMachine:
    def __init__(self, init: str, accept: str, rules: dict, tapes: list = [['_']*10000]):
        self.init   = init
        self.accept = accept
        self.rules  = rules
        self.tapes  = tapes
    
    def set_tape(self, input: str):
        if not ':' in input:
            self.tapes = [list(input) + ['_']*(10000-len(input))]
        else:
            inputs = input.split(':')
            self.tapes = []
            for tape_input in inputs:
                self.tapes += [list(tape_input) + ['_']*(10000-len(tape_input))]
        
    def simulate(self):
        step = 0
        indexes = [0]*len(self.tapes)
        curr_state = self.init
        curr_chars = [tape[index] for index, tape in zip(indexes, self.tapes)]
        self.diagram(curr_state, indexes, step)
        while (curr_state, tuple(curr_chars)) in self.rules:
            new_state, new_chars, moves = self.rules[(curr_state, tuple(curr_chars))]
            for num, (index, tape) in enumerate(zip(indexes, self.tapes)):
                tape[index] = new_chars[num]
                indexes[num] += ["<","-",">"].index(moves[num]) - 1
            curr_state = new_state
            curr_chars = [tape[index] for index, tape in zip(indexes, self.tapes)]
            step += 1
            self.diagram(curr_state, indexes, step)
            sleep(1)
        if curr_state == self.accept:
            print(f"Accepted with state {self.accept}")
        else:
            print(f"Rejected with state {curr_state}")
    
    def diagram(self, curr_state, indexes, step):
        clear()
        print(f"State: {curr_state}\t\t\t\t\t\t\t\tStep: {step}")
        for index, tape in zip(indexes, self.tapes):
            for char in tape[index-20:] + tape[:index+21]:
                print(f"|{char}" if char != "_" else "| ", end="")
            print("|")
            print(" "*41 + "^")
