"""
Description:
    Parse user input
"""

import argparse

class ArgParser:
    def __init__(self):
        """Create argument parser"""
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("input", nargs="+", help = "Audio file or directory of audio files")
        self.parser.add_argument('-r', "--real_time", help = "Set to true for real time speech to text and contradiction analysis.")

    def parse_args(self):
        """Parse and return user inputs"""
        return self.parser.parse_args()