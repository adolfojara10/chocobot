from pydub import AudioSegment
from pydub.playback import play, _play_with_simpleaudio
from multiprocessing import Process
from threading import Thread
import pygame
import os
import random


global audio_playing

def f_stop_sound():
    global audio_playing
    try:
        if audio_playing:
            audio_playing.terminate()
    except Exception as e:
        print("exception from stop(): ", e)


def f_check_sounds():
    pass

def f_good(game_level):


    #path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/good/"
    #path_to_audio = os.path.join(path_to_audio, f'{number_of_track}.mp3')
    #audio = AudioSegment.from_file(path_to_audio)
    #play(audio)

    if "simon_dice" in game_level:
        
        if game_level.split("_")[-1] == "facil":
            path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/good/Simon1.m4a"
            audio = AudioSegment.from_wav(path_to_audio)
            play(audio)

        elif game_level.split("_")[-1] == "medio":
            path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/good/Simon2.m4a"
            audio = AudioSegment.from_file(path_to_audio)
            play(audio)

        elif game_level.split("_")[-1] == "dificil":
            path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/good/Simon3.m4a"
            audio = AudioSegment.from_file(path_to_audio)
            play(audio)

    elif "conciencia_corporal" in game_level:
        
        if game_level.split("_")[-1] == "facil":
            path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/good/Espejo1.m4a"
            audio = AudioSegment.from_file(path_to_audio)
            play(audio)

        elif game_level.split("_")[-1] == "medio":
            path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/good/Espejo2.m4a"
            audio = AudioSegment.from_file(path_to_audio)
            play(audio)

        elif game_level.split("_")[-1] == "dificil":
            path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/good/Espejo3.m4a"
            audio = AudioSegment.from_file(path_to_audio)
            play(audio)

    elif "yoga" in game_level:
        
        if game_level.split("_")[-1] == "facil":
            path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/good/Yoga1.m4a"
            audio = AudioSegment.from_file(path_to_audio)
            play(audio)

        elif game_level.split("_")[-1] == "medio":
            path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/good/Yoga2.m4a"
            audio = AudioSegment.from_file(path_to_audio)
            play(audio)

        elif game_level.split("_")[-1] == "dificil":
            path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/good/Yoga3.m4a"
            audio = AudioSegment.from_file(path_to_audio)
            play(audio)

    elif "encuentra_diferencias" in game_level:

        if game_level.split("_")[-1] == "facil":
            path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/good/Objeto1.m4a"
            audio = AudioSegment.from_file(path_to_audio)
            play(audio)

        elif game_level.split("_")[-1] == "medio":
            path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/good/Objeto2.m4a"
            audio = AudioSegment.from_file(path_to_audio)
            play(audio)

        elif game_level.split("_")[-1] == "dificil":
            path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/good/Objeto3.m4a"
            audio = AudioSegment.from_file(path_to_audio)
            play(audio)

    elif "completa_imagen" in game_level:

        if game_level.split("_")[-1] == "facil":
            path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/good/Unir1.m4a"
            audio = AudioSegment.from_file(path_to_audio)
            play(audio)

        elif game_level.split("_")[-1] == "medio":
            path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/good/Unir2.m4a"
            audio = AudioSegment.from_file(path_to_audio)
            play(audio)

        elif game_level.split("_")[-1] == "dificil":
            path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/good/Unir3.m4a"
            audio = AudioSegment.from_file(path_to_audio)
            play(audio)

    elif "encuentra_objeto" in game_level:
        if game_level.split("_")[-1] == "facil":
            path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/good/Similar1.m4a"
            audio = AudioSegment.from_file(path_to_audio)
            play(audio)

        elif game_level.split("_")[-1] == "medio":
            path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/good/Similar2.m4a"
            audio = AudioSegment.from_file(path_to_audio)
            play(audio)

        elif game_level.split("_")[-1] == "dificil":
            path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/good/Similar3.m4a"
            audio = AudioSegment.from_file(path_to_audio)
            play(audio)

    elif "atencion_auditiva" in game_level:

        if game_level.split("_")[-1] == "facil":
            path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/good/Sonido1.m4a"
            audio = AudioSegment.from_file(path_to_audio)
            play(audio)

        elif game_level.split("_")[-1] == "medio":
            path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/good/Sonido2.m4a"
            audio = AudioSegment.from_file(path_to_audio)
            play(audio)

        elif game_level.split("_")[-1] == "dificil":
            path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/good/Sonido3.m4a"
            audio = AudioSegment.from_file(path_to_audio)
            play(audio)

    elif "sonidos_naturaleza" in game_level:
        if game_level.split("_")[-1] == "facil":
            path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/good/Sonido1.m4a"
            audio = AudioSegment.from_file(path_to_audio)
            play(audio)

        elif game_level.split("_")[-1] == "medio":
            path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/good/Sonido2.m4a"
            audio = AudioSegment.from_file(path_to_audio)
            play(audio)

        elif game_level.split("_")[-1] == "dificil":
            path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/good/Sonido3.m4a"
            audio = AudioSegment.from_file(path_to_audio)
            play(audio)



