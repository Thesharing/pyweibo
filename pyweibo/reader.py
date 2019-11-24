import json
import os
from abc import abstractmethod


class BaseReader:

    def __init__(self):
        pass

    @abstractmethod
    def read(self) -> dict:
        raise NotImplementedError

    @abstractmethod
    def write(self, obj):
        raise NotImplementedError

    @abstractmethod
    def exists(self):
        raise NotImplementedError


class LocalFileReader(BaseReader):

    def __init__(self, path):
        BaseReader.__init__(self)
        self.path = path

    def read(self) -> dict:
        with open(self.path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data

    def write(self, obj):
        with open(self.path, 'w', encoding='utf-8') as f:
            f.write(str(obj))

    def exists(self):
        return os.path.isfile(self.path)


class AppInfoInputReader(LocalFileReader):

    def __init__(self, path):
        LocalFileReader.__init__(self, path)

    def read(self) -> dict:
        app_key = input('App Key: ')
        app_secret = input('App Secret: ')
        return {
            'app_key': app_key,
            'app_secret': app_secret
        }


class TokenInputReader(LocalFileReader):

    def __init__(self, path):
        LocalFileReader.__init__(self, path)

    def read(self) -> dict:
        access_token = input('Token: ')
        expires_in = input('Expires in: ')
        return {
            'access_token': access_token,
            'expires_in': expires_in
        }
