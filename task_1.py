from process import *

config = {
    'task_id': 'news_task',
    'database': {
        'host': 'localhost',
        'user': 'root',
        'passwd': '111111',
        'database': 'test'
    },
    'tables': {
        'primary_table_name': 'test_1',
        'primary_table_key': 'id',
        'primary_table_fields': ['title', 'summary'],
        'attached_table_name': 'test_2',
        'attached_table_key': 'id',
        'attached_table_fields': ['content']
    }
}

process = Process(config)
process.create_task_table()
process.start()
