from peewee import *


def content_database(params: dict):
    params.setdefault('charset', None)
    params.setdefault('port', None)
    database = MySQLDatabase(host=params['host'], user=params['user'],
                             passwd=params['passwd'], database=params['database'],
                             charset=params['charset'], port=params['port'])
    database.connect()
    return database


class Task(object):
    def __init__(self, config: dict):
        self.database = None
        self.content_database(config['database'])
        self.build_related_sql(config['tables'])

    def content_database(self, params: dict):
        params.setdefault('charset', None)
        params.setdefault('port', None)
        self.database = MySQLDatabase(host=params['host'], user=params['user'],
                                      passwd=params['passwd'], database=params['database'],
                                      charset=params['charset'], port=params['port'])
        self.database.connect()
        self.database.create_table()

    def build_related_sql(self, tables: dict):
        tables.setdefault('attached_table_name', None)
        tables.setdefault('attached_table_key', None)
        tables.setdefault('attached_table_fields', None)
        sql = 'SELECT '
        sql += tables['primary_table_name'] + '.' + tables['primary_table_key']
        for field in tables['primary_table_fields']:
            sql += ', ' + tables['primary_table_name'] + '.' + field
        if tables['attached_table_fields'] is not None:
            for field in tables['attached_table_fields']:
                sql += ', ' + tables['attached_table_name'] + '.' + field
        sql += ' From ' + tables['primary_table_name']
        if tables['attached_table_name'] is not None:
            sql += ' INNER JOIN ' + tables['attached_table_name'] + ' ON '
            sql += tables['primary_table_name'] + '.' + tables['primary_table_key'] + ' = '
            sql += tables['attached_table_name'] + '.' + tables['attached_table_key']


        #* from test_1 inner join test_2 on test_1.id = test_2.id'
        print(sql)
        return

    def start(self):
        return

    def stop(self):
        return

    def _import(self):
        return self.database

    def _execute(self):
        return self.database

    def _export(self):
        return self.database
