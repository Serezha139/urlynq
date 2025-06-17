import requests
import settings


class LynqService:
    def __init__(self):
        self.url = settings.LYNQ_API_URL
        self.secret = settings.LYNQ_SECRET

    def get_user_data(self, from_date="2023-01-01"):
        """
        Fetch user data from the Lynq server.

        Parameters:
        - from_date (str): Optional date string in 'YYYY-MM-DD' format.

        Returns:
        - dict: The server response or error.
        """
        payload = {
            "secret": self.secret,
            "from": from_date
        }

        try:
            response = requests.get(self.url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

lynq_service = LynqService()
