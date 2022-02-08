from scrapy import Spider
from scrapy.loader import ItemLoader
from ebayScraper.items import EbayscraperItem


class SpideroneSpider(Spider):
    name = 'spiderOne'  # spider name
    # list of allowed domains as if it encounters any domain other then this then it will ignore
    allowed_domains = [
        'quotes.toscrape.com/']
    # starting point
    start_urls = [
        'https://quotes.toscrape.com/']

    # Parse is default name and it cannot be changed
    def parse(self, response):
        quotes = response.xpath(
            '//*[@class="quote"]')
        for quote in quotes:
            text = quote.xpath(
                './/*[@class="text"]/text()').extract_first()
            author = quote.xpath(
                './/*[@class="author"]/text()').extract_first()
            tags = quote.xpath(
                './/*[@class="keywords"]/@content').extract_first()

            # next_page_url = response.xpath(
            #     "//*[@class='next']/a/@href").extract_first()
            # absolute_nextPageUrl = response.urljoin(next_page_url)
            yield{'text': text, 'author': author, 'tags': tags}
            # yield scrapy.Request(absolute_nextPageUrl)


# Old Code


# l = ItemLoader(item=EbayscraperItem(), response=response)

#         text = response.xpath(
#             './/*[@class="text"]/text()').extract_first()
#         author = response.xpath(
#             './/*[@class="author"]/text()').extract_first()
#         tag = response.xpath(
#             './/*[@class="keywords"]/@content').extract_first()
#         l.add_value('text', text)
#         l.add_value('tag', tag)
#         l.add_value('author', author)

#         return l.load_item()
