from odoo import models, fields, api
from scraper import SouqScrapper
import base64
import urllib2


class Product(models.Model):
    def load_image(self, image_url):
        image = base64.decodestring(urllib2.urlopen(image_url).read())
        self.image = image

    _name = 'souq.product'
    link = fields.Char()
    name = fields.Char()
    price = fields.Char()
    description = fields.Char()
    image = fields.Binary()
    condition = fields.Char()
    seller = fields.Char()

    def update_product(self):
        scraper = SouqScrapper(self.link)
        self.name = scraper.name()
        self.price = scraper.price()
        self.description = scraper.description()
        image_url = scraper.image_url()
        self.load_image(image_url)

    def update_all_products(self):
        records = self.env['souq.product'].search([])
        for record in records:
            obj = self.env['souq.product'].browse([record.id])
            scraper = SouqScrapper(obj.link)
            name = scraper.name()
            price = scraper.price()
            description = scraper.description()
            image_url = scraper.image_url()
            self.load_image(image_url)
            obj.write({"name": name, "description": description, "price": price})
