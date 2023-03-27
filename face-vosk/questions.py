import numpy
import tkinter
import vosk_real_time

global asked_questions
global rigth_answers
global children_answers
global children_name

#start the variables
def f_start_vars(name):
    global asked_questions
    global rigth_answers
    global children_answers
    global children_name

    asked_questions = []
    rigth_answers = []
    children_answers = []
    children_name = name

#method that starts the questionnaire and saves the answers
def f_start(name):
    f_start_vars(name=name)


#method to select random questions
def f_random_question():
    pass


#in charge of building the gui
def f_build_gui():
    pass


#in charge of taking the time to answer the question
def f_timer():
    pass


#mthod that saves all the answers given by the children in a file
def f_save_all():
    pass

#method that starts the recording for the microphone
def f_microphone():
    pass
