def generate_fibonacci(n):
    """Return a list containing the first n Fibonacci numbers."""

    # Guard for invalid or zero-length requests.
    if n <= 0:
        return []

    def build_sequence(remaining, a, b, sequence):
        """
        Recursively build Fibonacci numbers in O(n) time.
        a and b track the two latest Fibonacci values.
        """
        if remaining == 0:
            return sequence

        sequence.append(a)
        return build_sequence(remaining - 1, b, a + b, sequence)

    # Start recursion with F(0)=0 and F(1)=1.
    return build_sequence(n, 0, 1, [])


if __name__ == "__main__":
    try:
        # Take user input for how many Fibonacci numbers to generate.
        count = int(input("How many Fibonacci numbers do you want? "))
        fib_numbers = generate_fibonacci(count)
        print("Fibonacci sequence:", fib_numbers)
    except ValueError:
        print("Please enter a valid integer.")
