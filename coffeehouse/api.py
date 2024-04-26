import requests

from .exception import CoffeeHouseError


class API:
    """
    Base class for all CoffeeHouse services.
    It can be instantiated by itself as a holder for the API key,
    or it can be subclassed by CoffeeHouse services

    :param access_key: Access key from coffeehouse.intellivoid.net
    :param endpoint: Base URL for all requests, without the trailing slash
    """

    def __init__(
        self, access_key,
        endpoint='https://api.intellivoid.net/coffeehouse',
    ):
        """
        Public base constructor for CoffeeHouse API
        It can be instantiated by itself as a holder for the API key,
        or it can be subclassed by CoffeeHouse services

        :param access_key: Access key from coffeehouse.intellivoid.net
        :param endpoint: Base URL for all requests, without the trailing slash
        """
        if isinstance(access_key, API):
            self.access_key = access_key.access_key
            self.endpoint = access_key.endpoint
        else:
            self.access_key = access_key
            self.endpoint = endpoint

    def _send(self, path, access_key=True, **payload):
        """
        Send a request to the server configured by self.endpoint.

        :param path: The path over the base URL, without the preceding slash
        :type path: str
        :return: The response, parsed
        :rtype: dict
        """
        if access_key:
            payload['access_key'] = self.access_key
        response = requests.post(
            f"{self.endpoint}/{path}",
            json=payload,
        )
        request_id = response.headers.get('x-request-id')
        result = CoffeeHouseError.parse_and_raise(
            response.status_code,
            response.text,
            request_id,
        )
        return result.get('payload', result.get('results'))
