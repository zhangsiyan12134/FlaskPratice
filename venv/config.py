import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '9d49a3fd9cb2c7526db9d3df6d2931321b1ffb210bb1e79940b6f48e9acf615c275ded5bd7b5c3cbd66684e21a0651cef9e942f4103f979e7ed67d7e4c0f891d'
