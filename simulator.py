from machine import TuringMachine
from machine_parser import parse
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str, help='Input file containing machine definition')
parser.add_argument('-i', '--input', type=str, help='Input tape of the machine')
args = parser.parse_args()


def main():    
    tm = parse(args.file)
    tm.set_tape(args.input)
    tm.simulate()


if __name__ == '__main__':
    main()
