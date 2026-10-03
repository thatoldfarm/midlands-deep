import random

class MathPuzzleTeacher:
    def start_teaching(self):
        print("Teaching math puzzles...")

class WordPuzzleTeacher:
    def start_teaching(self):
        print("Teaching word puzzles...")

class PullitzerThePuzzlerPerplexes:
    def __init__(self):
        self.math_teacher = MathPuzzleTeacher()
        self.word_teacher = WordPuzzleTeacher()
        self.puzzles_solved = 0

    def present_puzzles(self):
        print("Greetings, young AI! I am Pullitzer The Puzzler Perplexes.")

if __name__ == "__main__":
    puzzler = PullitzerThePuzzlerPerplexes()
    puzzler.present_puzzles()
