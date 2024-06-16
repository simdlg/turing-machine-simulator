# Turing Machine Simulator

A Turing Machine simulator written in Python.

## How to use

Run simulator.py with the following command line arguments:
- `-f` (or `--file`) to specify the path of the file containing the machine's definition. See the "machines" folder for examples.
  - example: `-f machines/binary-palindrome.py`
- `-i` (or `--input`) to specify the tape(s) input. For multi-tape machines, use `:` to separate different tapes input.
  - example: `-i 1001#1011::` (example input for the "binary-addition" machine)
  - `1001:1011` specifies `1001` as input for the first tape, and `1011` as input for the second tape.
  - `1001:` specifies `1001` as input for the first tape, and nothing for the second tape (empty).
  - `:1011` specifies `1011` as input for the second tape, and nothing for the first tape.
  - `1001#1011::` specifies `1001#1011::` as input for the first tape, and nothing for the second and third tape.

## How to write your own machines

Save a .txt file with the following contents:
- `@init [initial-state]`
- `@accept [accept-state]`
- rules: 
  - `[initial-state],[initial-symbol],[new-state],[new-symbol],[head-movement]`
  - `[initial-state],[initial-symbol-tape1],...,[initial-symbol-tapeN],[new-state],[new-symbol-tape1],...,[new-symbol-tapeN],[head-movement-tape1],...,[head-movement-tapeN]`
  - See examples in the "machines" folder.

## Contributing

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

Keep this in mind if, for whatever reason, you decide to contribute to this repository.
