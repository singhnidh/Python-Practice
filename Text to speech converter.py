# Importing the library
from gtts import gTTS
import os

# Providing the text
input_text = "Hey! This is arijit singh voice assistatS. please type of sound track i play for you"

# Setting the language
language = "en"

# Passing to gtts engine
voice = gTTS(text=input_text, lang=language, slow=False)

# Creating and saving the audio file
voice.save("demo.mp3")

# Playing the file
os.system("start demo.mp3")
