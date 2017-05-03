from process import *

config = {
    'database': {
        'host': 'localhost',
        'user': 'root',
        'passwd': '111111',
        'database': 'test'
    },
    'task': {
        'name': 'news_task',
        'table': 'test_1',
        'fields': ['title', 'summary'],
        'primary_key': 'id',
        'attached': {
            'table': 'test_2',
            'fields': ['content'],
            'relation_key': 'id',
        }
    }
}

process = Process(config)
process.start()

