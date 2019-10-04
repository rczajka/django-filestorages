import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'test-secret-key'

INSTALLED_APPS = [
    'app',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


FILE_STORAGES = {
    'default': {
        'BACKEND': 'core.storage.MockStorage',
    },
    'some.defined': {
        'OPTIONS': {
            'prefix': 'example:'
        }
    },
}
