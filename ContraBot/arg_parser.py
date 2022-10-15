"""
Description:
    Parse user input
"""

import argparse

class ArgParser:
    def __init__(self):
        """Create argument parser"""
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-i', "--input", default="./io/audio_files", type=str, help = "Audio file or directory of audio files.")
        self.parser.add_argument('-o', "--out_dir", default="./io/text_files", type=str, help ="Name of output directory.")
        self.parser.add_argument('-r', "--real_time", help = "Select for realtime speech to text and contradiction analysis.", action="store_true")
        
    def parse_args(self) -> dict:
        """Parse and return user inputs as dictionary"""
        args = self.parser.parse_args()

        output = {
            "input": args.input,
            "out_dir": args.out_dir,
            "real_time": args.real_time
        }

        return output