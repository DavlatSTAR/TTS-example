import pyttsx3
from PyPDF2 import PdfReader


# Initialize TTS engine
engine = pyttsx3.init()

# Set properties
engine.setProperty('rate', 150)  # Speed (default: 200 words per minute)
engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)


def extract_text_pypdf2(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


file_path = "example.pdf"
print(extract_text_pypdf2(file_path))

# Speak text
engine.say(extract_text_pypdf2(file_path))
engine.runAndWait()
