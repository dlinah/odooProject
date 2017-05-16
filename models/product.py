from odoo import models, fields

class Product(models.Model):
	_name='souq.product'
	link=fields.Char()
	name=fields.Char()
	price=fields.float()
	description=fields.Char()
	image=fields.Binary()
	condition=fields.Char()
	seller=fields.Char()