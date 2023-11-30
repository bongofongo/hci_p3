import sys
import pyttsx3

def init_engine():
    engine = pyttsx3.init()
    return engine

def say(s):
    engine.say(s)
    engine.runAndWait() # In here the program will wait as if is in main file

engine = init_engine()
engine.setProperty('voice', sys.argv[2])
engine.setProperty('rate', 180) 
engine.setProperty('volume',0.9) 

say(str(sys.argv[1])) # Here it will get the text through sys from main file