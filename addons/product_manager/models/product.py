from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProductManager(models.Model):
    _name = 'product.manager'
    _description = 'Quản lý sản phẩm'
    _order = 'name'

    name = fields.Char('Tên sản phẩm', required=True, index=True)
    code = fields.Char('Mã sản phẩm', required=True, index=True)
    description = fields.Text('Mô tả')
    price = fields.Float('Giá bán', required=True)
    quantity = fields.Integer('Số lượng', default=0)
    category = fields.Char('Danh mục')
    supplier = fields.Char('Nhà cung cấp')
    active = fields.Boolean('Hoạt động', default=True)
    date_created = fields.Datetime('Ngày tạo', default=fields.Datetime.now)
    last_updated = fields.Datetime('Cập nhật lần cuối', default=fields.Datetime.now)

    @api.constrains('price', 'quantity')
    def _check_values(self):
        for record in self:
            if record.price < 0:
                raise ValidationError('Giá bán không được âm!')
            if record.quantity < 0:
                raise ValidationError('Số lượng không được âm!')

    @api.model
    def create(self, vals):
        vals['last_updated'] = fields.Datetime.now()
        return super(ProductManager, self).create(vals)

    def write(self, vals):
        vals['last_updated'] = fields.Datetime.now()
        return super(ProductManager, self).write(vals) 