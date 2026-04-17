def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


if __name__ == "__main__":
    x = 20
    y = 4
    try:
        print(f"Division of {x} by {y} is {divide(x, y)}")
    except ValueError as error:
        print(error)
