import json

from urllib.parse import urljoin

import requests


class ResponseStatusCodeException(Exception):
    pass


class RequestErrorException(Exception):
    pass


class MyTargetClient:

    def __init__(self, url, user, password):
        self.base_url = url
        self.session = requests.Session()

        self.user = user
        self.password = password
        self.csrf_token = None

        self.login()

    def _request(self, method, location=None, force_url=None,
                 status_code=200, headers=None, params=None, data=None, json=False):
        """
        wrapper over default requests.request method
        """

        url = urljoin(self.base_url, location)
        if force_url is None:
            self.url = url
        else:
            self.url = force_url

        response = self.session.request(method, self.url, headers=headers, params=params, data=data)

        if response.status_code != status_code:
            raise ResponseStatusCodeException(f' Got {response.status_code} {response.reason} for URL "{url}"')

        if json:
            json_response = response.json()

            if json_response.get('bStateError'):
                error = json_response['sErrorMsg']
                raise RequestErrorException(f'Request "{url}" dailed with error "{error}"!')
            return json_response
        return response

    def login(self):
        """
        auth method for MyTargetClient
        :return: response
        """
        method = 'POST'
        url = 'https://auth-ac.my.com/auth'
        params = {'lang': 'ru', 'nosavelogin': 0}
        headers = {
                   'Content-Type': 'application/x-www-form-urlencoded',
                   'Referer': 'https://target.my.com/'
                  }

        data = {
                'login': self.user,
                'password': self.password,
                'continue': 'https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email',
                'failure': 'https://account.my.com/login/'
                }

        response = self._request(method, force_url=url, headers=headers, params=params, data=data)

        method = 'GET'
        location = 'csrf'
        headers = {'Referer': 'https://target.my.com/auth/mycom?state=target_login%3D1'}
        self.csrf_token = self._request(method,
                                        location=location,
                                        headers=headers).headers['Set-Cookie'].split(';')[0].split('=')[-1]

        return response

    def create_segment(self, name):
        method = 'POST'
        location = 'api/v2/remarketing/segments.json'
        params = {
                           'fields': 'relations__object_type,'
                           'relations__object_id,'
                           'relations__params,'
                           'relations_count,'
                           'id,'
                           'name,'
                           'pass_condition,'
                           'created,'
                           'campaign_ids,'
                           'users,'
                           'flags'
                  }
        data = json.dumps({
                            "name": name,
                            "pass_condition": 1,
                            "relations": [{"object_type": "remarketing_player",
                            "params": {"type": "positive", "left": 365, "right": 0}}],
                            "logicType": "or"
                            })

        headers = {
                   'Content-Type': 'application/json',
                   'Referer': 'https://target.my.com/segments/segments_list/new/',
                   'X-CSRFToken': self.csrf_token
                   }
        response = self._request(method, location=location, params=params, headers=headers, data=data, json=True)
        return response

    def delete_segment(self, segment_id):
        method = 'DELETE'
        location = f'api/v2/remarketing/segments/{segment_id}.json'
        headers = {
                   'Referer': 'https://target.my.com/segments/segments_list',
                   'X-CSRFToken': self.csrf_token
                   }
        return self._request(method, location, headers=headers, status_code=204)

    def segment_list(self):
        method = 'GET'
        location = 'api/v2/remarketing/segments.json?limit=500'
        response = self._request(method, location=location, json=True)
        return response
