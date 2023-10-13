from pydub import AudioSegment
from pydub.playback import play
import os

def f_good(number_of_track):
    path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/good/"
    path_to_audio = os.path.join(path_to_audio, f'{number_of_track}.mp3')
    audio = AudioSegment.from_file(path_to_audio)
    play(audio)

def f_bad(number_of_track):
    path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/bad/"
    path_to_audio = os.path.join(path_to_audio, f'{number_of_track}.mp3')
    audio = AudioSegment.from_file(path_to_audio)
    play(audio)

def f_welcome():
    path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/"
    path_to_audio = os.path.join(path_to_audio, 'welcome.mp3')
    audio = AudioSegment.from_file(path_to_audio)
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

def f_yoga():
    path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/"
    path_to_audio = os.path.join(path_to_audio, 'yoga.mp3')
    audio = AudioSegment.from_file(path_to_audio)
    play(audio)


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
    play(audio)

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
