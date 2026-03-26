import pyttsx3

engine = pyttsx3.init()

engine.setProperty("rate", 160)

engine.say("Driver alert system is working correctly")

engine.runAndWait()