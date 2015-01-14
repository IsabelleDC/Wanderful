DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'wanderful',
    }
}

LOGIN_URL = 'login'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'isabellrey@gmail.com'
EMAIL_HOST_PASSWORD = 'wai2013GM'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'isabellrey@gmail.com'