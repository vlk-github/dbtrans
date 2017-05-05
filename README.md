# dbtrans
Use the Google translate API to translate tables in the mysql

depend
--------

    $ pip install pymysql
    $ pip install requests
    $ pip install googletrans
    
configuration
--------

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
