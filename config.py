# 数据库配置
DATABASES = {
    "bdp_spider": {
        "host": "127.0.0.1",
        "user": "root",
        "port": 3306,
        "passwd": "",
        "db": "bdp_spider"
    },
}

MAX_DB_CONNECTIONS = 10


# redis conf
CACHES = {
    "TestCaches": {
        "host": "127.0.0.1",
        "user": "root",
        "passwd": "",
        "port": 6379,
        "db": "10"
    }
}