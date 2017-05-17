from odoo import models, fields ,api
from scraper import souqScrapper
import base64
import urllib2 

class Product(models.Model):

	@api.onchange('image_url')
	def _load_image(self):
		print 'ckdmkemdkmdkemdk --------------'
		link=self.image_url
		image = base64.encodestring(urllib2.urlopen(link).read())
		print imag
		self.image=image
		print 'inchange'



	_name='souq.product'
	link=fields.Char()
	name=fields.Char()
	price=fields.Char()
	description=fields.Char()
	image=fields.Binary()
	condition=fields.Char()
	seller=fields.Char()
	image_url=fields.Char()

	def update_product(self):
		scraper = souqScrapper(self.link)
		self.name= scraper.name()
		self.price= scraper.price()
		self.description=scraper.description()
		self.image_url=scraper.image_url()

	def update_all_products(self):
		records = self.env['souq.product'].search([])
		for record in records:
			print ("id :", record.id)
			obj = self.env['souq.product'].browse([record.id])
			scrapper = souqScrapper(obj.link)
			name= scraper.name()
			price= scraper.price()
			description=scraper.description()
			image_url=scraper.image_url()
			res = obj.write({"name": name, "description": description, "price": price,'image_url':image_url})
       
	
    
