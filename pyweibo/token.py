import json


class AppInfo:

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret

    def __str__(self):
        return json.dumps({
            'app_key': self.key,
            'app_secret': self.secret
        }, ensure_ascii=False)

    @classmethod
    def from_dict(cls, d):
        return AppInfo(d['app_key'], d['app_secret'])

    @classmethod
    def from_str(cls, s):
        d = json.loads(s)
        return cls.from_dict(d)

    @classmethod
    def from_file(cls, path):
        with open(path, 'r', encoding='utf-8') as f:
            s = f.read()
            return cls.from_str(s)


class Token:

    def __init__(self, token, expire_time):
        self.token = token
        self.expire_time = expire_time

    def __str__(self):
        return json.dumps({
            'access_token': self.token,
            'expires_in': self.expire_time
        }, ensure_ascii=False)

    @staticmethod
    def from_dict(d):
        return Token(d['access_token'], d['expires_in'])

    @classmethod
    def from_str(cls, s):
        d = json.loads(s)
        return cls.from_dict(d)

    @classmethod
    def from_file(cls, path):
        with open(path, 'r', encoding='utf-8') as f:
            s = f.read()
            return cls.from_str(s)
