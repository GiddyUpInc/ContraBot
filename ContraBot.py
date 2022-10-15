"""
Description:
    Main script for running ContraBot - speech processing with contradiction detection.
"""

from ContraBot.arg_parser import ArgParser
from ContraBot.converter import Converter
from ContraBot.speech_processing import SpeechRecognition
from ContraBot.utils import get_dir, get_filename, get_extension

def parse_input() -> dict:
    """Parse user input and exit if no input given"""
    # Create argparser object and call method to return user input
    parser = ArgParser()
    args = parser.parse_args()

    # Check if audio is realtime or single/multiple file(s)
    if args.real_time:
        print("Processing real-time audio.")
        return []
    elif args.input != []:
        inputs = args.input

        return args
    else:
        exit("Must specify audio file(s) or realtime audio.")

def transcribe_audio(audio_files: list):
    """Transcribe audio for list of audio files"""
    pass

def main():
    # Call function to parse user input
    args = parse_input()


    if len(args) > 0:
        """Transcribe audio files specified by user"""
        transcribe_audio(args)
    else:
        """Real time audio (not yet implemented)"""
        exit()

if __name__ == "__main__":
    main()