# encoding=utf-8
import os
import warnings
import pymysql.cursors
from googletrans import Translator

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
            translator = Translator()
            aa = """
<div class="text" id="text" style="font-size: 14px;">
                        <p style="font-size: 14px;">　　中新社华盛顿5月1日电 <a href="http://country.huanqiu.com/america" class="linkAbout" target="_blank" title="美国">美国</a>总统特朗普5月1日接受美国媒体采访时表示，如果情况允许，他愿意与<a href="http://country.huanqiu.com/north_korea" class="linkAbout" target="_blank" title="朝鲜">朝鲜</a>最高领导人金正恩举行会面。</p>
<p style="font-size: 14px;">　　特朗普当天在白宫椭圆办公室接受彭博社专访时做出上述表态。特朗普说，“如果与他(金正恩)会面是一件可行之事，我肯定会这么做，并且会感到荣幸，但前提是情况要允许。”他说，“大多数政治人物不会明确表态愿意与金正恩会面，但我愿意。”</p>
<p style="font-size: 14px;">　　特朗普在采访中没有指明“情况允许”的具体含义。这一表态也成为当天白宫例行记者会上的热门话题。</p><div class="ad250x250 fLeft marRig10" id="adPp"><!-- Ad Survey 广告位代码  文章内页画中画08--><script type="text/javascript">AD_SURVEY_Add_AdPos("9263");</script></div>
<p style="font-size: 14px;">　　白宫发言人斯派塞1日表示，“情况允许”意味着很多事情，这首先需要朝鲜立即停止挑衅性行为。斯派塞说，朝鲜半岛局势持续紧张，朝鲜对美国以及地区盟友构成严重的潜在安全威胁。特朗普总统将始终把保护美国的国家安全作为首要目1234asas

                    </div>
            """

            #translations = translator.translate(aa)
            print(len(aa))
           # for translation in translations:
              #  print(translation)
            #data.append(self.last_id)
            #aa = sql_execute(self.update_tpl, data)
            #print(data)
        pass


task = Task(**task_params)
task.execute()
database.close()
