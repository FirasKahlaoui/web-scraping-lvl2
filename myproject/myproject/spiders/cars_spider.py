import scrapy
from myproject.items import CarItem


class CarsSpider(scrapy.Spider):
    name = "cars"
    start_urls = [
        "https://www.cars.com/new-cars/?type=electric-vehicle",
        "https://www.cars.com/new-cars/?type=suv",
        "https://www.cars.com/new-cars/?type=sedan",
        "https://www.cars.com/new-cars/?type=pickup-truck",
        "https://www.cars.com/new-cars/?type=coupe",
        "https://www.cars.com/new-cars/?type=hatchback",
        "https://www.cars.com/new-cars/?type=wagon",
        "https://www.cars.com/new-cars/?type=convertible",
        "https://www.cars.com/new-cars/?type=van"
    ]

    def parse(self, response):
        vehicle_type = response.url.split('=')[-1].replace('-', ' ').title()

        self.log(f'Parsing {vehicle_type} page')

        for car in response.css('div.horizontal-model-year-card'):
            image = car.css(
                'div.horizontal-model-year-card-image img::attr(src)').get()
            name = car.css(
                'div.horizontal-model-year-card-details-compare a::text').get()
            start_price = car.css(
                'div.horizontal-model-year-card-details-compare::text').re_first(r'\$(\d+,\d+)')

            self.log(
                f'Found car: {name} with price {start_price} and image {image}')

            yield CarItem(
                image=image,
                name=name,
                start_price=start_price,
                type=vehicle_type
            )

        next_page = response.css(
            'a.shop-srp-listings__vehicle-card-link::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
