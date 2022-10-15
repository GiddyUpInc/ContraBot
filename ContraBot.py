"""
Description:
    Main script for running ContraBot - speech processing with contradiction detection.
"""

import os

from contrabot.arg_parser import ArgParser
from contrabot.speech_processing import SpeechRecognition
from contrabot.utils import list_wav_files

def parse_input() -> dict:
    """Parse user input and return dictionary with input and output dir"""
    # Create argparser object and call method to return dictionary with user input
    parser = ArgParser()
    args = parser.parse_args()

    # Unpack dictionary
    input: str = args["input"]
    out_dir: str = args["out_dir"]
    real_time = args["real_time"]

    # Exit if real time chosen
    if real_time:
        exit("Real time not yet implemented")

    # Create list for multiple input files
    wav_files = []
    
    # Check if input exists and is file/dir
    if os.path.isfile(input):
        wav_files.append(input)
    elif os.path.isdir(input):
        wav_files = wav_files + list_wav_files(input)
    else:
        exit("Input doesn't exist.")

    output = {
        "wav_files": wav_files,
        "out_dir": out_dir
    }

    return output


def transcribe_audio(audio_files: list, out_dir: str):
    """Transcribe audio for list of audio files"""
    pass

def analyse_text(dir: str):
    """Analyse text in each txt file in dir and create companion analysis file"""
    pass

def main():
    # Call function to parse user input
    args = parse_input()
    audio_files = args["wav_files"]
    out_dir = args["out_dir"]

    # Transcribe audio files to text files in outdir
    transcribe_audio(audio_files, out_dir)

    # Analyse text to find contradictions
    analyse_text(out_dir)


if __name__ == "__main__":
    main()