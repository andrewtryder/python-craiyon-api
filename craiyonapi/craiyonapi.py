import time
from typing import List, Tuple
import requests

# I assume these will change over time.
DRAW_VERSION = "35s5hfwn9n78gb06"
SEARCH_VERSION = "hpv3obayw36clkqp"


class CraiyonAPI:
    """
    CraiyonAPI is a client for the Craiyon AI art generation and search APIs.

    Attributes:
        Model: A class that contains constants for the available models, such as Art, Drawing, Photo, or NoneType.

    Methods:
        __init__: Initializes a new instance of the CraiyonAPI class.
        draw: Generates art from the provided prompt and negative prompt.
        search: Searches for images related to the provided text.
    """

    class Model:
        """
        A class that contains constants for the available models.
        """
        Art = "art"
        Drawing = "drawing"
        Photo = "photo"
        NoneType = "none"

    class GenerationResult:
        """
        A class that represents the result of the art generation.
        """
        def __init__(self, images: List[str], next_prompt: str, duration: float):
            """
            Initializes a new instance of the GenerationResult class.

            Parameters:
                images (List[str]): A list of image URLs.
                next_prompt (str): The next prompt returned by the API.
                duration (float): The duration of the generation in seconds.
            """
            self.images = images
            self.next_prompt = next_prompt
            self.duration = duration

    def __init__(self, model: str = Model.Drawing):
        """
        Initializes a new instance of the CraiyonAPI class.

        Parameters:
            model (str): The model to use for generation. Default is "drawing".
        """
        self.model = model

    def draw(self, http_client: requests.Session, negative_prompt: str, prompt: str) -> GenerationResult:
        """
        Generates art from the provided prompt and negative prompt.

        Parameters:
            http_client (requests.Session): The HTTP client to use for the request.
            negative_prompt (str): The negative prompt to use for the generation.
            prompt (str): The prompt to use for the generation.

        Returns:
            GenerationResult: The result of the generation.
        """
        start = time.monotonic()
        payload = {
            "model": self.model,
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "version": DRAW_VERSION
        }
        response = http_client.post("https://api.craiyon.com/v3", json=payload)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as error:
            raise ValueError(f"An error occurred: {error}")
        json_response = response.json()
        duration = time.monotonic() - start
        images = [f"https://img.craiyon.com/{path}" for path in json_response["images"]]
        return CraiyonAPI.GenerationResult(images, json_response["next_prompt"], duration)

    def search(self, http_client: requests.Session, text: str) -> List[Tuple[str, str]]:
        """
        Searches for images related to the provided text.

        Parameters:
            http_client (requests.Session): The HTTP client to use for the request.
            text (str): The text to search for.

        Returns:
            List[Tuple[str, str]]: A list of tuples containing the image URL and its description.
        """
        payload = {
            "text": text,
            "version": SEARCH_VERSION
        }
        response = http_client.post("https://search.craiyon.com/search", data=payload)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as error:
            raise ValueError(f"An error occurred: {error}")
        results = response.json()
        images = [(f"https://img.craiyon.com/{path}", description) for path, description in results]
        return images
