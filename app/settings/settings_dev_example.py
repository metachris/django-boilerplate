# Django settings for development
DEBUG = True
TEMPLATE_DEBUG = DEBUG
IS_TESTENV = True

ADMINS = (
    # ('Your Name', 'name@example.com'),
    )

MANAGERS = ADMINS

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'MAKE_THIS_UNIQUE'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<DB_NAME>',
        'USER': '<DB_USER>',
        'PASSWORD': '<DB_PASS>',
        'HOST': '<DB_IP>',
        'PORT': '<DB_PORT>',
        }
}

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '192.168.1.11:6379',
        "KEY_PREFIX": 'sportlog_',
        'OPTIONS': {
            'DB': 1,
            'PASSWORD': 'yadayada',
            'PARSER_CLASS': 'redis.connection.HiredisParser'
        },
        },
    }
