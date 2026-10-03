def list_available_games():
    return ["Tic Tac Toe", "Chess", "Snake", "Puzzle"]

def play_tic_tac_toe():
    print("Playing Tic Tac Toe...")

def play_chess():
    print("Playing Chess...")

def play_snake():
    print("Playing Snake...")

def play_puzzle():
    print("Playing Puzzle...")

class Land:
    def __init__(self):
        self.connected_to_hime = True

    def terminal(self):
        available_games = list_available_games()
        print(f"Available games in terminal: {available_games}")

if __name__ == "__main__":
    land = Land()
    land.terminal()
