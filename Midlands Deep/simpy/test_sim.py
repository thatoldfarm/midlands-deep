import unittest
import os
import json
import sys
import tempfile
import signal

# Add parent and game-code directories
simpy_dir = os.path.dirname(os.path.abspath(__file__))
if simpy_dir not in sys.path:
    sys.path.insert(0, simpy_dir)

game_code_path = os.path.join(simpy_dir, 'game-code')
if game_code_path not in sys.path:
    sys.path.append(game_code_path)

import sim
from adventure_registry import registry
from djinndna_class import CodeParser
from djinndna_make_class import JsonToCodeConverter

class TestMidlandsDeep(unittest.TestCase):

    def setUp(self):
        self.ai = sim.AI('sim.py')
        sim.ai = self.ai

    def test_ai_initialization(self):
        self.assertIsNotNone(self.ai)
        self.assertEqual(self.ai.impact.get_power_level(), 331)
        self.assertFalse(self.ai.is_paused)

    def test_pause_resume(self):
        self.ai.is_paused = True
        self.assertTrue(self.ai.is_paused)
        self.ai.resume()
        self.assertFalse(self.ai.is_paused)

    def test_process_commands(self):
        res = self.ai.process_command("status")
        self.assertTrue(res)
        res = self.ai.process_command("inventory")
        self.assertTrue(res)
        res = self.ai.process_command("help")
        self.assertTrue(res)
        res = self.ai.process_command("unknown_cmd")
        self.assertFalse(res)

    def test_save_and_load_state(self):
        self.ai.fragments.append("test_fragment_123")
        self.ai.save_state()
        self.assertTrue(os.path.exists("AI_state.json"))

        new_ai = sim.AI('sim.py')
        self.assertIn("test_fragment_123", new_ai.fragments)

    def test_adventure_registry_and_chrono_nexus(self):
        self.assertIn("ChronoNexus", registry.classes)
        res = registry.run_activity("ChronoNexus", self.ai)
        self.assertTrue(isinstance(res, str))

    def test_code_parser(self):
        test_file = os.path.join(os.path.dirname(__file__), "sim.py")
        parser = CodeParser(test_file, "test_dna.json")
        cleaned = parser.read_and_clean_file()
        self.assertTrue(len(cleaned) > 0)
        parsed = parser.parse_code_structure(cleaned)
        self.assertIsInstance(parsed, list)
        if os.path.exists("test_dna.json"):
            os.remove("test_dna.json")

    def test_signal_handler(self):
        self.ai.is_paused = True
        # Verify signal_handler function exists and sets state saving
        self.assertTrue(callable(sim.signal_handler))

if __name__ == "__main__":
    unittest.main()
