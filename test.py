import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description="A simple Python program with command-line arguments.")

# Define your command-line arguments
parser.add_argument("-f", "--file", help="Specify a file.")
parser.add_argument("-n", "--number", type=int, help="Specify a number.")
parser.add_argument("--flag", action="store_true", help="A flag without a value.",required=True)

# Parse the command-line arguments
args = parser.parse_args()

# Access the values of the arguments
if args.file:
    print(f"File specified: {args.file}")

if args.number:
    print(f"Number specified: {args.number}")

print(args.flag)
if args.flag:
    print("Flag is set.")

# If you run the script with "python script.py -f myfile.txt -n 42 --flag"
# it will display the specified arguments and flags.
