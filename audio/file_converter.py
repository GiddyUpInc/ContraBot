"""
Description:
    Class to convert audio file
"""

from pydub import AudioSegment

class Converter:
    def __init__(self):
        """Initialize converter"""
        pass
    
    def convert(self, audio_file: str, extension: str = "wav"): 
        """Convert audio file to required filetype"""
        # Get audio segment
        sound = AudioSegment.from_file(audio_file)
        
        # Create output filename
        filename = audio_file.split('.')[0]
        output = filename + extension
        
        sound.export(output, extension)
        
        return output