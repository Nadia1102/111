import os

def get_filename(db_name, table_name = None):
    path = os.path.join(os.getcwd(), 'data', db_name)
    if table_name:
        path = os.path.join(path, table_name)
    return os.path.join(path, "_info.json")
