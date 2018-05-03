import scrapy
from scrapy.loader import ItemLoader
from .Game import GameLoader

class SpiderSteam(scrapy.Spider):
    name = "SpiderSteam"

    def start_requests(self):
        urls = [
            'https://store.steampowered.com/search/?sort_by=Released_DESC&category1=998'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for row in response.xpath('//a[contains(@class, "search_result_row")]'):            
            yield GameLoader(row).load_item()
            
        next_page = response.css('a.pagebtn::attr(href)').extract()[-1]
        if next_page is not None:
            total_items = response.css('div.search_pagination_left::text').extract_first().strip().split(' ')
            if total_items[3].isdigit() and total_items[5].isdigit():
                if int(total_items[3])/int(total_items[5]) < 1:
                    next_page = response.urljoin(next_page)
                    yield scrapy.Request(next_page, callback=self.parse)