import requests
import json
url = 'https://movie.douban.com/j/tv/recommend_groups?tag=%E7%83%AD%E9%97%A8'
headers = {
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}
resp = requests.get(url=url, headers=headers)
resp_dict = json.loads(resp.text)
print(resp_dict)