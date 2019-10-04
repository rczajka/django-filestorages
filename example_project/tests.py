from django.conf import settings
from django.core.files.base import ContentFile
from django.test import TestCase, override_settings
from core.storage import MockStorage
from filestorages import get_storage


class StorageTests(TestCase):
    @override_settings(
        DEFAULT_FILE_STORAGE='core.storage.MockStorage'
    )
    def test_no_config(self):
        del settings.FILE_STORAGES
        get_storage('undefined').save('noconfig', ContentFile('x'))
        self.assertIn('noconfig', MockStorage.stored)

    @override_settings(
        FILE_STORAGES={},
        DEFAULT_FILE_STORAGE='core.storage.MockStorage'
    )
    def test_empty_config(self):
        get_storage('undefined').save('emptyconfig', ContentFile('x'))
        self.assertIn('emptyconfig', MockStorage.stored)

    @override_settings(FILE_STORAGES={
        'some': {'BACKEND': 'core.storage.MockStorage', 'OPTIONS': {'prefix': 'some:'}},
        'some.defined': {'OPTIONS': {}},
        'some.defined.storage': {'OPTIONS': {'prefix': 'storage:'}},
    })
    def test_config(self):
        get_storage('some.defined.storage').save('test', ContentFile('x'))
        self.assertIn('storage:test', MockStorage.stored)
