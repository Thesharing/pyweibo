# PyWeibo

![Version](https://img.shields.io/pypi/v/pyweibo)
![Download](https://img.shields.io/pypi/dm/pyweibo)
![License](https://img.shields.io/pypi/l/pyweibo)
![Status](https://img.shields.io/pypi/status/pyweibo)

Python SDK for Weibo API.

## 安装

```bash
pip install pyweibo
```

## 准备工作

1. 注册微博帐户，在[微博开放平台](https://open.weibo.com/apps)中创建新应用；

2. 在 应用信息 -> 基本信息 获取`App Key`和`App Secret`；

3. 在 应用信息 -> 高级信息 -> OAuth2.0 授权设置 中设置`授权回调页`为：

> https://api.weibo.com/oauth2/default.html

## 使用说明

### OAuth2 鉴权

基本用法

```python
from pyweibo import Auth
auth = Auth()
```
在运行时，需要手动输入`App Key`和`App Token`：

```bash
App Key: <Your App Key>
App Secret: <Your App Secret>
```

接下来系统默认浏览器会自动打开授权回调页。

将地址栏的地址复制粘贴到终端中，即可产生Token。

```bash
Input the url or the token: <The URL or the token>
```

最终，Token会被保存在`./token.json`文件中以便日后使用。

除此以外还可以修改：

* 读取`App key`和`App Secret`的方式，可以从本地文件读取：`LocalFileReader('./app.json')`

* 授权回调页，默认值为https://api.weibo.com/oauth2/default.html

## API Client

基本用法

```python
from pyweibo import Auth, Client

# Get the token
auth = Auth()
token = auth.token.token

# Start the client
client = Client()
data = client.statuses.home_timeline.get(access_token=token)
```

* 所有API方法及其参数可以在[官方文档](https://open.weibo.com/wiki/%E5%BE%AE%E5%8D%9AAPI)查询。

* 可以以类属性的形式访问微博API，其中最后一个方法调用必须是 `get` 或者 `post` ，根据文档决定。

```python
client.api_name_1.api_name_2.get(param1=value1, param2=value2)
```

* 所有API参数以方法参数的形式传递即可。 

* 还可以通过 Dict Index 的方式调用API：

```python
client[api_name_1][api_name_2].get(param1=value1, param2=value2)
```

* 方法返回值类型为`TextDict`，所有值都会被封装为可以直接访问的属性：

```python
user = data.statuses[0].user
```

* 通过`pic`参数可以上传图片：

```python
with open('image.png', 'rb') as f:
    client.statuses.upload_pic.post(pic=f)
```

* 对于 `2/statuses/upload` 等地址为 https://upload.api.weibo.com/2/statuses/upload.json 的API，用 `UploadClient` 代替 `Client`:

```python
from pyweibo import UploadClient

client = UploadClient()
with open('image.png', 'rb') as f:
    client.statuses.upload.post(status='Image', pic=f)
```

## Contribute

项目地址：[Thesharing/pyweibo](https://github.com/Thesharing/pyweibo)

在使用过程中遇到问题可以[提出Issue](https://github.com/Thesharing/pyweibo/issues/new)。

## Reference

[michaelliao/sinaweibopy](https://github.com/michaelliao/sinaweibopy)

[lxyu/weibo](https://github.com/lxyu/weibo)

[Thesharing/spider-util](https://github.com/thesharing/spider-util)
