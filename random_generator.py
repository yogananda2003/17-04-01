import random


def generate_random_number(start: int = 1, end: int = 100) -> int:
    return random.randint(start, end)


if __name__ == "__main__":
    print(f"Random number: {generate_random_number()}")
