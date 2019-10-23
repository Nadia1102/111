

class TinyDB:
    _databases = []
    _db_registry = {}

    def __self__(self):
        _databases = json.load('databases.info')

    def get_database_names(self):
        return self._databases

    def get_database(self, db_name):
        self._load_database(db_name)
        return self._db_registry[db_name]

    def _load_database(self, db_name):
        pass # TODO

