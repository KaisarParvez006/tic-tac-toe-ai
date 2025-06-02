import random

board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(3):
        print(" " + board[i*3] + " | " + board[i*3+1] + " | " + board[i*3+2])
        if i < 2:
            print("---|---|---")
    print()

def is_winner(brd, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in win_conditions:
        if all(brd[pos] == player for pos in condition):
            return True
    return False

def is_draw():
    return " " not in board

def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = "X"
                break
        except:
            pass
        print("Invalid move. Try again.")

def ai_move():
    available_moves = [i for i in range(9) if board[i] == " "]
    move = random.choice(available_moves)
    board[move] = "O"

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X' and AI is 'O'.")
    print_board()

    while True:
        player_move()
        print_board()
        if is_winner(board, "X"):
            print("You win!")
            break
        if is_draw():
            print("It's a draw!")
            break

        print("AI's turn...")
        ai_move()
        print_board()
        if is_winner(board, "O"):
            print("AI wins!")
            break
        if is_draw():
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()