# django-filestorages

Django-getstorage is a tiny Python library for dealing with configurable
Django storages.

It allows you to define a dictionary of file storage configurations
in your `settings` and refer to them by name in your code.

It should be obsolete once [Django ticket 26029](https://code.djangoproject.com/ticket/26029).
is resolved.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install django-filestorages.

```bash
pip install django-filestorages
```


## Usage

Wherever you need a storage, use a 

```python
from getstorage import get_storage

file = models.FileField(storage=get_storage('some.configured.storage'))
```


## License
[MIT](https://choosealicense.com/licenses/mit/)
