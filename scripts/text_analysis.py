import argparse
import os

from audio.audio import Audio

def define_and_parse_args():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-t', "--text_file", type=str, default = "", help =  "Pass text file to be analysed.")
    
    parsed_args = parser.parse_args()
    
    return parsed_args

def main():
    """Get user inputs"""
    args = define_and_parse_args()
    
    text_file = args.text_file
    
    if os.path.exists(text_file) != True:
        exit("Text file does not exist.")
        
    """Text Analysis"""

if __name__ == "__main__":
    main()