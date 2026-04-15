def reverse_words(sentence: str) -> str:
    words = sentence.split()
    return " ".join(reversed(words))


def count_vowels(text: str) -> int:
    vowels = {"a", "e", "i", "o", "u"}
    return sum(1 for char in text.lower() if char in vowels)


if __name__ == "__main__":
    sample = "ai generated code example"
    print(f"Original: {sample}")
    print(f"Reversed words: {reverse_words(sample)}")
    print(f"Vowel count: {count_vowels(sample)}")
