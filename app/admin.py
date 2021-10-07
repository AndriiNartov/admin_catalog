from flask import redirect, flash, url_for
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_security import current_user

from app import app, db
from app.models import User, Product, Address


class AdminMixin:

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        flash('Please, log in to enter the Admin page!', category='info')
        return redirect(url_for('security.login'))


class AdminView(AdminMixin, ModelView):
    pass


class HomeAdminView(AdminMixin, AdminIndexView):

    @expose('/')
    def index(self):
        return self.render('admin/index.html')


class AddressAdminView(AdminMixin, ModelView):
    form_columns = ['country', 'zip_code', 'city', 'street', 'house_number', 'apartment_number']
    column_list = ['country', 'zip_code', 'city', 'street', 'house_number', 'apartment_number']
    column_filters = ['country', 'zip_code', 'city', 'street']


class UserAdminView(AdminMixin, ModelView):
    form_columns = ['email', 'active', 'password']
    column_list = ['email', 'active']


admin = Admin(app, 'Catalog', index_view=HomeAdminView(), template_mode='bootstrap4')

admin.add_view(UserAdminView(User, db.session))
admin.add_view(AdminView(Product, db.session))
admin.add_view(AddressAdminView(Address, db.session))
