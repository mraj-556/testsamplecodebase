import sys

def main():
    try:
        # Your application logic here
        print("Application started")
        # Example: risky operation
        result = 10 / 0
    except Exception as e:
        print(f"Critical error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()