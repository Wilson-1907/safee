import requests
from app.config.settings import BACKEND_URL
from app.utils.logger import logger


class BackendClient:

    def send_voice(self, text):

        try:

            payload = {
                "driver_input": text
            }

            response = requests.post(BACKEND_URL, json=payload)

            data = response.json()

            return data.get("response")

        except Exception as e:

            logger.error(f"Backend error: {e}")

            return "System error. Please try again."