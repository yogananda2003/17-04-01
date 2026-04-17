def check_odd_even(number: int) -> str:
    """Return 'Even' if the number is even, otherwise 'Odd'."""
    return "Even" if number % 2 == 0 else "Odd"


def main() -> None:
    try:
        user_input = int(input("Enter a number: "))
        result = check_odd_even(user_input)
        print(f"The number is {result}.")
    except ValueError:
        print("Please enter valid integer.")


if __name__ == "__main__":
    main()
