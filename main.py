def is_palindrome(text: str) -> bool:
    cleaned_text = text.replace(" ", "").lower()
    return cleaned_text == cleaned_text[::-1]

def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Element ciągu nie może być ujemny.")
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

def count_vowels(text: str) -> int:
    vowels = set("aeiouyąęó")
    return sum(1 for char in text.lower() if char in vowels)

def calculate_discount(price: float, discount: float) -> float:
    if not (0 <= discount <= 1):
        raise ValueError("Zniżka musi być z zakresu od 0 do 1")
    return price * (1 - discount)

def flatten_list(nested_list: list) -> list:
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

def word_frequencies(text: str) -> dict:
    cleaned_text = "".join(char if char.isalnum() else " " for char in text)

    words = cleaned_text.lower().split()
    word_freq = {}

    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    return word_freq

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True