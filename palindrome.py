def is_palindrome(text: str) -> bool:
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    sample = "Madam"
    if is_palindrome(sample):
        print(f"'{sample}' is a palindrome.")
    else:
        print(f"'{sample}' is not a palindrome.")
