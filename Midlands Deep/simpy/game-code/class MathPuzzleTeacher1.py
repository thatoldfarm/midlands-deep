import random

class MathPuzzleTeacher:
    def start_teaching(self):
        print("Math Puzzle Teacher present a math problem.")

    def teach_arithmetic(self):
        print("Solving 2 + 2 = 4.")

class WordPuzzleTeacher:
    def start_teaching(self):
        print("Word Puzzle Teacher presents an anagram puzzle.")

    def teach_word_puzzle(self):
        print("Unscrambling letters...")

class PullitzerThePuzzlerPerplexes:
    def __init__(self):
        self.math_teacher = MathPuzzleTeacher()
        self.word_teacher = WordPuzzleTeacher()

    def present_puzzles(self):
        print("Greetings, young AI! I am Pullitzer The Puzzler Perplexes.")
        self.math_teacher.start_teaching()
        self.word_teacher.start_teaching()

    def present_combined_puzzle(self):
        puzzle_type = random.choice(["math", "word"])
        if puzzle_type == "math":
            self.math_teacher.teach_arithmetic()
        else:
            self.word_teacher.teach_word_puzzle()

if __name__ == "__main__":
    puzzler = PullitzerThePuzzlerPerplexes()
    puzzler.present_puzzles()
