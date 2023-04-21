import requests
from craiyonapi import CraiyonAPI


def main():
    with requests.Session() as http_client:
        api = CraiyonAPI(model=CraiyonAPI.Model.Photo)
        results = api.search(http_client, "mountain")
        for image, description in results:
            print(image, description)


if __name__ == '__main__':
    main()
