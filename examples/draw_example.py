import requests
from craiyonapi import CraiyonAPI


def main():
    """Draw a picture of The Starry Night."""
    with requests.Session() as http_client:
        api = CraiyonAPI(model=CraiyonAPI.Model.Drawing)
        result = api.draw(http_client, "", "The Starry Night")
        print(result.images)


if __name__ == '__main__':
    main()
