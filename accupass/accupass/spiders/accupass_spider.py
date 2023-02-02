import scrapy
from scrapy_selenium import SeleniumRequest
from scrapy import Selector

class AccupassSpiderSpider(scrapy.Spider):
    name = 'accupass_spider'
    allowed_domains = ['accupass.com']
    start_urls = ['https://www.accupass.com/?area=north']

    def start_requests(self):
        yield SeleniumRequest(url='https://www.accupass.com/?area=north', callback=self.parse)

    def parse(self, response):
        self.extract_from_parent(response)

    # parent[[child],[child],[child]]
    def extract_from_parent(self,response):
        # time: style-05d4bd51-event-time
        # title: style-f13be39c-event-name
        # location: style-5a792945-event-location-type
        # tag: style-74411dd0-tag
        # 自顶向下 结构性提取信息 使用class定位最上层的父类列表
        cards=response.xpath('/html/body/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div/div/div/div/div[@class="style-bb526e47-theme-event-card-container"]')
        print("cards:")
        print(cards)
        print(type(cards))
        
        for card in cards:
            print("card:")
            print(card)
            print(type(card))
            title=card.css("p.style-f13be39c-event-name::text").get()
            time=card.css("p.style-05d4bd51-event-time::text").get()
            location=card.css("div.style-5a792945-event-location-type::text").get()
            tag=card.css("a.style-74411dd0-tag::text").get()
            print("title:"+str(title))
            print("time:"+str(time))
            print("location:"+str(location))
            print("tag:"+str(tag))
            print("========================")