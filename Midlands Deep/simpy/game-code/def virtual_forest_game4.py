import random

def explore_virtual_forest(ai=None):
    locations = ["Enchanted Cave", "Oracle's Library", "Hidden Citadel"]
    return random.choice(locations)

def virtual_forest_game(location="Virtual Forest", previous_adventures=[]):
    return f"Exploring {location}..."

if __name__ == "__main__":
    print(virtual_forest_game())
