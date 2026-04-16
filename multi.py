def multiply_numbers(a: int, b: int) -> int:
    """Return the product of two integers."""
    return a * b


def main() -> None:
    try:
        first = int(input("Enter first numbe: "))
        second = int(input("Enter second numr: "))
        result = multiply_numbers(first, second)
        print(f"Multiplication result: {result}")
    except ValueError:
        print("Please enter valid integers.")


if __name__ == "__main__":
    main()
