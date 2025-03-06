from caesar import ALPHABETS, detect_alphabet

def define_order(key:str) -> list:
    alphabet_lower, alphabet_upper = detect_alphabet(key)
    order_list = []
    for char in key:
        if char in alphabet_lower:
            order_list.append(alphabet_lower.index(char))
        elif char in alphabet_upper:
            order_list.append(alphabet_upper.index(char))
    return order_list


def string_to_matrix(text: str, columns: int, fill_value=''):
    """Converts text into a matrix (list of lists) with a fixed number of columns."""
    # If the text length is not divisible by the columns, pad the text to fit perfectly
    if len(text) % columns != 0:
        padding = columns - (len(text) % columns)
        text += fill_value * padding  # You can change the padding character if needed
    return [list(text[i:i + columns]) for i in range(0, len(text), columns)]



def transpose_matrix(matrix, fill_value=''):
    """Reverses rows and columns (transposes) in a list-of-lists matrix."""
    max_length = max(len(row) for row in matrix)
    padded_matrix = [row + [fill_value] * (max_length - len(row)) for row in matrix]
    return [list(row) for row in zip(*padded_matrix)]


def replacement_cipher(string:str, key:str) -> str:
    encrypted = ''
    print(string_to_matrix(string, len(key)))
    matrix = transpose_matrix(string_to_matrix(string, len(key)))
    for i in range(len(matrix)):
        print(matrix[i])
    num_key = define_order(key)
    while num_key:
        encrypted += "".join(matrix[num_key.index(min(num_key))])
        matrix.pop(num_key.index(min(num_key)))
        num_key.pop(num_key.index(min(num_key)))

    return encrypted.lower().capitalize()


def replacement_decipher(encrypted: str, key: str) -> str:
    columns = len(key)
    num_key = define_order(key)  # Get column order based on key
    # Calculate the number of rows
    rows = len(encrypted) // columns
    print(rows)
    enc2 = [[] * columns for _ in range(rows)]
    matrix = string_to_matrix(encrypted, rows)
    print(matrix)

    # Sort key order to determine correct column positions
    sorted_key = sorted([num, i] for i, num in enumerate(num_key))  # (key_value, original_index)
    print(sorted_key)
    index = 0
    rows = ([num] for i, num in enumerate(sorted_key))
    for _, row in sorted_key:
        try:
            enc2[row] = matrix[index]
            index += 1
        except IndexError:
            break

    print(enc2)
    print(transpose_matrix(enc2))
    enc2 = transpose_matrix(enc2)
    decrypted = ""
    while enc2:
        decrypted += ''.join(enc2[0])
        enc2.pop(0)
    print(decrypted)
    return decrypted.lower().capitalize()
