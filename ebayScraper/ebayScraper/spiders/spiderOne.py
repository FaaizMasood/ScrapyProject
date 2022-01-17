import scrapy


class SpideroneSpider(scrapy.Spider):
    name = 'spiderOne'  # spider name
    # list of allowed domains as if it encounters any domain other then this then it will ignore
    allowed_domains = [
        'https://www.ebay.com/b/Lamps-Lighting-Ceiling-Fans/20697/bn_818527']
    # starting point
    start_urls = [
        'https://www.ebay.com/b/Lamps-Lighting-Ceiling-Fans/20697/bn_818527']

    # Parse is default name and it cannot be changed
    def parse(self, response):
        all_tvs = response.xpath(
            '//*[@class="s-item s-item__pl-on-bottom s-item--watch-at-corner"]')
        for tv in all_tvs:
            text = tv.xpath(
                './/*[@class="s-item__title"]/text()').extract_first()
            price = tv.xpath(
                './/*[@class="s-item__price"]/text()').extract_first()
            ratings = tv.xpath(
                './/*[@class="s-item__reviews"]//*[@class="clipped"]/text()').extract_first()
            discount = tv.xpath(
                './/*[@class="s-item__details clearfix"]//*[@class="s-item__detail s-item__detail--primary"]//*[@class="BOLD"]/text()').extract_first()

            next_page_url = response.xpath(
                "//*[@class='pagination__items']/li/a/@href").extract_first()
            absolute_nextPageUrl = response.urljoin(next_page_url)
            # yield{'text': text, 'price': price, 'ratings': ratings, 'discount': discount}
            yield scrapy.Request(absolute_nextPageUrl)
