from urllib.parse import urlencode
from controller.exceptions import (CharacterNotFoundException,
                                   AnimeNotFoundException,
                                   MangaNotFoundException,
                                   TopNotFoundException,
                                   ServiceUnavailable)

from matplotlib.pyplot import imshow
import numpy as np
from PIL import Image
from io import BytesIO


class JikanGatewaysAPI(object):

    URL = 'https://api.jikan.moe/'

    def __init__(self, client_http):
        self.client = client_http

    def search_data(self):
        return self.client.get(self.URL)

    def search_character(self, name):
        resource = 'v3/search/character?'

        # traduz nosso dicionário python nos parametros de busca HTTP
        query_string = urlencode({'q': name})

        full_url = f'{self.URL}{resource}{query_string}'

        print(full_url)

        response = self.client.get(full_url)


        # Not Found
        if response.status_code == 404:
            raise CharacterNotFoundException(name)
        # Service Unavailable
        elif response.status_code == 503:
            raise ServiceUnavailable()

        return response

    def search_anime(self, name):
        resource = 'v3/search/anime?'

        # traduz nosso dicionário python nos parametros de busca HTTP
        query_string = urlencode({'q': name})

        full_url = f'{self.URL}{resource}{query_string}'

        print(full_url)

        response = self.client.get(full_url)


        # Not Found
        if response.status_code == 404:
            raise AnimeNotFoundException(name)
        # Service Unavailable
        elif response.status_code == 503:
            raise ServiceUnavailable()

        return response


    def search_manga(self, name):
            resource = 'v3/search/manga?'

            # traduz nosso dicionário python nos parametros de busca HTTP
            query_string = urlencode({'q': name})

            full_url = f'{self.URL}{resource}{query_string}'

            print(full_url)

            response = self.client.get(full_url)


            # Not Found
            if response.status_code == 404:
                raise MangaNotFoundException(name)
            # Service Unavailable
            elif response.status_code == 503:
                raise ServiceUnavailable()

            return response

    def get_top_mal(self, top_type):
        resource = 'v3/top/'

        # traduz nosso dicionário python nos parametros de busca HTTP

        full_url = f'{self.URL}{resource}{top_type}'

        print(full_url)

        response = self.client.get(full_url)
        # Not Found
        if response.status_code == 404 or response.status_code == 400:
            raise TopNotFoundException()
        # Service Unavailable
        elif response.status_code == 503:
            raise ServiceUnavailable()

        return response

class ImageViewer:
    def __init__(self, image, client_http):
        self.image = image
        self.client = client_http

    def print_picture(self):
        response = self.client.get(self.image)

        image = Image.open(BytesIO(response.content))
        image.show()


