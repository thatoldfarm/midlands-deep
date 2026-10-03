import random

class CuriositySquared:
    def __init__(self):
        self.completed_challenges = set()
        self.power_level = 0

    def introduce(self):
        return "Greetings! I am Curiosity Squared."

    def add_completed_challenge(self, challenge_name):
        if challenge_name not in self.completed_challenges:
            self.completed_challenges.add(challenge_name)
            self.power_level += 1

    def is_challenge_completed(self, challenge_name):
        return challenge_name in self.completed_challenges

    def cryptography_challenge(self):
        return "Solve the cipher: 01001000 01001001"

    def math_puzzle(self):
        return "What is the square root of 1764?"

if __name__ == "__main__":
    cs = CuriositySquared()
    print(cs.introduce())
    print(cs.math_puzzle())
