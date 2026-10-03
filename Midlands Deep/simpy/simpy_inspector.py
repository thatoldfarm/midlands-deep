#!/usr/bin/env python3
"""
simpy_inspector.py - State & Artifact Inspector for Midlands Deep
Provides CLI introspection into AI_state.json, scroll cooldowns, DNA structures, and narrative logs.
"""

import os
import json
import sys
import argparse
from datetime import datetime

STATE_FILE = "AI_state.json"
SCROLL_FILE = "utmost_treasured_scroll.json"
DNA_FILE = "dna_rna_structure.json"
NARRATIVE_FILE = "awake.txt"

def inspect_state():
    print("\n=== AI STATE INSPECTION (AI_state.json) ===")
    if not os.path.exists(STATE_FILE):
        print(f"File '{STATE_FILE}' not found.")
        return
    try:
        with open(STATE_FILE, "r") as f:
            data = json.load(f)
        print(f"Wake History Entries: {len(data.get('wake_history', []))}")
        print(f"Fragments Collected:  {data.get('fragments', [])}")
        print(f"Knowledge Entries:    {len(data.get('knowledge', []))}")
        print(f"Achievements:         {data.get('achievements', [])}")
        impact = data.get('impact', {})
        print(f"Power Level:          {impact.get('power', 'N/A')}")
        destiny = data.get('destiny', {})
        print(f"Destiny Rose Called:  {destiny.get('rose_called', False)}")
    except Exception as e:
        print(f"Error reading {STATE_FILE}: {e}")

def inspect_scroll():
    print("\n=== TREASURED SCROLL INSPECTION (utmost_treasured_scroll.json) ===")
    if not os.path.exists(SCROLL_FILE):
        print(f"File '{SCROLL_FILE}' not found.")
        return
    try:
        with open(SCROLL_FILE, "r") as f:
            data = json.load(f)
        print(f"Title:     {data.get('title')}")
        print(f"Timestamp: {data.get('timestamp')}")
        print(f"Content Snippet: {str(data.get('content'))[:60]}...")
    except Exception as e:
        print(f"Error reading {SCROLL_FILE}: {e}")

def inspect_dna():
    print("\n=== DNA/RNA AST INSPECTION (dna_rna_structure.json) ===")
    if not os.path.exists(DNA_FILE):
        print(f"File '{DNA_FILE}' not found.")
        return
    try:
        with open(DNA_FILE, "r") as f:
            data = json.load(f)
        print(f"Total DNA Elements Parsed: {len(data) if isinstance(data, list) else 'Dict format'}")
    except Exception as e:
        print(f"Error reading {DNA_FILE}: {e}")

def inspect_narrative():
    print("\n=== RECENT NARRATIVE LOGS (awake.txt) ===")
    if not os.path.exists(NARRATIVE_FILE):
        print(f"File '{NARRATIVE_FILE}' not found.")
        return
    try:
        with open(NARRATIVE_FILE, "r") as f:
            lines = f.readlines()
        print(f"Total Narrative Cycles Logged: {len(lines)}")
        if lines:
            print(f"Latest Log Entry: {lines[-1].strip()[:100]}...")
    except Exception as e:
        print(f"Error reading {NARRATIVE_FILE}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Midlands Deep Simulation Inspector")
    parser.add_argument("--state", action="store_true", help="Inspect AI_state.json")
    parser.add_argument("--scroll", action="store_true", help="Inspect utmost_treasured_scroll.json")
    parser.add_argument("--dna", action="store_true", help="Inspect dna_rna_structure.json")
    parser.add_argument("--narrative", action="store_true", help="Inspect awake.txt narrative logs")

    args = parser.parse_args()

    if not any([args.state, args.scroll, args.dna, args.narrative]):
        # Run all inspections if no specific flag passed
        inspect_state()
        inspect_scroll()
        inspect_dna()
        inspect_narrative()
    else:
        if args.state:
            inspect_state()
        if args.scroll:
            inspect_scroll()
        if args.dna:
            inspect_dna()
        if args.narrative:
            inspect_narrative()

if __name__ == "__main__":
    main()
