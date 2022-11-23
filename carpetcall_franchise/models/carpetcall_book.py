from odoo import fields, models, api
from odoo.exceptions import ValidationError


# class Record(models.Model):
#     # _name = 'record.public'
#     _name = 'record.shareable'
#     _check_company_auto = True
#     _description = "mutil_company"
#
#     company_id = fields.Many2one('res.company')
#     other_record_id = fields.Many2one('other.record', check_company=True)
#
#     info = fields.Text()
#     company_info = fields.Text(company_dependent=True)
#     display_info = fields.Text(string='Infos', compute='_compute_display_info')
#
#     @api.depends_context('company')
#     def _compute_display_info(self):
#         for record in self:
#             record.display_info = record.info + record.company_info


# class Record(models.Model):
#     _name = 'record.restricted'
#     _check_company_auto = True
#
#     company_id = fields.Many2one('res.company', required=True, default=lambda self: self.env.company)
#
#     other_record_id = fields.Many2one('other.record', check_company=True)


# class Record(models.Model):
#     _name = 'record.shareable'
#     _check_company_auto = True
#
#     company_id = fields.Many2one('res.company')
#     other_record_id = fields.Many2one('other.record', check_company=True)




# class Record(models.Model):
#     _name = 'record.restricted'
#     _check_company_auto = True
#
#     company_id = fields.Many2one('res.company', required=True, default=lambda self: self.env.company)
#     other_record_id = fields.Many2one('other.record', check_company=True)
#


# class CompanyDetail(models.Model):
#     _name = 'company.detail'
#     _check_company_auto = True
#     _description = "Company_details"
#



class Book(models.Model):
    """
    Describes a Book catalogue.
    """
    _name = "carpetcall.book"
    _description = "Book"
    _check_company_auto = True
    # _check_company_auto = False


    name = fields.Char("Title", required=True)
    company_id = fields.Many2one('res.company', 'Company', required=True, default=lambda self: self.env.company, readonly=True)
    user_id = fields.Many2one('res.users', string='Technician', check_company=True)
    company_details = fields.Text(string="Company Details", company_dependent=True)

    @api.onchange('company_details')
    def _onchange_company_details(self):
        self = self.with_company(self.company_id)


    @api.onchange('company_id')
    def _onchange_company_id(self):
        for rec in self:
            rec.company_details = 'self.env.user.company_id'
            # rec.company_details = 'testest'
            # rec.comment = "DDDD Changeer the company_id information!!!"


    # context['allowed_company_ids'][1])
    # company_id_s = fields.Char("Company_id_now")
    # company_id_s = lambda self: self.env.user
    # get_companyid = lambda self: self.env['res.company'].browse(self.env['res.company']._company_default_get('carpetcall_franchise'))

                                #lambda self: self.env.user.company_id )

                                 #default=lambda self: self.env['res.company'].browse(self.env['res.company']._company_default_get('carpetcall_franchise')))

                                 #domain=['&&', ('company_id', 'in', 'company_ids'), ('company_id', '=', True)] )

                                 #domain=[('company_id', 'in', 'company_ids')])

                                 #default=lambda self: self.env.user.company_id)

    #### default=lambda self: self.env['res.company'].browse(self.env['res.company']._company_default_get('your.module')))  #default=lambda self: self.env.user.company_id)#

    range = fields.Char("Range")
    sku = fields.Char("Sku", readonly=True)
    fibre = fields.Char("Fibre") #, states={'readonly': True, 'invisible': False})
    colour = fields.Char("Colour")
    stock = fields.Char("Stock_code", readonly=True) #, domain="[('stock', '=', 'self.env.user.company_id')]")
                                                            #lambda self: self.env['res.company'].browse(self.env['res.company']._company_default_get('carpetcall_franchise'))')]" )
    roll_type = fields.Char("Roll Type", readonly=True)
    retail_price = fields.Float('Retail Price', digits=(12, 2), readonly=True)
    roll_price = fields.Float('Roll Price', digits=(12, 2), readonly=True)
    floor_cost = fields.Float('Floor Cost', digits=(12, 2), groups="carpetcall_franchise.carpetcall_group_manager")
    roll_qty = fields.Float('Roll Quantity', digits=(12, 2), readonly=True)
    order_qty = fields.Float('Order Quantity', digits=(12, 2), groups="carpetcall_franchise.carpetcall_group_manager")
    free_qty = fields.Float('Free qty', digits=(12, 2), groups="carpetcall_franchise.carpetcall_group_manager")

    parking_zone = fields.Selection([('a', 'AB'), ('b', 'BC'), ('c', 'CD')], string="Test_selection", copy='False', default='a')
    two_wheels = fields.Integer(string='Motor')
    four_wheels = fields.Integer(string='Mobile Umum')

    @api.onchange('parking_zone')
    def harge(self):
        for rec in self:
            if rec.parking_zone == 'a':
                rec.two_wheels = 2000
                rec.four_wheels = False
                rec.comment = "AAAA information!"
            elif rec.parking_zone == 'b':
                rec.two_wheels = False
                rec.four_wheels = 3000
                rec.comment = "BBBBB infomation!!!"
            elif rec.parking_zone == 'c':
                rec.two_wheels = 1000
                rec.four_wheels = 2600
                rec.comment = "CCCCC information!!!"

    comment = fields.Text("Comment", default="This is the commment to edit fields.")

    # parterid = fields.many2one('res.partner', 'Customer', readonly=True,
    #                 states={'draft': [('readonly', False)], 'sent': [('readonly', False)],
    #                         'test': [('readonly', False)]}, required=True, change_default=True, select=True,
    #                 track_visibility='always')



    isbn = fields.Char(string="Status_Code")



    active = fields.Boolean("Active?", default=True)
    date_published = fields.Date(string="Date Provided")
    image = fields.Binary("Cover")
    publisher_id = fields.Many2one("res.partner", string="Supplier")
    # build_id = fields.Many2one("public.builder", string="Builder")
    build_id = fields.Many2one("carpetcall.builder", string="Builder")
    builder_name = fields.Char(string="Build_Name", related="build_id.name")
    builder_phone = fields.Char(string="Build_Phone", related="build_id.mobie")
    builder_address = fields.Char(string="Build_address", related="build_id.address")
    # function_info = fields.Many2one("res.partner", string="NameFunction", domain=[('id', '=', 'publisher_id')])
    # function_info = fields.Many2one("res.partner.function", string="NameFun")
    function_info = fields.Char(string='Supplier_Info', related="publisher_id.function") #, domain=[('id', '=', 'publisher_id')])
    address_info = fields.Char(string="The Supplier Address", related="publisher_id.street")
    tel_info = fields.Char(string="The Supplier phone", related="publisher_id.phone")
    author_ids = fields.Many2many(comodel_name="res.partner", string="Contact")

    def _check_isbn(self):
        self.ensure_one()
        digits = [int(x) for x in self.isbn if x.isdigit()]
        if len(digits) == 13:
            ponderations = [1, 3] * 6
            terms = [a * b for a, b in zip(digits[:12], ponderations)]
            remain = sum(terms) % 10
            check = 10 - remain if remain != 0 else 0
            return digits[-1] == check

    def button_check_isbn(self):
        # print(self.env)
        for book in self:
            if not book.isbn:
                raise ValidationError("Please provide an ISBN for %s" % book.name)
            if book.isbn and not book._check_isbn():
                raise ValidationError("%s ISBN is invalid" % book.isbn)
        return True