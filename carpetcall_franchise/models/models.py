# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class carpetcall_franchise(models.Model):
#     _name = 'carpetcall_franchise.carpetcall_franchise'
#     _description = 'carpetcall_franchise.carpetcall_franchise'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
