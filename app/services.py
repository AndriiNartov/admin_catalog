from app import db

from app.models import Product, Address, User


class DatabasePrefillMessageAndCategory:
    MESSAGE_SUCCESS = "Database is successfully prefilled!"
    MESSAGE_FAIL = 'Oops, something went wrong! Try again or fill the database manually!'
    CATEGORY_SUCCESS = 'success'
    CATEGORY_FAIL = 'danger'


prefill_datastore = {
    Product: {
          'name': ['Iphone 12 Red', 'Iphone 12 Blue', 'Iphone 13 Mini', 'Iphone 12 Yellow', 'Iphone 12 Gold'],
          'color': ['Red', 'Blue', 'Black', 'Yellow', 'Gold'],
          'weight': [120.0, 125.0, 100.0, 130.0, 115.0],
          'price': [1199.0, 2125.0, 1000.0, 1300.0, 1150.0]
    },
    Address: {
          'country': ['Ukraine', 'Ukraine', 'Germany', 'Netherlands', 'Belgium'],
          'zip_code': ['01001', '59000', '10243', '1017 XA', '1000'],
          'city': ['Kyiv', 'Dnipro', 'Berlin', 'Amsterdam', 'Brussel'],
          'street': ['vul.Shevhchenko', 'vul.Vernadskogo', 'Bergerweg', 'Canalstraat', 'Rue de Loxum'],
          'house_number': ['10', '21', '10/5', '130', '52'],
          'apartment_number': ['100', '', '30', '255', '3']
    }
}


def auto_fill_in_database():
    try:
        print(DatabasePrefillMessageAndCategory.MESSAGE_SUCCESS)
        for model in prefill_datastore:
            for index in range(5):
                new_instance = model()
                for key in prefill_datastore[model]:
                    new_instance.__setattr__(key, prefill_datastore[model][key][index])
                    if hasattr(model, 'user'):
                        new_instance.user = User.query.first()
                db.session.add(new_instance)
        db.session.commit()
        return DatabasePrefillMessageAndCategory.MESSAGE_SUCCESS, DatabasePrefillMessageAndCategory.CATEGORY_SUCCESS
    except:
        db.session.rollback()
        return DatabasePrefillMessageAndCategory.MESSAGE_FAIL, DatabasePrefillMessageAndCategory.CATEGORY_FAIL
