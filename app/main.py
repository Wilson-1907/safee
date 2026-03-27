import threading
import time

from app.audio.microphone import Microphone
from app.audio.speaker import Speaker
from app.api.backend_client import BackendClient
from app.api.insight_fetcher import get_latest_insight

mic = Microphone()
speaker = Speaker()
backend = BackendClient()

last_insight = None


# 🎤 DRIVER LISTENING LOOP
def listen_loop():
    while True:
        text = mic.listen()

        if not text:
            continue

        print("Driver:", text)

        response = backend.send_voice(text)

        if response:
            speaker.speak(response)


# 🌐 INSIGHT LOOP (INTERRUPTS)
def insight_loop():
    global last_insight

    while True:
        insight = get_latest_insight()

        if insight and insight != last_insight:
            print("🚨 NEW INSIGHT:", insight)

            # INTERRUPT SPEAK
            speaker.speak("Alert! " + insight)

            last_insight = insight

        time.sleep(3)  # check every 3 seconds


if __name__ == "__main__":
    print("🚗 Driver AI System Started")

    t1 = threading.Thread(target=listen_loop)
    t2 = threading.Thread(target=insight_loop)

    t1.start()
    t2.start()

    t1.join()
    t2.join()