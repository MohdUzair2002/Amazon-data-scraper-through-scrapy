import scrapy
from scrapy import Request
from time import sleep

class AmazonspiderSpider(scrapy.Spider):
    name = 'amazonspider'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.amazon.com/dp',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'If-None-Match': 'W/"920b0-r4F1aW4VVPGUx82CcYJ/tfctUf8"',
        'Cache-Control': 'max-age=0',
        'TE': 'trailers',
    }
    # allowed_domains = ['www.google.com']
    with open ('asd.csv') as file:
       start_urls = [line.strip() for line in file]
    def start_request(self):
      request=Request(url=self.start_urls,callback=self.parse)
      yield request
    def parse(self, response):
        # asin=response.xpath("//*[@class='a-size-base prodDetAttrValue']/text()")[-2].get()
        # price=response.xpath("//*[@class='a-offscreen']/text()").get()
        with open("Demo.txt","w",encoding="utf-8") as F:
          F.write(str(response.xpath("//html").get()))
        
        title=response.xpath("//*[@id='productTitle']/text()").get()
        price=response.xpath("//*[@class='a-offscreen']/text()").get()

        yield{
              'Title':title,
              # 'asin':asin,
              'price':price,
              
          }
