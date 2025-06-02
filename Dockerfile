FROM odoo:18.0

# Cài đặt các dependency nếu có
USER root
RUN pip3 install --upgrade pip

# Copy custom modules vào thư mục addons
COPY . /mnt/extra-addons/

# Chỉnh quyền
RUN chown -R odoo:odoo /mnt/extra-addons

# Trở lại user odoo
USER odoo

# Chạy Odoo với đường dẫn addons bổ sung
CMD ["odoo", "-d", "odoo_test_db", "--addons-path=/mnt/extra-addons,/usr/lib/python3/dist-packages/odoo/addons", "--dev=all"]

