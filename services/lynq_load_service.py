import requests
import settings


class LynqService:
    def __init__(self):
        self.url = settings.LYNQ_API_URL
        self.secret = settings.LYNQ_SECRET

    def get_user_data(self):
        """
        Fetch user data from the Lynq server.

        Parameters:
        - from_date (str): Optional date string in 'YYYY-MM-DD' format.

        Returns:
        - dict: The server response or error.
        """
        has_more = True
        skip = 0
        result = []
        while has_more:
            try:
                payload = {
                    "secret": "k3vpy8drml0czu7fwbxnj1otqg5aes9k4yd2hcvxrw6um3lbnefa7tqijs0pzxlr",
                    "skip": skip,
                    "limit": settings.LYNQ_API_USER_LIMIT
                }
                response = requests.get(self.url, json=payload)
                response.raise_for_status()
                json = response.json().get("data")
                result.extend(json.get('users', []))
                has_more = json.get("pagination", {}).get("hasMore", False)
                skip += settings.LYNQ_API_USER_LIMIT
            except requests.exceptions.RequestException as e:
                return {"error": str(e)}

        return result

lynq_service = LynqService()
