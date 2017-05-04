import pymysql
from task import *


class Process(object):
    def __init__(self, config:dict):
        self.database = pymysql.connect(**config['database'])
        self.task = config['task']

    def create_task_table(self):
        try:
            with self.database.cursor() as cursor:
                cursor.execute(self.task.get_create_table_sql())
                self.database.commit()
        finally:
            self.database.close()
        pass

    """
    def build_export_sql(self):

        sql = 'SELECT %(fields)s FROM %(tables)s'
        sql += self.task_kwargs['primary_table_name'] + '.' + table_kwargs['primary_table_key']
        for field in table_kwargs['primary_table_fields']:
            sql += ', ' + table_kwargs['primary_table_name'] + '.' + field
        if 'attached_table_fields' in table_kwargs:
            for field in table_kwargs['attached_table_fields']:
                sql += ', ' + table_kwargs['attached_table_name'] + '.' + field
        sql += ' From ' + table_kwargs['primary_table_name']
        if 'attached_table_name' in table_kwargs:
            sql += ' INNER JOIN ' + table_kwargs['attached_table_name'] + ' ON '
            sql += table_kwargs['primary_table_name'] + '.' + table_kwargs['primary_table_key'] + ' = '
            sql += table_kwargs['attached_table_name'] + '.' + table_kwargs['attached_table_key']
        return sql
"""
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
