from django.db import models
from filestorages import get_storage


class AModel(models.Model):
    file = models.FileField(storage=get_storage('some.defined.storage'))

