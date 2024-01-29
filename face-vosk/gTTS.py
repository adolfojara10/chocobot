from gtts import gTTS
import os

mytext = 'Lo estás haciendo bien, intentémoslo de nuevo'
language = 'es'

# Specify the directory in the home folder
audio_dir = os.path.expanduser('/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/bad/')

# Ensure the directory exists, create it if necessary
os.makedirs(audio_dir, exist_ok=True)

# Specify the path for the MP3 file
audio_path = os.path.join(audio_dir, '3.mp3')

# Generate the audio file
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save(audio_path)

# Playing the generated file
#os.system(f"xdg-open {audio_path}")
