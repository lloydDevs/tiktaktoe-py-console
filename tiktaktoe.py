players = [0, 1]

valid_combinations = [
    ["a1","b1", "c1"],
    ["a2","b2", "c2"],
    ["a3","b3", "c3"],
    ["a1","a2", "a3"],
    ["b1","b2", "b3"],
    ["c1","c2", "c3"],
    ["a1","b2","c3"],
    ["c1","b2","a3"]
]

# Initialize board state
board = {
    "a1": " ", "b1": " ", "c1": " ",
    "a2": " ", "b2": " ", "c2": " ",
    "a3": " ", "b3": " ", "c3": " ",
}

def print_board():
    print("    A   B   C")
    print("  -------------")
    print(f"1 | {board['a1']} | {board['b1']} | {board['c1']} |")
    print("  -------------")
    print(f"2 | {board['a2']} | {board['b2']} | {board['c2']} |")
    print("  -------------")
    print(f"3 | {board['a3']} | {board['b3']} | {board['c3']} |")
    print("  -------------")

def check_win(player_symbol):
    for combo in valid_combinations:
        if all(board[pos] == player_symbol for pos in combo):
            return True
    return False

def is_draw():
    return all(value != " " for value in board.values())

def play_game():
    play = True
    current_player = 0
    symbols = ["X", "O"]

    print("Welcome to Console TikTakToe!")
    print_board()

    while play:
        symbol = symbols[current_player]
        move = input(f"Player {current_player + 1} ({symbol}), enter your move (e.g. a1, b2) or type \"exit\" to quit: ").lower()
        if move == "exit":
            play = False
            return
        if move not in board:
            print("Invalid move! Try again.\n")
            continue

        if board[move] != " ":
            print("That cell is already taken! Choose another.\n")
            continue

        board[move] = symbol
        print_board()

        if check_win(symbol):
            print(f"Player {current_player + 1} ({symbol}) wins!")
            break

        if is_draw():
            print("It's a draw!")
            break

        current_player = 1 - current_player  #switch player
# This will trigger the game
play_game()
