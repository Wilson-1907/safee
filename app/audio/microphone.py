import speech_recognition as sr
from app.utils.logger import logger

class Microphone:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio)
            logger.info(f"Driver said: {text}")
            return text
        except Exception:
            logger.warning("Could not understand speech")
            return None