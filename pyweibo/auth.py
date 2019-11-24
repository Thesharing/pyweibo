import re
import webbrowser
import urllib.parse as urlparse
from datetime import datetime
from spiderutil.network import API
from spiderutil.exceptions import AuthenticationFailedException

from .reader import BaseReader, LocalFileReader, AppInfoInputReader
from .token import Token, AppInfo


class Auth:
    """
    Authentication.
    Get token with initialization of Auth.
    """

    def __init__(self, token_reader: BaseReader = None,
                 info_reader: BaseReader = None,
                 api_session: API = None,
                 redirect_uri='https://api.weibo.com/oauth2/default.html'):
        """
        auth = Auth() will initialize and query the token.
        :param token_reader: Read the token.
        :param info_reader: Read the app key and secret.
        :param api_session: Network _session.
        :param redirect_uri: URL to redirect.
        """
        self._token_reader = LocalFileReader(
            './token.json') if token_reader is None else token_reader
        self._session = API(
            'https://api.weibo.com/') if api_session is None else api_session
        if self._token_reader.exists():
            token = Token.from_dict(self._token_reader.read())
            if int(token.expire_time) * 10 > datetime.now().timestamp():
                self._token = token
            else:
                self._token = self.authorize(info_reader=info_reader,
                                             redirect_uri=redirect_uri)
                self._token_reader.write(self._token)
        else:
            self._token = self.authorize(info_reader=info_reader,
                                         redirect_uri=redirect_uri)
            self._token_reader.write(self._token)

    @property
    def token(self):
        """
        Get the token
        :return: Token, contains token value and expire time
        """
        return self._token

    def authorize(self, info_reader: BaseReader = None,
                  redirect_uri='https://api.weibo.com/oauth2/default.html'):
        """
        Read the app key and secret, and query the token.
        :param info_reader: Read the app key and secret.
        :param redirect_uri: URL to redirect.
        :return:
        """
        if info_reader is None:
            info_reader = AppInfoInputReader('./app.json')
        app_info = AppInfo.from_dict(info_reader.read())
        webbrowser.open(
            self._url('authorize') + '?client_id={}&redirect_uri={}'.format(
                app_info.key, redirect_uri))
        raw_str = input('Input the url or the token: ')
        code = self._extract_code(raw_str)
        data = {
            'client_id': app_info.key,
            'client_secret': app_info.secret,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': redirect_uri
        }
        r = self._session.oauth2.access_token.post(data=data)
        token = Token.from_str(r.text)
        return token

    @staticmethod
    def _url(url):
        """
        Generate the full URL.
        """
        return urlparse.urljoin('https://api.weibo.com/oauth2/', url)

    @staticmethod
    def _extract_code(code):
        """
        Extract the access code from full URL.
        :param code: Plain code or URL.
        :return: Plain code.
        """
        if '?code=' in code:
            res = re.search(r'\?code=(.+)$', code)
            if res is not None:
                code = res.group(1)
        if len(code) == 32:
            return code
        else:
            raise AuthenticationFailedException()
