import pyttsx3

# Initialize engine
engine = pyttsx3.init()

# Voice settings
engine.setProperty("rate", 160)   # speed
engine.setProperty("volume", 1.0) # max volume

def speak_alert(message):
    print("AI:", message)
    engine.say(message)
    engine.runAndWait()


# 🚨 Example: Drowsy Driver Alert
speak_alert("Warning. Driver appears drowsy. Please take a break for twenty minutes as soon as possible.")