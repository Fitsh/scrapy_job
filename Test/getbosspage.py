import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
}
url = "https://www.zhipin.com/c101010100/?query=python&page=1"
print(requests.get(url, headers=headers).content.decode("utf-8"))