"""
Description:
    Class to convert audio file
"""

# from pydub import AudioSegment

# class Converter:
#     def __init__(self):
#         """Initialize converter"""
#         pass
    
#     def convert(self, audio_file: str, ext: str = "wav"): 
#         """Convert audio file to required filetype"""
#         try:
#             # Get audio segment
#             sound = AudioSegment.from_file(audio_file)
            
#             # Create output filename
#             filename = audio_file.split('.')[0]
#             output = filename + ext
            
#             # Export audio file
#             sound.export(output, ext)
#         except:
#             exit(f"Could not convert audio file: {audio_file}")
        
#         return output