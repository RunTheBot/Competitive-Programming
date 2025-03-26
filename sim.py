#!/usr/bin/env python3

def logic(a, b):
    # Define your binary logic operation here.
    # For example, this function implements logical AND.
    a = not a
    b = not b
    return a or b 

def print_truth_table():
    print("{:<5} {:<5} {:<7}".format("A", "B", "Output"))
    print("-" * 20)
    # Iterate in order: False, True for both inputs.
    for a in [False, True]:
        for b in [False, True]:
            result = logic(a, b)
            print("{:<5} {:<5} {:<7}".format(a, b, result))

def logic3(a, b, c):
    # Invert all inputs then perform a sample logical operation.
    return not ((not a and b) and c)

def print_truth_table_3():
    print("{:<5} {:<5} {:<5} {:<7}".format("A", "B", "C", "Output"))
    print("-" * 30)
    for a in [False, True]:
        for b in [False, True]:
            for c in [False, True]:
                result = logic3(a, b, c)
                print("{:<5} {:<5} {:<5} {:<7}".format(a, b, c, result))

def logic4(a, b, c, d):
    # Invert 'a' and perform a sample logic operation on all four inputs.
    return (a ^ b) or (c ^ d)
def print_truth_table_4():
    print("{:<5} {:<5} {:<5} {:<5} {:<7}".format("A", "B", "C", "D", "Output"))
    print("-" * 40)
    for a in [False, True]:
        for b in [False, True]:
            for c in [False, True]:
                for d in [False, True]:
                    result = logic4(a, b, c, d)
                    print("{:<5} {:<5} {:<5} {:<5} {:<7}".format(a, b, c, d, result))


if __name__ == "__main__":
    print_truth_table()

    # print_truth_table_3()

    # print_truth_table_4()