GRID_SIZE = 20

grid = [[" " for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
placed_words = []

def print_grid():
    for row in grid:
        print(" ".join(row))

def place_first_word(word):
    row = GRID_SIZE // 2
    col = GRID_SIZE // 2 - len(word) // 2

    for i, letter in enumerate(word):
        grid[row][col + i] = letter

    placed_words.append({
        "word": word,
        "row": row,
        "col": col,
        "direction": "horizontal"
    })

def try_place_word(word):
    for placed in placed_words:
        existing_word = placed["word"]

        for i, letter in enumerate(word):
            for j, existing_letter in enumerate(existing_word):
                if letter == existing_letter:

                    # Try vertical placement
                    start_row = placed["row"] - i
                    start_col = placed["col"] + j

                    if can_place(word, start_row, start_col):
                        place_word(word, start_row, start_col)
                        return True

    return False

def can_place(word, row, col):
    for i, letter in enumerate(word):
        r = row + i
        c = col

        if r < 0 or r >= GRID_SIZE:
            return False

        if grid[r][c] != " " and grid[r][c] != letter:
            return False

    return True

def place_word(word, row, col):
    for i, letter in enumerate(word):
        grid[row + i][col] = letter

    placed_words.append({
        "word": word,
        "row": row,
        "col": col,
        "direction": "vertical"
    })

def main():
    while True:
        hint = input("Enter hint (or 'create cross word'): ")

        if hint.lower() == "create cross word":
            print_grid()
            break

        word = input("Enter word: ").upper()

        if not placed_words:
            place_first_word(word)
        else:
            success = try_place_word(word)
            if not success:
                print("Could not place word.")

main()
