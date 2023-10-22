from requests import get, post
import time

headers = {
"Accept": "*/*",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "he,en-US;q=0.9,en;q=0.8",
"Connection": "keep-alive",
"Content-Type": "application/json;charset=utf-8",
"Cookie": 'AlertSound=0; Lastalerts=; SilenceWaveAll=0; ListEmergency=[]; ASP.NET_SessionId=fqg5ghofyai551ae23x5k0yf; TS013a1194=01feb52f0adc93a4a1f347cf69658dca8ac262e5e4dada96c046e8cbd0208f9bc690dc1d8b2cd8b07a826db836cdd4a031863dee298129856e475f2e3397eabe8b168a647f; _ga_V2BQHCDHZP=GS1.1.1697932684.1.1.1697933840.60.0.0; _ga=GA1.1.950058810.1697932685',
"DNT": "1",
"Host": "www.oref.org.il",
"If-Modified-Since": "Sun, 22 Oct 2023 00:22:16 GMT",
"If-None-Match": 'W/"6467bdcf7d4da1:0"',
"Referer": "https://www.oref.org.il/12481-he/Pakar.aspx",
"Sec-Fetch-Dest": "empty",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Site": "same-origin",
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
"X-Requested-With": "XMLHttpRequest",
"sec-ch-ua": '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": "Linux"

}

url = 'http://www.oref.org.il/WarningMessages/alert/alerts.json'


while 1:
    

    r = get(url, headers=headers)
    r.raise_for_status()
    if r.content != b'\xef\xbb\xbf\r\n':
        print(time.ctime())
        print(r)
        print(r.content)
        print(r.text)
    time.sleep(3)
