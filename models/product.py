from odoo import models, fields ,api
from scraper import souqScrapper
import base64
import urllib2 

class Product(models.Model):

	@api.depends('image_url')
	def _load_image(self,cr,uid,ids,args,fields,context=None):
		link=self.image_url
		self.image = base64.encodestring(urllib2.urlopen(link).read())

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

	
    
