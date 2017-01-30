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
            """
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
            return jsonObject
        def recursive_xpath_selector(selector, pwd): # pwd default = "/html"
            """
            This function select all selector => parent to child selector
            """
            ### recursive all selector
            if selector:
                for i in selector.xpath('child::*'):
                    jsonObject = findAllAttr(i.extract())
                    jsonObject['text'] = i.xpath('text()').extract_first()
                    sub_pwd = pwd + "/" + jsonObject['tag']
                    if 'class' in jsonObject:
                        sub_pwd = sub_pwd + "["+ "{}".format(jsonObject['class']) + "]"
                    jsonObject['hierarchy'] = sub_pwd
                    jsonObject['status'] = 'active'
                    addJsonObjectToItem(jsonObject)
                    print(jsonObject)
                    recursive_xpath_selector(i, sub_pwd)
            else:
                print('Finished!!!')

        # Maybe <!doctype html> changing

        jsonObject = findAllAttr(response.css('html').extract_first())
        jsonObject['hierarchy'] = "/html"
        addJsonObjectToItem(jsonObject)
        recursive_xpath_selector(response, "/html")

        yield page
