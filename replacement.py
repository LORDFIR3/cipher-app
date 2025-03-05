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


def string_to_matrix(text:str, columns:int):
    """Converts text into a matrix (list of lists) with a fixed number of columns."""
    print("Initial Matrix (Before Transposition):")
    for row in [list(text[i:i + columns]) for i in range(0, len(text), columns)]:
        print(row)
    return [list(text[i:i + columns]) for i in range(0, len(text), columns)]


def transpose_matrix(matrix, fill_value=None):
    """Reverses rows and columns (transposes) in a list-of-lists matrix."""
    max_length = max(len(row) for row in matrix)
    padded_matrix = [row + [fill_value] * (max_length - len(row)) for row in matrix]
    return [list(row) for row in zip(*padded_matrix)]


def replacement_cipher(string:str, key:str) -> str:
    encrypted = ''
    matrix = transpose_matrix(string_to_matrix(string, len(key)))
    num_key = define_order(key)
    while num_key:
        print(f"num_key: {num_key}")
        print(f"matrix: {matrix}")
        print(f"min(num_key): {min(num_key) if num_key else 'EMPTY'}")

        encrypted += "".join(matrix[num_key.index(min(num_key))])
        matrix.pop(num_key.index(min(num_key)))
        num_key.pop(num_key.index(min(num_key)))
    return encrypted


def replacement_decipher(encrypted: str, key: str) -> str:
    columns = len(key)
    num_key = define_order(key)  # Get column order based on key

    # Calculate the number of rows
    rows = len(encrypted) // columns

    # Sort key order to determine correct column positions
    sorted_key = sorted((num, i) for i, num in enumerate(num_key))  # (key_value, original_index)

    # Create empty matrix
    matrix = [[''] * columns for _ in range(rows)]

    # Read encrypted text column-wise based on sorted key order
    index = 0
    for _, col in sorted_key:
        for row in range(rows):
            matrix[row][col] = encrypted[index]
            index += 1

    # Flatten back into a string
    return ''.join(char for row in matrix for char in row)


