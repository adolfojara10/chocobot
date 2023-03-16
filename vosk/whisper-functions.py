import numpy as np
import tempfile
import time
import wave
import pyaudio
import json
import torch
import whisper
#from vosk import Model, KaldiRecognizer

global modelo
global recognizer

def f_initialize():
    
    global modelo
    global recognizer

    torch.cuda.is_available()
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

    print(DEVICE)

    modelo = whisper.load_model("base", device=DEVICE)




def f_record_speech(seconds):
    """
    Record speech for the specified number of seconds and save the recording as a temporary WAV file.

    :param seconds: The number of seconds to record for.
    :return: The path to the temporary WAV file.
    """

    # Set up the PyAudio object
    CHUNK = 8192
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    p = pyaudio.PyAudio()

    # Open a stream to record audio
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    # Start recording
    frames = []
    print("hablaaaa")
    for i in range(0, int(RATE / CHUNK * seconds)):
        data = stream.read(CHUNK)
        frames.append(data)

    # Stop recording
    stream.stop_stream()
    stream.close()
    p.terminate()

    print("guardando")

    # Save the recording as a temporary WAV file
    # save the recorded audio as a WAV file
    wave_file = wave.open("./whisper.wav", "wb")
    wave_file.setnchannels(CHANNELS)
    wave_file.setsampwidth(p.get_sample_size(FORMAT))
    wave_file.setframerate(RATE)
    wave_file.writeframes(b"".join(frames))
    wave_file.close()


def f_translate():
    global modelo
    
    print("whisper")
    audio = whisper.load_audio("./whisper.wav")
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(modelo.device)
    print("translating")

    options = whisper.DecodingOptions(language="es", without_timestamps=False, fp16 = False)
    result = whisper.decode(modelo, mel, options)
    print(result.text)




if __name__ == "__main__":
    f_initialize()
    f_record_speech(10)
    f_translate()


