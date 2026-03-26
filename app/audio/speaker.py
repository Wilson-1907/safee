import pyttsx3
from app.config.settings import VOICE_RATE, VOICE_VOLUME


class Speaker:

    def __init__(self):

        self.engine = pyttsx3.init()

        self.engine.setProperty("rate", VOICE_RATE)

        self.engine.setProperty("volume", VOICE_VOLUME)

    def speak(self, message):

        print("AI:", message)

        self.engine.say(message)

        self.engine.runAndWait()