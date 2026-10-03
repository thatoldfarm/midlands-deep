import random

class WeatherConditions:
    def generate_weather_conditions(self):
        return random.choice(["Sunny", "Stormy", "Misty", "Clear Skies"])

def generate_scenario():
    scenarios = [
        "An ancient sea creature surfaces, curious about the ship.",
        "A mysterious message in a bottle floats nearby.",
        "A sudden dense fog engulfs the ship, obscuring vision.",
    ]
    return random.choice(scenarios)

def the_voyage():
    weather = WeatherConditions().generate_weather_conditions()
    scenario = generate_scenario()
    print(f"Voyage status - Weather: {weather}, Scenario: {scenario}")

if __name__ == "__main__":
    the_voyage()