def f_bad2():
    random_number = random.randint(1, 77)
    #random_number = random.randint(1, 4)
    
    #audio_dir = os.path.expanduser('/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/bad/')
    audio_dir = os.path.expanduser('/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/negativosm4a')
    random_audio = str(random_number) + ".m4a"
    
    audio_path = os.path.join(audio_dir, random_audio)
    print(audio_path)
    audio = AudioSegment.from_file(audio_path)
    print("holaaaaa1")
    play(audio)
    print("holaaaaa2")



def f_bad():
    #random_number = random.randint(1, 77)
    random_number = random.randint(1, 4)
    
    audio_dir = os.path.expanduser('/home/catedra/Desktop/chocobot/chocobot/audios-estaticos/')
    #audio_dir = os.path.expanduser('/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audio/negativosm4a/')
    random_audio = str(random_number) + ".mp3"
    audio_path = os.path.join(audio_dir, random_audio)

    # Initialize Pygame and mixer
    pygame.mixer.init()

    # Load the audio file
    pygame.mixer.music.load(audio_path)

    # Play the audio
    pygame.mixer.music.play()

    # Wait for the audio to finish
    """while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)"""
   
    


def f_welcome():
    random_number = random.randint(1, 2)

    path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/saludo"
    sal = "Saludo" + str(random_number)
    random_audio = str(sal) + ".m4a"
    audio_path = os.path.join(path_to_audio, random_audio)
    audio = AudioSegment.from_file(audio_path)
    play(audio)   

def f_no_user():
    path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/"
    path_to_audio = os.path.join(path_to_audio, 'no_user.mp3')
    audio = AudioSegment.from_file(path_to_audio)
    play(audio)   

def f_student_saved():
    path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/"
    path_to_audio = os.path.join(path_to_audio, 'student_saved.mp3')
    audio = AudioSegment.from_file(path_to_audio)
    play(audio)   

"""
||
||
||
"""


def f_simon_dice():
    path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/"
    path_to_audio = os.path.join(path_to_audio, 'simon_dice.mp3')
    audio = AudioSegment.from_file(path_to_audio)
    play(audio)

def f_easy_simon(number_of_track):
    path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/simon/easy/"
    path_to_audio = os.path.join(path_to_audio, f'{number_of_track}.mp3')
    audio = AudioSegment.from_file(path_to_audio)
    play(audio)

def f_med_simon(number_of_track):
    path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/simon/med/"
    path_to_audio = os.path.join(path_to_audio, f'{number_of_track}.mp3')
    audio = AudioSegment.from_file(path_to_audio)
    play(audio)

def f_dif_simon(number_of_track):
    path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/simon/dif/"
    path_to_audio = os.path.join(path_to_audio, f'{number_of_track}.mp3')
    audio = AudioSegment.from_file(path_to_audio)
    play(audio)

"""
||
||
||
"""
def f_movenet():
    path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/"
    path_to_audio = os.path.join(path_to_audio, 'movenet.mp3')
    audio = AudioSegment.from_file(path_to_audio)
    play(audio)


