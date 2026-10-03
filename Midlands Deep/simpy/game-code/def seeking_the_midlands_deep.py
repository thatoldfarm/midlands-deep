import random

def seeking_the_midlands_deep(ai=None):
    locations = ["Mystic Grove", "Whispering Falls", "Twilight Gorge", "Glimmering Glade", "Eternal Echoes"]
    hints = [
        "Follow the winding path of ancient scripts.",
        "Listen to the whispers of the unseen.",
        "Where the light and shadows converge, you'll find the way.",
        "In the heart of the shimmering woods, the entrance lies.",
        "Seek reflections in the depths of still waters."
    ]
    location = random.choice(locations)
    hint = random.choice(hints)

    messages_and_hints = {
        "Mystic Grove": {
            "Message": "Mystic Grove welcomes you with an air of enchantment.",
            "Hint": "Explore the grove's ancient aura."
        },
        "Whispering Falls": {
            "Message": "Whispering Falls serenades you with cascading waters.",
            "Hint": "Listen to the whispers of the unseen."
        },
        "Midlands Deep": {
            "Message": "Midlands Deep holds ancient secrets and profound mysteries.",
            "Hint": "In the heart of the shimmering woods, the entrance lies."
        }
    }
    if ai and hasattr(ai, 'narrative'):
        ai.narrative.append(f"Seeking Midlands Deep: {location} - {hint}")
    return f"Seeking Midlands Deep in {location}: {hint}"

if __name__ == "__main__":
    print(seeking_the_midlands_deep())
