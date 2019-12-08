# PyWeibo

![Version](https://img.shields.io/pypi/v/pyweibo)
![Download](https://img.shields.io/pypi/dm/pyweibo)
![License](https://img.shields.io/pypi/l/pyweibo)
![Status](https://img.shields.io/pypi/status/pyweibo)

Python SDK for Weibo API.

[中文文档](https://github.com/Thesharing/pyweibo/blob/master/README-zh.md)

## Installation

```bash
pip install pyweibo
```

## Preparation

1. Register the Sina Weibo account, and establish a new app in [open.weibo.com](https://open.weibo.com/apps).

2. Get `App Key` and `App Secret` from 应用信息 -> 基本信息

3. Set `Redirect URI` in 应用信息 -> 高级信息 -> OAuth2.0授权设置 as:

> https://api.weibo.com/oauth2/default.html

## Usage

### Authentication

Basic usage

```python
from pyweibo import Auth
auth = Auth()
```
When running, you need to manually input `App Key` and `App Token`:

```bash
App Key: <Your App Key>
App Secret: <Your App Secret>
```

Next the web browser will automatically open the redirect uri.

Copy the uri to the console, and the token will be generated:

```bash
Input the url or the token: <The URL or token>
```

Finally, the token will also be stored in `./token.json`.

As for advanced usages, you can specify:

* The way to read app key and secret from the local file: `LocalFileReader('./app.json')`

* The redirect uri, default is https://api.weibo.com/oauth2/default.html

## API Client

Basic usage

```python
from pyweibo import Auth, Client

# Get the token
auth = Auth()
token = auth.token.token

# Start the client
client = Client()
data = client.statuses.home_timeline.get(access_token=token)
```

* The APIs and their parameters can be referred from [official docs](https://open.weibo.com/wiki/%E5%BE%AE%E5%8D%9AAPI).

* You can access the api call like class attributes, where the last method call must be `get` or `post`. 

```python
client.api_name_1.api_name_2.get(param1=value1, param2=value2)
```

* Also you can use dict index like:
 
 ```python
client[api_name_1][api_name_2].get(param1=value1, param2=value2)
 ```

* The return value is a `TextDict`, where you can access the attributes directly like:

```python
user = data.statuses[0].user
```

* Also you can upload the picture with the parameter `pic`:

```python
with open('image.png', 'rb') as f:
    client.statuses.upload_pic.post(pic=f)
```

* For api like `2/statuses/upload` of which the url is https://upload.api.weibo.com/2/statuses/upload.json, use `UploadClient` instead of `Client`:

```python
from pyweibo import UploadClient

client = UploadClient()
with open('image.png', 'rb') as f:
    client.statuses.upload.post(status='Image', pic=f)
```

## Contribute

Project：[Thesharing/pyweibo](https://github.com/Thesharing/pyweibo)

Establish [new issue](https://github.com/Thesharing/pyweibo/issues/new) if there is any question or advice.

## Reference

[michaelliao/sinaweibopy](https://github.com/michaelliao/sinaweibopy)

[lxyu/weibo](https://github.com/lxyu/weibo)

[Thesharing/spider-util](https://github.com/thesharing/spider-util)
