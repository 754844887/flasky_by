import redis
from datetime import timedelta

# 数据库配置
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Huawei@123@192.168.234.128:3306/flask_by?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# session 缓存配置
SESSION_TYPE = 'redis'
SESSION_COOKIE_NAME = 'flask_session'
#SESSION_COOKIE_DOMAIN = ''
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = False
PERMANENT_SESSION_LIFETIME = timedelta(days=7)
SESSION_PERMANENT = False
SESSION_USE_SIGNER = False
SESSION_KEY_PREFIX = 'session'
SESSION_REDIS = redis.Redis(host='127.0.0.1', port=6379)

# 表单secret_key
SECRET_KEY = 'QAZwsx@!@#'