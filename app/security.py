import sqlalchemy
from flask_security import SQLAlchemyUserDatastore, Security

from app import app, db
from app.models import User, Role


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


@app.before_first_request
def create_admin():
    tables_list = sqlalchemy.inspect(db.get_engine(app)).get_table_names()
    if not tables_list:
        db.create_all()
    if not user_datastore.find_user(email="admin@example.com"):
        user_datastore.create_user(email="admin@example.com", password="admin")
    db.session.commit()
