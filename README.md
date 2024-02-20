# Simple Calculator CLI App

This is a simple command-line interface (CLI) application that allows you to perform basic arithmetic operations: _addition_, _subtraction_, _multiplication_, and _division_.

## Usage

To use the calculator, follow these steps:

1. Open your command line interface (terminal).
2. Navigate to the directory where the script `app.py` is located.
3. Run the script with the following command:

```bash
python app.py <action> <a> <b>
```

Replace `<action>` with one of the following: `add`, `subtract`, `multiply`, or `divide`.
Replace `<a>` and `<b>` with the numbers you want to perform the operation on.

## Examples

- To add two numbers:

```bash
python calculator.py add 5 3
```

- To subtract two numbers:

```bash
python calculator.py subtract 10 4
```

- To multiply two numbers:

```bash
python calculator.py multiply 7 2
```

- To divide two numbers:

```bash
python calculator.py divide 15 3
```

## Notes

- Make sure to provide valid numbers as input. Non-numeric inputs will result in an error.
- `python app.py -h`, `python app.py --help` to show help message
