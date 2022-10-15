"""
Description:
    Class implements google speech recognition package
    to transcribe audio files to text files.

    Will be extended to transcribe real time audio.
"""
from os import path
import speech_recognition as sr

class SpeechRecognition:
    def __init__(self):
        """Init"""
        self.r = sr.Recognizer()
        
    def transcribe_audio_file(self, audio_file: str, text_file: str):
        """Takes audio file input, transcribes audio and writes to text file"""
        AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), audio_file)
        
        # Read the entire audio file
        r = sr.Recognizer()
        with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)
            
        # Return text as list
        text = r.recognize_google(audio)
        
        # Write text to file
        with open(text_file, 'w') as f:
            f.write(text)
            
    def transcribe_realtime(self):
        """Real time transcription of microphone audio"""
        pass
    
    