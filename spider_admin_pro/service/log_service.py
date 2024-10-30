
# 导入redis
import datetime
from spider_admin_pro.utils.redis_util import RedisConnectionManager


service = RedisConnectionManager.get_connection()


def get_log_key(data):
   
    # 寻找所有类似key的键，并返回列表 task_log:2024-10-30:*
    data = datetime.datetime.now().strftime("%Y-%m-%d")

    # 构建键的模式
    pattern = f'task_log:{data}:*'

    # 使用 SCAN 命令查找所有匹配的键
    cursor = '0'
    keys = []
    while cursor != 0:
        cursor, keys_batch = service.scan(cursor=cursor, match=pattern, count=100)
        keys.extend(keys_batch)

    


    # 将字节字符串转换为普通字符串
    keys = [key.decode('utf-8') for key in keys]
