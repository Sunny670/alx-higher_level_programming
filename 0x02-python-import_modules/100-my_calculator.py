#!/usr/bin/python3
if__name__ == "__main__":
    """Handle basic arithmetic operations."""
    form calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) - 1 != 3:
        print("usage: ./100-my_calculator.py<a><operatoor><b>")
        sys.exit(1)
        ops = {"+": add, "-": sub, "*": mul, "/": div}
        if sys.argv[2] not in list(ops.keys()):
            print("Unknown operator. Available operators: +, -, *, /")
            sys.exit(1)
            a = int(sys.argv[1])
            b = int(sys.argv[3])
        print("{}{}{} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))
