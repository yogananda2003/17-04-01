def check_odd_even(number):
    """Return 'Even' if number is even, otherwise return 'Odd'."""
    return "Even" if number % 2 == 0 else "Odd"


if __name__ == "__main__":
    try:
        user_input = int(input("Enter a number: "))
        result = check_odd_even(user_input)
        print(f"The number is {result}.")
    except ValueError:
        print("Please enter a valid integer.")
