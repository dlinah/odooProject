from odoo import models, fields, api
from scraper import SouqScrapper
import base64
import urllib2


class Product(models.Model):
    def load_image(self, image_url):
        print 'ckdmkemdkmdkemdk --------------'
        image = base64.decodestring(urllib2.urlopen(image_url).read())
        print image
        self.image = image
        print 'inchange'

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
        print(self.image)

    def update_all_products(self):
        records = self.env['souq.product'].search([])
        for record in records:
            print ("id :", record.id)
            obj = self.env['souq.product'].browse([record.id])
            scraper = SouqScrapper(obj.link)
            name = scraper.name()
            price = scraper.price()
            description = scraper.description()
            image_url = scraper.image_url()
            res = obj.write({"name": name, "description": description, "price": price, 'image_url': image_url})
