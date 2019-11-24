from spiderutil.network import API
from spiderutil.structure import TextDict


class Client(API):
    """
    API Client.
    """

    def __init__(self, proxies=None, timeout=None, retry=None):
        API.__init__(self, url='https://api.weibo.com/2/', proxies=proxies,
                     timeout=timeout, retry=retry)

    def get(self, url, **kwargs):
        if url[-5:] != '.json':
            url += '.json'
        r = super(Client, self).get(url, params=kwargs)
        return TextDict.load(r.text)

    def post(self, url, **kwargs):
        if url[-5:] != '.json':
            url += '.json'
        if 'pic' not in kwargs:
            r = super(Client, self).post(url, data=kwargs)
        else:
            files = {"pic": kwargs.pop("pic")}
            r = super(Client, self).post(url, data=kwargs, files=files)
        return TextDict.load(r.text)
