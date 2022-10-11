

import speech_recognition as sr
from os import path

from audio.audio import Audio

def main():
    """Main"""
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "LyingBeach.wav")

    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file
        
    text = r.recognize_google(audio)
    
    print(text)

if __name__ == "__main__":
    main()