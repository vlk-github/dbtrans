from task import *


class Process(object):
    def __init__(self, config: dict):
        self.database = MySQLDatabase(**config['database'])
        self.database.field_overrides['text'] = 'TEXT'
        self.export_sql = self.build_export_sql(**config['tables'])


    def create_task_table(self):
        database_proxy.initialize(self.database)

        task = Task()
        task.create_table()
        print(task.table_exists())

        #task.create_table()
        #Task.Meta.database = self.database
        #self.database.create_table(Task)

        return

    def build_export_sql(self, **table_kwargs):
        sql = 'SELECT '
        sql += table_kwargs['primary_table_name'] + '.' + table_kwargs['primary_table_key']
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
