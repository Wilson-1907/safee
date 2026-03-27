# app/api/backend_client.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import requests, os
from dotenv import load_dotenv
from app.model.rag_client import RAGClient
# from app.model.groq_client import ask_groq  # Placeholder for Groq integration
from app.utils.logger import logger

# Load environment variables
load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# Backend constants
BACKEND_PORT = 9000

# Initialize RAG client (PDFs inside app/model/data/)
rag_client = RAGClient()

# Flask app
app = Flask(__name__)
CORS(app)  # Allow frontend JS

@app.route("/api/voice", methods=["POST"])
def voice():
    data = request.json
    driver_input = data.get("driver_input", "").strip()

    responses = []

    # --- Weather query ---
    if "weather in" in driver_input.lower():
        try:
            city = driver_input.lower().split("weather in")[-1].strip()
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
            resp = requests.get(url).json()

            if "main" in resp:
                temp = resp["main"]["temp"]
                desc = resp["weather"][0]["description"]
                responses.append(f"The weather in {city.title()} is {desc}, {temp}°C")
            else:
                responses.append(f"Could not find weather info for {city.title()}")
        except Exception as e:
            logger.error(f"Weather API error: {e}")
            responses.append("Error fetching weather data. Please try again.")

    # --- RAG query ---
    try:
        rag_answer = rag_client.ask(driver_input)
        if rag_answer:
            responses.append(f"Insight from documents: {rag_answer}")
    except Exception as e:
        logger.error(f"RAG error: {e}")
        responses.append("Error fetching document insights.")

    # --- Placeholder for Groq API ---
    # try:
    #     groq_answer = ask_groq(driver_input)
    #     responses.append(f"Groq says: {groq_answer}")
    # except Exception as e:
    #     logger.error(f"Groq API error: {e}")

    # Combine all responses
    final_response = " | ".join(responses) if responses else "Sorry, I couldn't understand that."
    return jsonify({"response": final_response})


if __name__ == "__main__":
    logger.info(f"Driver Voice Interface Started on port {BACKEND_PORT}")
    app.run(port=BACKEND_PORT, debug=True)