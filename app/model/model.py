from tools import WeatherAPI
from app.model.rag_client import RAG

class DriverAssistantModel:
    def __init__(self, weather_api_key):
        self.weather = WeatherAPI(weather_api_key)
        self.rag = RAG()

    def answer(self, question):
        question_lower = question.lower()

        # weather query
        if "weather" in question_lower:
            # try to extract city
            words = question_lower.split()
            city = None
            for i, w in enumerate(words):
                if w in ["in", "at"] and i+1 < len(words):
                    city = words[i+1]
                    break
            city = city if city else "Karatina"
            return self.weather.get_weather(city)

        # blackspot query
        elif "blackspot" in question_lower or "dangerous road" in question_lower:
            return self.rag.query(question)

        # fallback
        else:
            return "I am monitoring your driving. I cannot answer that yet."