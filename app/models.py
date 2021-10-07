from app import db
from flask_security import UserMixin, RoleMixin


roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(500), nullable=True)
    active = db.Column(db.Boolean)
    orders = db.relationship('Order', backref='user', lazy=True)
    addresses = db.relationship('Address', backref='user', lazy=True)
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return f'<User {self.id}>'


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(255))


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    color = db.Column(db.String(30))
    weight = db.Column(db.Float)
    price = db.Column(db.Float(asdecimal=True, decimal_return_scale=2))

    def __repr__(self):
        return f'<Product {self.name}>'


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(50))
    zip_code = db.Column(db.String(15))
    city = db.Column(db.String(50))
    street = db.Column(db.String(100))
    house_number = db.Column(db.String(10))
    apartment_number = db.Column(db.String(10))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    orders = db.relationship('Order', backref='address', lazy=True)

    def __repr__(self):
        return f'<Address {self.id}>'


orders_products = db.Table(
    'orders_products',
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True),
    db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True)
)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))
    products = db.relationship('Product', secondary=orders_products, lazy='subquery', backref=db.backref('orders', lazy=True))
