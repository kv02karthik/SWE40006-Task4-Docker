import argparse
import os


def main():
    parser = argparse.ArgumentParser(description="Add or subtract two numbers.")
    parser.add_argument("operation", choices=("add", "subtract"))
    parser.add_argument("first", type=float)
    parser.add_argument("second", type=float)
    args = parser.parse_args()

    if args.operation == "add":
        result = args.first + args.second
        symbol = "+"
    else:
        result = args.first - args.second
        symbol = "-"

    calculation = f"{args.first:g} {symbol} {args.second:g} = {result:g}"
    output_file = os.getenv("OUTPUT_FILE", "/data/history.txt")

    print("Calculator container started")
    print(f"Result: {calculation}")
    with open(output_file, "a", encoding="utf-8") as history:
        history.write(calculation + "\n")
    print(f"Saved result to {output_file}")
    print("Calculator container completed successfully")


if __name__ == "__main__":
    main()
