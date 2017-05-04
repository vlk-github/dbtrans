# encoding=utf-8
import os
import warnings
import pymysql.cursors
from translator import *

connect_params = {
    'host': 'localhost',
    'user': 'root',
    'passwd': '111111',
    'database': 'test',
    'charset': 'utf8'
}

task_params = {
    'name': 'news',
    'source': 'zh-CN',
    'target': 'ja',
    'table': 'test_1',
    'fields': ['title', 'summary'],
    'primary_key': 'id',
    'attached': {
        'table': 'test_2',
        'fields': ['content'],
        'relation_key': 'id',
    }
}

warnings.filterwarnings('ignore')
database = pymysql.connect(**connect_params)
database.autocommit(True)


def sql_execute(query, args=None):
    with database.cursor(pymysql.cursors.DictCursor) as cursor:  # type: pymysql.cursors.Cursor
        result = cursor.execute(query, args)
        if query.startswith('SELECT'):
            result = cursor.fetchall()
    return result


class Task(object):
    def __init__(self, **config):
        config.setdefault('attached', None)
        self.name = config['name']
        self.source = config['source']
        self.target = config['target']
        self.table = config['table']
        self.fields = config['fields']
        self.attached = config['attached'] if 'attached' in config else None
        self.primary_key = self.add_field_prefix(config['primary_key'])
        self.select_tpl = 'SELECT ' + self.splice_fields() + ' FROM ' + self.splice_tables()
        self.select_tpl += ' WHERE ' + self.primary_key + ' > %s ORDER BY ' + self.primary_key + ' LIMIT 1'
        self.update_tpl = 'UPDATE ' + self.splice_tables() + ' SET ' + self.splice_fields(True)
        self.update_tpl += ' WHERE ' + self.primary_key + ' = %s'
        self.last_id = self.load_last_id()

    def splice_fields(self, updated=False):
        fields = []
        for field in self.fields:
            fields.append(self.add_field_prefix(field))
        if self.attached is not None:
            for field in self.attached['fields']:
                fields.append(self.add_field_prefix(field, True))
        if not updated:
            fields.insert(0, self.primary_key)
            fields = ', '.join(fields)
        else:
            fields = '=%s, '.join(fields) + '=%s'
        return fields

    def splice_tables(self):
        tables = self.table
        if self.attached is not None:
            tables += ' INNER JOIN %s ON %s = %s' % (self.attached['table'], self.primary_key,
                                                     self.add_field_prefix(self.attached['relation_key'], True))
        return tables

    def add_field_prefix(self, field, attached=False):
        prefix = self.table if not attached else self.attached['table']
        return '%s.%s' % (prefix, field)

    def load_last_id(self):
        last_id = 0
        if os.path.exists(self.name):
            with open(self.name, 'r') as file:
                last_id = int(file.read())
        return last_id

    def save_last_id(self):
        with open(self.name, 'w') as file:
            file.write(self.last_id)
        pass

    def execute(self):
        result = sql_execute(self.select_tpl, [self.last_id])
        if result:
            data = list(result[0].values())
            self.last_id = data.pop(0)
            trans = Translalor()
            translations = trans.translate(data, src=self.source, dest=self.target)
            for translation in translations:
                print(translation)
            data.append(self.last_id)
            #aa = sql_execute(self.update_tpl, data)
            #print(data)


task = Task(**task_params)
task.execute()
database.close()
