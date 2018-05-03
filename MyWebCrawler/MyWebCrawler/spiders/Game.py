from scrapy.loader import ItemLoader
import scrapy

class Game(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    link = scrapy.Field()
    imgLink = scrapy.Field()
    released = scrapy.Field()
    hasWinSup = scrapy.Field()
    hasMacSup = scrapy.Field()
    hasLinSup = scrapy.Field()
    hasHTCSup = scrapy.Field()
    hasOcuSup = scrapy.Field()
    reviewSum = scrapy.Field()

class GameLoader(ItemLoader):
    tagLink = 'a::attr(href)'
    tagImgLink = 'div.col.search_capsule img::attr(src)'
    tagPrice = 'div.col.search_price.responsive_secondrow::text'
    tagPrice2 = 'div.col.search_price.responsive_secondrow span strike::text'
    tagName = 'span.title::text'
    tagReleased = 'div.col.search_released.responsive_secondrow::text'
    tagWinSup = 'span.platform_img.win'
    tagMacSup = 'span.platform_img.mac'
    tagLinSup = 'span.platform_img.linux'
    tagHTCSup = 'span.platform_img.htcvive'
    tagOcuSup = 'span.platform_img.oculusrift'
    tagVeryPos = 'span.search_review_summary.positive::attr(data-tooltip-html)'
    tagVeryNeg = 'span.search_review_summary.negative::attr(data-tooltip-html)'

    def __init__(self,row):
        super(GameLoader, self).__init__(Game(),row)
        self.add_css('name', self.tagName)
        self.add_css('price', self.tagPrice)
        self.add_css('price', self.tagPrice2)
        self.add_css('link', self.tagImgLink)
        self.add_css('imgLink', self.tagLink)
        self.add_css('released', self.tagReleased)
        self.add_value('hasWinSup',['False']) if row.css(self.tagWinSup).extract_first() is None else self.add_value('hasWinSup',['True'])
        self.add_value('hasMacSup',['False']) if row.css(self.tagMacSup).extract_first() is None else self.add_value('hasMacSup',['True'])
        self.add_value('hasLinSup',['False']) if row.css(self.tagLinSup).extract_first() is None else self.add_value('hasLinSup',['True'])
        self.add_value('hasHTCSup',['False']) if row.css(self.tagHTCSup).extract_first() is None else self.add_value('hasHTCSup',['True'])
        self.add_value('hasOcuSup',['False']) if row.css(self.tagOcuSup).extract_first() is None else self.add_value('hasOcuSup',['True'])
        if row.css(self.tagVeryPos).extract_first() is not None: self.add_value('reviewSum',row.css(self.tagVeryPos).extract_first())
        if row.css(self.tagVeryNeg).extract_first() is not None: self.add_value('reviewSum',row.css(self.tagVeryPos).extract_first())