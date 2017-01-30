from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from tracker.items import TrackerItem, PageItem, HtmlTagItem
import os
import time
import hashlib


# scrapy crawl scrapydoc -o out.json
class ScrapyDocSpider(CrawlSpider):
    name = "scrapydoc"
    allowed_domains = ['scrapy.org', 'www.scrapy.org']
    start_urls = ['https://doc.scrapy.org/en/latest/']
    rules = (
        Rule(LinkExtractor(allow=(r'.*')), callback='parse_blog'),
    )

    def parse_blog(self, response):
        ### Downloading web page source
        directoryName = "./data/doc.scrapy.com/" + time.strftime("%Y-%d-%a-%H:%M") + "/"
        if not os.path.exists(directoryName):
            os.makedirs(directoryName)
        filename = directoryName + response.url.replace('/', '\\') + '.html' # Replace / to \ because your Os(Linux, Win)
        with open(filename, 'wb') as f:
            f.write(response.body)

        self.logger.info("Start url: %s", response.url)
        page = PageItem()
        page['url']         = response.url
        page['status']      = 'active'
        page['pageCode']    = ' ' # response.body
        page['pageHash']    = hashlib.md5(response.body).hexdigest()
        page['headHash']    = hashlib.md5(response.css('head').extract_first().encode('utf8')).hexdigest()
        page['bodyHash']    = hashlib.md5(response.css('body').extract_first().encode('utf8')).hexdigest()
        page['tags']        = []

        def addJsonObjectToItem(jsonObje):
            page['tags'].append(jsonObje)

        def findAllAttr(string):
            """
            - You must sent string type value like: <a href="asd" rel="asdas">asdas</a>
            - finding all attribute one tag and return json object
            - It is buggie.
            """
            print(string)
            print(type(string))
            jsonObject = {}
            okey = string.split('>')[0][1:] # String tag and attribute
            if okey.find(" ") != -1: # <head> <p class="asd"></head>
                okey[:okey.index(" ")]
                tagName = okey[:okey.index(" ")] # Index First Space, and find tag
                okey = okey[okey.index(" "):] # one space and All attribute key and value or nothing
                jsonObject['tag'] = tagName ### Tag name
            else:
                jsonObject['tag'] = okey
                okey = ""
            if okey != "" and okey != " ": ### if is true, there was less a attribute.
                okey = okey[1:] # erasing space
                while okey:
                    if okey.find("\" ") != -1:
                        something = okey[:okey.index("\" ")+1]
                        okey = okey[okey.index("\" ")+2:]
                        something = something.split("=")
                        if len(something) < 2:
                            jsonObject.update({something[0]:""})
                        else:
                            jsonObject.update({something[0]:something[1]})
                    else:
                        something = okey.split("=")
                        if len(something) < 2:
                            jsonObject.update({something[0]:""})
                        else:
                            jsonObject.update({something[0]:something[1]})
                        break
                """
                for attr in TagAndStringAttr[1:]:
                    little = attr.split("=")
                    if len(little) < 2: ### Beacuse,sometime there was like defer asyns tag
                        jsonObject.update({little[0]:""})
                    else:
                        jsonObject.update({little[0]:little[1]})
                """
            return jsonObject
        def recursive_xpath_selector(selector, parent_clas):
            """This function select all selector"""
            ### recursive all selector
            if selector:
                # print(selector)
                for i in selector.xpath('child::*'):
                    #print('####  ', i)
                    jsonObject = findAllAttr(i.extract())
                    #jsonObject['text'] = i.xpath('text()').extract_first()
                    #jsonObject.update({'status':"active"})
                    addJsonObjectToItem(jsonObject)
                    print(jsonObject)
                    sub_clas = i.css('::attr(class)').extract_first()
                    #print(type(parent_clas))
                    #print(parent_clas)
                    #print(type(sub_clas))
                    #print(sub_clas)
                    #print('$$$$$ ')
                    if sub_clas:
                        #print(type(sub_clas.encode("utf8")))
                        sub_clas = parent_clas + sub_clas + " "
                    else:
                        sub_clas = parent_clas
                    #print(sub_clas)
                    #print('~~~~~~')
                    #print(parent_clas)
                    #print(tags)
                    recursive_xpath_selector(i, sub_clas)
            else:
                print('Finished!!!')

        recursive_xpath_selector(response, "")
        """
        html = HtmlTagItem()
        html['head'] = ' ' # HeadTagItem()
        html['headHash'] = hashlib.md5(response.css('head').extract_first().encode('utf8')).hexdigest()
        html['body']     = ' ' # BodyTagItem()
        html['bodyHash'] = hashlib.md5(response.css('body').extract_first().encode('utf8')).hexdigest()
        page['html'] = html
        """
        yield page
