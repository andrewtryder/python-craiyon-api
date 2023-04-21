import unittest
import requests
from craiyonapi import CraiyonAPI


class TestCraiyonAPI(unittest.TestCase):
    def setUp(self):
        self.http_client = requests.Session()

    def tearDown(self):
        self.http_client.close()

    def test_drawing_generation(self):
        api = CraiyonAPI()
        result = api.draw(self.http_client, "", "The Starry Night")
        self.assertIsInstance(result, CraiyonAPI.GenerationResult)
        self.assertGreater(len(result.images), 0)
        self.assertGreater(result.duration, 0)

    def test_search(self):
        api = CraiyonAPI()
        results = api.search(self.http_client, "cat")
        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)
        self.assertIsInstance(results[0], tuple)
        self.assertIsInstance(results[0][0], str)
        self.assertIsInstance(results[0][1], str)


if __name__ == '__main__':
    unittest.main()
