# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TrackerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class PageItem(scrapy.Item):
    """
    <html>
        <head></body>
        <body></body>
    </html>
    """
    url         = scrapy.Field() # page url
    status      = scrapy.Field() # active, deactive, new, old => page status
    pageCode    = scrapy.Field() # page html tag code
    pageHash    = scrapy.Field() # page  md5 value
    headHash    = scrapy.Field() # page head hash
    bodyHash    = scrapy.Field() #
    tags        = scrapy.Field() #

class HtmlTagItem(scrapy.Item):
    head        = scrapy.Field() # HeadTagItem()
    headHash    = scrapy.Field() # Head tag source code hash
    body        = scrapy.Field() # BodyTagItem()
    bodyHash    = scrapy.Field() # Body tag source code hash

class HeadTagItem(scrapy.Item):
    headCode    = scrapy.Field() # Head tag source code
    headParsing = scrapy.Field() # some tag

class BodyTagItem(scrapy.Item):
    bodyCode    = scrapy.Field() # Body tag source code
    bodyParsing = scrapy.Field() # some tag

class TagItem(scrapy.Item):
    pass
