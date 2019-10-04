from collections import defaultdict
from django.core.files.storage import Storage
try:
    from io import BytesIO
except:
    # Python 2
    from StringIO import StringIO as BytesIO


class MockStorage(Storage):
    stored = set()

    def __init__(self, prefix=''):
        self.prefix = prefix

    def exists(self, name):
        return self.prefix + name in self.stored

    def open(self, mode='rb'):
        return BytesIO()

    def save(self, name, content, max_length=None):
        self.stored.add(self.prefix + name)

