import scrapy


class SpideroneSpider(scrapy.Spider):
    name = 'spiderOne'  # spider name
    # list of allowed domains as if it encounters any domain other then this then it will ignore
    allowed_domains = [
        'https://www.ebay.com/sch/i.html?_nkw=TVs&_sacat=11071&_trkparms=pageci%3A8317b07f-6a6d-11ec-89a1-c661edad1081%7Cparentrq%3A11e7d26717e0a77d31d299d7fff6f78c%7Ciid%3A1']
    start_urls = ['https://www.ebay.com/sch/i.html?_nkw=TVs&_sacat=11071&_trkparms=pageci%3A8317b07f-6a6d-11ec-89a1-c661edad1081%7Cparentrq%3A11e7d26717e0a77d31d299d7fff6f78c%7Ciid%3A1']  # starting point

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
            # print('\n')
            # print(text)
            # print(price)
            # print(ratings)
            # print(discount)
            # print('\n')
            yield{'text': text, 'price': price, 'ratings': ratings, 'discount': discount}
