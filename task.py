class Task(object):
    def __init__(self, **config):
        self.name = config['name']
        pass

    def get_create_table_sql(self):
        sql = """
                CREATE TABLE IF NOT EXISTS `%s` (
                `id` int(11) NOT NULL,
                `status` tinyint(4) NOT NULL,
                PRIMARY KEY (`id`)
                ) ENGINE=MyISAM DEFAULT CHARSET=utf8;
            """
        return sql % self.name