import argparse


def add_numbers(a, b):
    return a + b


def subtract_numbers(a, b):
    return a - b


def multiply_numbers(a, b):
    return a * b


def print_result(action, a, b):
    match action:
        case 'add':
            print(f'{a} + {b} = {add_numbers(a, b)}')
        case 'subtract':
            print(f'{a} - {b} = {subtract_numbers(a, b)}')
        case 'multiply':
            print(f'{a} * {b} = {multiply_numbers(a, b)}')
        case _:
            print(f'Unknown action "{action}"')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Simple calculator', description='A CLI to add, subtract or multiply two numbers.')
    parser.add_argument('action', type=str, help='One of: add, subtract, multiply')
    parser.add_argument('a', type=float, help='First number')
    parser.add_argument('b', type=float, help='Second number')
    args = parser.parse_args()

    print_result(args.action, args.a, args.b)