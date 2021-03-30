#config.py

import os
# import jwcrypto.jwk as jwk

class Config(object):
    # key = jwk.JWK.generate(kty='RSA', size=2048)
    # priv_pem = key.export_to_pem(private_key=True, password=None)
    # pub_pem = key.export_to_pem()
    # PRIV_KEY = jwk.JWK.from_pem(priv_pem)
    # PUB_KEY = jwk.JWK.from_pem(pub_pem)
    # DEBUG = False
    # TESTING = False
    # CSRF_ENABLED = True
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SECRET_KEY = os.environ['SECRET_KEY']
    # SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
    # S3_BUCKET = os.environ['S3_BUCKET']
    # S3_KEY = os.environ['S3_KEY']
    # S3_LOCATION = os.environ['S3_LOCATION']
    # S3_SECRET = os.environ['S3_SECRET']
    # STRIPE_SECRET  = os.environ['STRIPE_SECRET']
    # TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
    # TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
    # WEBHOOK_SECRET = os.environ['WEBHOOK_SECRET']
    # STRIPE_PRODUCT = os.environ['STRIPE_PRODUCT']
    # SENDER_PHONE = os.environ['SENDER_PHONE']
    # FRONTEND_ORIGIN = os.environ['FRONTEND_ORIGIN']
    # USER_VERIF_EXP_HOURS = 24
    SUPPORT_MAIL = "aicare@jiit.mx"
    # FRONTEND_TEST = os.environ['FRONTEND_TEST']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