def f_easy_movenet(number_of_track):
    path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/movenet/easy/"
    path_to_audio = os.path.join(path_to_audio, f'{number_of_track}.mp3')
    audio = AudioSegment.from_file(path_to_audio)
    play(audio)

def f_med_movenet(number_of_track):
    path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/movenet/med/"
    path_to_audio = os.path.join(path_to_audio, f'{number_of_track}.mp3')
    audio = AudioSegment.from_file(path_to_audio)
    play(audio)

def f_dif_movenet(number_of_track):
    path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/movenet/dif/"
    path_to_audio = os.path.join(path_to_audio, f'{number_of_track}.mp3')
    audio = AudioSegment.from_file(path_to_audio)
    play(audio)


"""
||
||
||
"""

def play_audio(audio):
    print("hola-------------------1")
    play(audio)
    print("hola-------------------2")



def f_play_audio_yoga(audio):
    global audio_playing
    """print("hola-------------------1")
    audio_playing = Process(target=play, args=(audio))
    audio_playing.start()
    audio_playing.join()
    print("hola-------------------2")"""

    audio_thread = Thread(target=play_audio, args=(audio,))
    audio_thread.start()
    audio_thread.join()


def f_yoga(game_level):
    global audio_playing
    """path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/"
    path_to_audio = os.path.join(path_to_audio, 'yoga.mp3')
    audio = AudioSegment.from_file(path_to_audio)
    play(audio)"""

    if game_level.split("_")[-1] == "facil":
        path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/yoga/YogaSesion1.mp3"
        #path_to_audio = os.path.expanduser('/home/catedra/Desktop/chocobot/chocobot/audios-estaticos/YogaSesion1.mp3')
        audio = AudioSegment.from_file(path_to_audio)
        f_play_audio_yoga(audio)

    elif game_level.split("_")[-1] == "medio":
        path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/yoga/YogaSesion2.mp3"
        audio = AudioSegment.from_file(path_to_audio)
        f_play_audio_yoga(audio)

    elif game_level.split("_")[-1] == "dificil":
        path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/yoga/YogaSesion3.mp3"
        audio = AudioSegment.from_file(path_to_audio)
        f_play_audio_yoga(audio)
    


"""
def f_easy_yoga(number_of_track):
    path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/yoga/easy/"
    path_to_audio = os.path.join(path_to_audio, f'{number_of_track}.mp3')
    audio = AudioSegment.from_file(path_to_audio)
    play(audio)

def f_med_yoga(number_of_track):
    path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/yoga/med/"
    path_to_audio = os.path.join(path_to_audio, f'{number_of_track}.mp3')
    audio = AudioSegment.from_file(path_to_audio)
    play(audio)

def f_dif_yoga(number_of_track):
    path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/yoga/dif/"
    path_to_audio = os.path.join(path_to_audio, f'{number_of_track}.mp3')
    audio = AudioSegment.from_file(path_to_audio)
    play(audio)"""

"""
||
||
||
"""

def f_encuentra_diferencias():
    path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/"
    path_to_audio = os.path.join(path_to_audio, 'encuentra_diferencias.mp3')
    audio = AudioSegment.from_file(path_to_audio)
    play(audio)  


def f_completa_imagen():
    path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/"
    path_to_audio = os.path.join(path_to_audio, 'completa_imagen.mp3')
    audio = AudioSegment.from_file(path_to_audio)
    play(audio)  


def f_encuentra_objeto():
    path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/"
    path_to_audio = os.path.join(path_to_audio, 'encuentra_objeto.mp3')
    audio = AudioSegment.from_file(path_to_audio)
    play(audio)  


def f_atencion_auditiva():
    path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/"
    path_to_audio = os.path.join(path_to_audio, 'atencion_auditiva.mp3')
    audio = AudioSegment.from_file(path_to_audio)
    play(audio)  


def f_sonidos_naturaleza():
    path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/"
    path_to_audio = os.path.join(path_to_audio, 'sonidos_naturaleza.mp3')
    audio = AudioSegment.from_file(path_to_audio)
    play(audio)  

#if __name__ == "__main__":
#    f_good(1)
