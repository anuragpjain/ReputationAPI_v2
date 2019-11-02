
"""Small code alternative to avoid going  to postman app and hit from there"""
import requests

URL = "http://127.0.0.1:5000/rep.cal"


PARAMS = {
    "machine_id": "7",
    "product_id": "1",
    "file_md5": "d77d2953c546cb33e2d0bff4989f6aa2",
    "url_md5": "d77d2953c546cb33e2d0bff4989f6aa3",
    "digisign_md5": "d77d2953c546cb33e2d0bff4989f6aa4"
}
r = requests.post(url=URL, json=PARAMS)
print(r.content.decode(encoding='utf-8'))
