def generate_fibonacci(n):
    """Return a list containing the first n Fibonacci numbers."""
    if n <= 0:
        return []
    if n == 1:
        return [0]

    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

#fibanocci

if __name__ == "__main__":
    try:
        count = int(input("How many Fibonacci number do you want? "))
        fib_numbers = generate_fibonacci(count)
        print("Fibonacci seq:", fib_numbers)
    except ValueError:
        print("Please do enter a valid integer.")
