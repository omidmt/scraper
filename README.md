# Scapper

## Config
Make a copy conf/scraper.yaml.template as conf/scraper.yaml. Keep it in the same folder. Update the telegram bot info.
## Get Telegram Bot 
Follow this [guide](https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e) to create a bot and get token and chat id, used in conf/scraper.yaml.
## Run

```bash
docker run -d --restart unless-stopped --name scraper -e "TZ=Australia/Sydney" -v /home/omid/Projects/scraper:/app  omidmt/scrapper:1.0
```

### arm run
```
docker run -d --restart unless-stopped --name scraper -e "TZ=Australia/Sydney" -v /home/omid/Projects/scraper:/app  omidmt/scrapper:1.0-arm
```

## Build

```bash
docker build -t omidmt/scrapper:1.0 .
```

### arm image
```
docker build -t omidmt/python3-rust:3.8 -f Dockerfile.python3-rust .
docker build -t omidmt/scrapper:1.0-arm -f Dockerfile.arm32v7 .
```

### Debug Request by Scrapy Shell

```python
from scrapy import Request

headers = {
  'Host': ['www.example.com.au'],
  'Accept-Language': ['en-US,en;q=0.5'],
  'Accept-Encoding': ['gzip,deflate,br'],
  'Accept': ['text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'],
  'User-Agent': ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:86.0) Gecko/20100101 Firefox/86.0'],
  'DNT': ['1'],
  'Upgrade-Insecure-Requests': ['1'],
  'Connection': ['keep-alive'],
  'Upgrade-Insecure-Requests': ['1'],
  'Pragma': ['no-cache'],
  'Cache-Control': ['no-cache']
}

url = 'https://www.example.com.au/p/playstation-5-console/45454545'

request_object = Request(url, headers=headers)

fetch(request_object)
```