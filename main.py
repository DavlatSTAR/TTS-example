from openai import OpenAI
from pathlib import Path
import os


API_KEY = os.environ.get("OPENAI_API_KEY")


Authorization = "Bearer OPENAI_API_KEY"

from openai import OpenAI

client = OpenAI(
  organization='org-MKZR3uX5bPkZIiRJfcZMIUNg',
  project='proj_hj4SBmLxta6KggS7H1fVyr6o',
  api_key=API_KEY
)


completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="Today is a wonderful day to build something people love!",
)
response.stream_to_file(speech_file_path)

print(completion.choices[0].message);




