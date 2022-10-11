
import argparse
import os

from audio.audio import Audio

def define_and_parse_args():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-f', "--file", type=str, default = "", help = "Pass audio file to be trascribed to text file.")
    parser.add_argument('-r', "--real_time", type=bool, default = False, help = "Set to true for real time speech to text and contradiction analysis.")
    
    parsed_args = parser.parse_args()
    
    return parsed_args

def main():
    """Get user inputs"""
    args = define_and_parse_args()
    
    filename: str = args.filename
    real_time: bool = args.real_time
    
    """Check user inputs"""
    if real_time is True:
        pass
    elif os.path.exists(filename) == True:
        name, ext = filename.split('.')
        
        if ext == ".wav":
            audio = Audio()
            audio.transcribe_audio_file()
            
        elif ext == ".txt":
            
        
    else:
        print("No input provided. Exiting...")
        
    """Text Analysis"""

if __name__ == "__main__":
    main()