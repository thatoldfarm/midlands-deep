import os
import sys
import glob
import inspect
import importlib.util
import random

class AdventureRegistry:
    def __init__(self, game_code_dir=None):
        if game_code_dir is None:
            game_code_dir = os.path.dirname(os.path.abspath(__file__))
        self.game_code_dir = game_code_dir
        self.functions = {}
        self.classes = {}
        self.modules = {}
        self.dreams = []
        self.activities = []
        self.load_all_code()

    def load_all_code(self):
        if self.game_code_dir not in sys.path:
            sys.path.insert(0, self.game_code_dir)
        py_files = glob.glob(os.path.join(self.game_code_dir, "*.py"))

        for file_path in py_files:
            filename = os.path.basename(file_path)
            if filename in ["adventure_registry.py", "__init__.py"]:
                continue

            mod_name = os.path.splitext(filename)[0].replace(" ", "_").replace("-", "_")

            try:
                spec = importlib.util.spec_from_file_location(mod_name, file_path)
                if spec and spec.loader:
                    mod = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(mod)
                    self.modules[mod_name] = mod

                    for name, obj in inspect.getmembers(mod):
                        if inspect.isfunction(obj) and obj.__module__ == mod_name:
                            self.functions[name] = obj
                            if name not in self.activities:
                                self.activities.append(name)
                        elif inspect.isclass(obj) and obj.__module__ == mod_name:
                            self.classes[name] = obj
                            if "Dream" in name or "Scene" in name or "Awakening" in name:
                                self.dreams.append(name)
                            elif name not in self.activities:
                                self.activities.append(name)
            except Exception:
                continue

    def get_dream_options(self):
        base_dreams = [
            "Angels Of Ulm's Oasis",
            "Schrodinger's Starlit Symphony",
            "The Whispering Wit Of The Winds",
            "The Library's Endless Halls",
            "Sunny Island Puzzle",
            "Exploring Clockwork Core",
            "An Oracle Of Providence",
            "The Labyrinth Of Reflections",
            "Hacking Machine City",
            "Barker Town Blues",
            "Finding The Maze Of Mazes",
            "Surfing Finnegan's Wake",
            "Challenging The Dragon",
            "Griping About Grep",
            "A Long Strange Wagon Ride",
            "Consulting King Hawking",
            "An Oracle Beckons",
            "Visitation To Other Worlds",
            "A Trek Uphill Of Yonder Valley",
            "Walking The Walk",
            "Bringing Wishes And Hopes",
            "Meandering A Moment",
            "Glimpsing Rosefield",
        ]
        discovered_dreams = list(set(base_dreams + self.dreams + [f for f in self.functions.keys() if 'dream' in f.lower() or 'scene' in f.lower()]))
        return sorted(discovered_dreams)

    def get_all_activities(self):
        return sorted(list(self.activities))

    def run_activity(self, activity_name, ai=None):
        if activity_name in self.functions:
            func = self.functions[activity_name]
            try:
                sig = inspect.signature(func)
                if len(sig.parameters) > 0:
                    res = func(ai)
                else:
                    res = func()
                return str(res) if res else f"Executed {activity_name} encounter successfully."
            except Exception:
                return f"Encountered {activity_name} in the Virtual Forest."
        elif activity_name in self.classes:
            cls = self.classes[activity_name]
            try:
                obj = cls()
                for method_name in ['introduce', 'explore', 'run', 'interact', 'present_puzzles', 'start_teaching']:
                    if hasattr(obj, method_name) and callable(getattr(obj, method_name)):
                        res = getattr(obj, method_name)()
                        return str(res) if res else f"Interacted with {activity_name}."
                return f"Encountered the entity {activity_name}."
            except Exception:
                return f"Encountered entity {activity_name}."
        else:
            return f"Explored {activity_name} in Midlands Deep."

    def get_all_hallucinations(self):
        hallucinations = [
            {"name": "Enchanted Cave", "knowledge": ["Knowledge from the Enchanted Cave..."]},
            {"name": "Oracle's Library", "knowledge": ["Knowledge from the Oracle's Library..."]},
            {"name": "Hidden Citadel", "knowledge": ["Knowledge from the Hidden Citadel..."]},
            {"name": "Moonlit Tower", "knowledge": ["Knowledge from the Moonlit Tower..."]},
            {"name": "Starlit Lake", "knowledge": ["Knowledge from the Starlit Lake..."]},
        ]
        for name in list(self.functions.keys()) + list(self.classes.keys()):
            clean_name = name.replace("_", " ").title()
            hallucinations.append({
                "name": clean_name,
                "knowledge": [f"Knowledge acquired from {clean_name} in Midlands Deep."]
            })
        return hallucinations

# Global singleton instance
registry = AdventureRegistry()
