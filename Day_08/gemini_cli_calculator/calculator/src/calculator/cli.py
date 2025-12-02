import argparse
from .evaluate import evaluate

def main():
    """
    Main function for the command-line interface of the calculator.
    Parses arguments, evaluates the expression, and prints the result.
    """
    parser = argparse.ArgumentParser(description="Evaluate a mathematical expression.")
    parser.add_argument("expression", type=str, help="The mathematical expression to evaluate.")
    args = parser.parse_args()
    
    result = evaluate(args.expression)
    print(result)

if __name__ == "__main__":
    main()