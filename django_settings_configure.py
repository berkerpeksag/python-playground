from django.conf import settings
from django.test import TestCase

TEST_DATABASE_NAME = 'test_db'

TEST_SETTINGS = {
    'DATABASES': {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': TEST_DATABASE_NAME,
        },
    },
}

if not settings.configured:
    settings.configure(**TEST_SETTINGS)


class TestSpam(TestCase):
    pass
