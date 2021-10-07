class Configuration:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../app_db.db'
    SECRET_KEY = 'secret'  # you should use more complex secret key in production
    SECURITY_PASSWORD_SALT = 'salt'  # you should use more complex salt in production
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
    SECURITY_POST_LOGOUT_VIEW = '/login'
    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_POST_LOGIN_VIEW = '/admin'
    SECURITY_POST_REGISTER_VIEW = '/login'
    SECURITY_BACKWARDS_COMPAT_UNAUTHN = True
