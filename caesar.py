import string

# Predefined alphabets for different languages
ALPHABETS = {
    "en": (string.ascii_lowercase, string.ascii_uppercase),
    "ua": ("абвгґдєжзиіїйклмнопрстуфхцчшщьюя", "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"),
    "el": ("αβγδεζηθικλμνξοπρστυφχψω", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"),
    "es": (string.ascii_lowercase + "áéíóúüñ", string.ascii_uppercase + "ÁÉÍÓÚÜÑ"),
    "fr": (string.ascii_lowercase + "àâçéèêëîïôûùüÿ", string.ascii_uppercase + "ÀÂÇÉÈÊËÎÏÔÛÙÜŸ"),
}

def detect_alphabet(text):
    """Detect the alphabet of the text based on the first letter."""
    for lang, (lower, upper) in ALPHABETS.items():
        if any(c in lower or c in upper for c in text):
            return lower, upper
    return string.ascii_lowercase, string.ascii_uppercase  # Default to English

def shift_character(char, shift, alphabet):
    """Shifts a character within its respective alphabet, handling wrap-around."""
    if char in alphabet:
        new_index = (alphabet.index(char) + shift) % len(alphabet)
        return alphabet[new_index]
    return char  # Return unchanged if not in the alphabet

def caesar_cipher(text: str, shift: int = 3) -> str:
    """Encrypts text using the Caesar cipher, supporting multiple languages."""
    alphabet_lower, alphabet_upper = detect_alphabet(text)

    return "".join(
        shift_character(char, shift, alphabet_lower) if char in alphabet_lower else
        shift_character(char, shift, alphabet_upper) if char in alphabet_upper else char
        for char in text
    )

def caesar_decipher(text: str, shift: int = 3) -> str:
    """Decrypts text encrypted using the Caesar cipher."""
    return caesar_cipher(text, -shift)
