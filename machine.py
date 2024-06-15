from time import sleep
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class TuringMachine:
    def __init__(self, init: str, accept: str, rules: dict, tape: list = ['_']*10000):
        self.init   = init
        self.accept = accept
        self.rules  = rules
        self.tape   = list(tape) + ["_"]*(10000-len(tape))
    
    def set_tape(self, input: str):
        self.tape = list(input) + ['_']*(10000-len(input))
        
    def simulate(self):
        step = 0
        index = 0
        curr_state = self.init
        curr_char = self.tape[index]
        self.diagram(curr_state, index, step)
        while (curr_state, curr_char) in self.rules:
            new_state, new_char, move = self.rules[(curr_state, curr_char)]
            self.tape[index] = new_char
            index += ["<","-",">"].index(move) - 1
            curr_state = new_state
            curr_char = self.tape[index]
            step += 1
            self.diagram(curr_state, index, step)
            sleep(1)
        if curr_state == self.accept:
            print(f"Accepted with state {self.accept}")
        else:
            print(f"Rejected with state {curr_state}")
    
    def diagram(self, curr_state, index, step):
        clear()
        print(f"State: {curr_state}\t\t\t\t\t\t\t\tStep: {step}")
        for char in self.tape[index-20:] + self.tape[:index+21]:
            print(f"|{char}" if char != "_" else "| ", end="")
        print("|")
        print(" "*41 + "^")
