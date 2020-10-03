import requests

cookies = {
    '__asc': 'f461b5bf174e839e9b62b481ad9',
    '__auc': 'f461b5bf174e839e9b62b481ad9',
    '__utmc': '212771392',
    '__utmz': '212771392.1601623944.1.1.utmcsr=(direct)^|utmccn=(direct)^|utmcmd=(none)',
    '__utmt': '1',
    '__utma': '212771392.337987579.1601623944.1601623944.1601623944.1',
    'uid-s': '06ec304-0956-429a-9b73-424fe342294f',
    'vsid': 'fecd0f53-a900-4002-8050-0dc0c2587d8b',
    '__atuvc': '2^%^7C40',
    '__atuvs': '5f76d7878cdfbecb001',
    '__utmb': '212771392.2.10.1601623944',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://english.tupaki.com/movie/review/V-/992',
    'Accept-Language': 'en-US,en;q=0.9',
    'If-None-Match': 'W/^\\^cdHQydcfPbeRWcHLzqkDGQ==^\\^',
}

response = requests.get('https://english.tupaki.com/movie/review/Bheeshma/976', headers=headers, cookies=cookies,verify=False)
print(response.text)