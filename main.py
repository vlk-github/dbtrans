# encoding=utf-8
import os
import warnings
import pymysql.cursors
from googletrans import Translator as BaseTranslator
from googletrans import urls, utils
from googletrans.constants import DEFAULT_USER_AGENT, LANGUAGES, SPECIAL_CASES

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


class Translator(BaseTranslator):
    def __init__(self, service_urls=None, user_agent=DEFAULT_USER_AGENT):
        BaseTranslator.__init__(self, service_urls, user_agent)

    def translate(self, text, dest='en', src='auto'):
        if src != 'auto':
            if src not in LANGUAGES.keys() and src in SPECIAL_CASES.keys():
                src = SPECIAL_CASES[src]
            elif src not in LANGUAGES.keys():
                raise ValueError('invalid source language')

        if dest not in LANGUAGES.keys():
            if dest in SPECIAL_CASES.keys():
                dest = SPECIAL_CASES[dest]
            else:
                raise ValueError('invalid destination language')

        if isinstance(text, list):
            result = []
            for item in text:
                translated = self.translate(item, dest=dest, src=src)
                result.append(translated)
            return result

        if len(text) > 5000:
            result = ''
            origin = text
            while len(origin) > 0:
                result += self._translate(origin[:5000], dest, src)
                origin = origin[5000:]
            return result

        data = self._translate(text, dest, src)
        return data

    def _translate(self, text, dest='en', src='auto'):
        token = self.token_acquirer.do(text)
        params = utils.build_params(query=text, src=src, dest=dest,
                                    token=token)
        url = urls.TRANSLATE.format(host=self._pick_service_url())

        if len(text) < 200:
            response = self.session.get(url, params=params)
        else:
            data = {'q': params.pop('q')}
            query = '?'
            for key in params:
                value = params[key]
                if type(value) == list:
                    for item in value:
                        query += key + '=' + item + '&'
                elif type(value) != str:
                    query += key + '=' + str(value) + '&'
                else:
                    query += key + '=' + value + '&'
            response = self.session.post(url + query, data=data)

        result = utils.format_json(response.text)
        data = ''.join([d[0] if d[0] else '' for d in result[0]])
        return data


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
            file.write(str(self.last_id))
        pass

    def execute(self):
        result = list(sql_execute(self.select_tpl, [self.last_id]))
        if result:
            data = list(dict(result[0]).values())
            print('id:' + str(data[0]) + ' title:' + data[1])
            self.last_id = data.pop(0)
            translator = Translator()
            data = translator.translate(data, src=self.source, dest=self.target)
            data.append(self.last_id)
            flag = sql_execute(self.update_tpl, data)
            if flag > 0:
                self.save_last_id()
                self.execute()
            else:
                print('update error!')
        else:
            print('not found data!')
        pass

task = Task(**task_params)
task.execute()
database.close()
