# -*- coding: utf-8 -*-

#################################
# 默认变量
#################################

# 登录账号密码
BASIC_AUTH_USERNAME = "admin"
BASIC_AUTH_PASSWORD = '123456'


# redis
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0

# BASIC_AUTH_JWT_KEY = secret_util.get_random_secret()

# token过期时间，单位天
BASIC_AUTH_EXPIRES = 7

# scrapyd地址, 结尾不要加斜杆
# SCRAPYD_SERVER = "http://127.0.0.1:6800"

# 数据存储文件夹
DATABASE_DIR = "database"

# 调度器 调度历史存储设置
# mysql or sqlite and other, any database for peewee support
# doc: http://docs.peewee-orm.com/en/latest/peewee/playhouse.html#database-url
SCHEDULE_HISTORY_DATABASE_URL = "sqlite:///{database_dir}/schedule_history.db".format(
    database_dir=DATABASE_DIR
)
# pip install pymysql
# SCHEDULE_HISTORY_DATABASE_URL = 'mysql://root:123456@127.0.0.1:3306/spider_admin'

# 调度器 定时任务存储地址 基于 SQLAlchemy
# doc: https://docs.sqlalchemy.org/en/13/core/engines.html#database-urls
JOB_STORES_DATABASE_URL = "sqlite:///{database_dir}/apscheduler.db".format(
    database_dir=DATABASE_DIR
)
# JOB_STORES_DATABASE_URL = 'mysql+pymysql://root:123456@127.0.0.1:3306/spider_admin'

# 日志文件夹
LOG_DIR = "logs"

DEFAULT_CACHE_DIR = "cache"

COMPRESS_STATIC = True
