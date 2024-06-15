from machine_parser import parse
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str, help='Input file containing machine definition')
parser.add_argument('-i', '--input', type=str, help='Input tape of the machine (use : to separate input of multiple tapes)')
args = parser.parse_args()


def main():
    if args.file and args.input:
        tm = parse(args.file)
        tm.set_tape(args.input)
        print(tm.rules)
        tm.simulate()
    else: raise Exception("Missing arguments")

if __name__ == '__main__':
    main()
