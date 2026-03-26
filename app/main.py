import asyncio
import json
import websockets

from app.audio.speaker import Speaker

WS_URL = "ws://localhost:8000/ws/driver-insights"

speaker = Speaker()


async def listen_for_insights():

    print("Waiting for AI model insights...")

    async with websockets.connect(WS_URL) as websocket:

        while True:

            message = await websocket.recv()

            data = json.loads(message)

            insight = data.get("message")

            if insight:

                print("AI Insight:", insight)

                speaker.speak(insight)


if __name__ == "__main__":

    asyncio.run(listen_for_insights())