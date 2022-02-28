import requests
import re
from urllib.parse import urlparse, parse_qs
print("Enter your link:")
url = input()
r = requests.get(url, allow_redirects=False)
#with open('tmp.html', 'r') as f:
#    content = f.read()
pattern = re.compile("var url = '(https://.+)';", re.M|re.I)
match_obj = pattern.search(r.text)
detail_url = match_obj.group(1)
qs = parse_qs(urlparse(detail_url).query)
id = ''
#TODO has_sku = False
for k, v in qs.items():
    if k == 'id':
        id = v[0]

new_url = 'https://h5.m.taobao.com/cart/order.html?buyParam=' + id + '_1'
print(new_url)
