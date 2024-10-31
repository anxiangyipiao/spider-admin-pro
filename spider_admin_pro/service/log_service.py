
# 导入redis
import datetime
import json
from spider_admin_pro.utils.redis_util import RedisConnectionManager

task_redis_server = RedisConnectionManager.get_connection()
sorted_set_key = 'key_sorted_set'


class LogCollectionService(object):



    @classmethod
    def page_key(cls, page, PAGE_SIZE=10):

        start_index = (page - 1) * PAGE_SIZE
        end_index = start_index + PAGE_SIZE - 1

        # 从有序集合中获取分页的键
        keys = task_redis_server.zrevrange(sorted_set_key, start_index, end_index)

        return keys
    @classmethod
    def count_key(cls):
        # 获取有序集合的长度
        count = task_redis_server.zcard(sorted_set_key)
        return count
    
    @classmethod
    def get_data_by_key(cls,keys:list):
    
    # 从哈希表中获取数据
        datas = []
        for key in keys:
            
            data = task_redis_server.hgetall(key)
            # 将bytes转换为string类型
            # 转为字典
            str_data = {
                'name': data[b'name'].decode('utf-8'),
                'source': data[b'source'].decode('utf-8'),
                'site_name': data[b'site_name'].decode('utf-8'),
                'time': data[b'time'].decode('utf-8'),
                'today_all_request': int(data[b'today_all_request'].decode('utf-8')),
                'today_success_request': int(data[b'today_success_request'].decode('utf-8')),
                'today_fail_request': int(data[b'today_fail_request'].decode('utf-8')),
                'this_time_all_request': int(data[b'this_time_all_request'].decode('utf-8')),
                'this_time_success_request': int(data[b'this_time_success_request'].decode('utf-8')),
                'this_time_fail_request': int(data[b'this_time_fail_request'].decode('utf-8')),
                'last_time': data[b'last_time'].decode('utf-8'),
                'run_time': data[b'run_time'].decode('utf-8'),
                'crawl_count': int(data[b'crawl_count'].decode('utf-8')),
                'failed_urls':  json.loads(data[b'failed_urls'].decode('utf-8'))
            }

            datas.append(str_data)

        return datas
    

    def get_data(cls, page=1, PAGE_SIZE=10):
        # 获取分页的键
        keys = cls.page_key(page, PAGE_SIZE)
        # 获取数据
        datas = cls.get_data_by_key(keys)
        # 获取总数
        count = cls.count_key()

        return datas, count