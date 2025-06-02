{
    'name': 'Product Manager',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'Quản lý sản phẩm',
    'description': """
        Module quản lý sản phẩm với các tính năng:
        * Quản lý thông tin sản phẩm
        * Tìm kiếm và lọc sản phẩm
        * Phân loại sản phẩm theo danh mục
        * Quản lý nhà cung cấp
    """,
    'author': 'Your Name',
    'website': 'https://www.example.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'views/menu_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
} 