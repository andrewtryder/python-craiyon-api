[![DeepSource](https://app.deepsource.com/gh/andrewtryder/python-craiyon-api.svg/?label=active+issues&show_trend=true&token=c9LIx6WG61VNwnUxU6tV-3dv)](https://app.deepsource.com/gh/andrewtryder/python-craiyon-api/?ref=repository-badge)[![DeepSource](https://app.deepsource.com/gh/andrewtryder/python-craiyon-api.svg/?label=resolved+issues&show_trend=true&token=c9LIx6WG61VNwnUxU6tV-3dv)](https://app.deepsource.com/gh/andrewtryder/python-craiyon-api/?ref=repository-badge)
# python-craiyon-api

python-craiyon-api is a Python Library for interacting with the unofficial Craiyon API.

## Installation

Grab this library and build. 

## Usage

Here's an example of how to use the module to generate a drawing:

```python
import requests
from craiyonapi import CraiyonAPI

http_client = requests.Session()
api = CraiyonAPI()

prompt = "Draw a cat playing the piano"
negative_prompt = "Don't draw a dog playing the guitar"
result = api.draw(http_client, negative_prompt, prompt)

for image in result.images:
    print(image)

print(f"Next prompt: {result.next_prompt}")
print(f"Generation duration: {result.duration} seconds")
```

## Contributing

Submit a PR

## Licence 

This module is released under the MIT License.
