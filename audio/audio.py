
import speech_recognition as sr
from os import path

class Audio:
    def __init__(self):
        """Init"""
        self.r = sr.Recognizer()
        
    def transcribe_audio_file(self, audio_file: str, text_file: str):
        """Takes audio file input and returns"""
        pass
    
    def transcribe_realtime(self):
        """Real time transcription of microphone audio"""
        pass
    
    