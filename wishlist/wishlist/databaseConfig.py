from _typeshed import Self


class DB(Self):
    self.testingDB = {   
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        }