# -*- coding: utf-8 -*-

"""
spider运行结果数据收集模块
"""
from pprint import pprint

from flask import request

# from spider_admin_pro.flask_app import BlueprintAppApi
from spider_admin_pro.model.stats_collection_model import StatsCollectionModel
from spider_admin_pro.service import schedule_history_service
from spider_admin_pro.service.stats_collection_service import StatsCollectionService
from spider_admin_pro.service.log_service import LogCollectionService
from spider_admin_pro.utils.flask_ext.flask_app import BlueprintAppApi

stats_collection_api = BlueprintAppApi("stats_collection", __name__)


@stats_collection_api.post('/addItem')
def add_item():
    # pprint(request.json)

    spider_job_id = request.json['job_id']
    project = request.json['project']
    spider = request.json['spider']
    item_scraped_count = request.json['item_scraped_count']
    item_dropped_count = request.json['item_dropped_count']
    start_time = request.json['start_time']
    finish_time = request.json['finish_time']
    duration = request.json['duration']
    finish_reason = request.json['finish_reason']
    log_error_count = request.json['log_error_count']

    # 查询 scrapyd_server_id
    schedule_history_row = schedule_history_service.get_schedule_history_service_by_job_id(spider_job_id=spider_job_id)
    if schedule_history_row:
        scrapyd_server_id = schedule_history_row.scrapyd_server_id
    else:
        scrapyd_server_id = 0

    StatsCollectionModel.create(
        spider_job_id=spider_job_id,
        scrapyd_server_id=scrapyd_server_id,
        project=project,
        spider=spider,
        item_scraped_count=item_scraped_count,
        item_dropped_count=item_dropped_count,
        start_time=start_time,
        finish_time=finish_time,
        finish_reason=finish_reason,
        log_error_count=log_error_count,
        duration=duration
    )


@stats_collection_api.post('/listItem')
def list_item():
    page = request.json.get("page", 1)
    size = request.json.get("size", 20)
    project = request.json.get("project")
    spider = request.json.get("spider")

    order_prop = request.json.get("order_prop")
    order_type = request.json.get("order_type")  # descending, ascending
    scrapyd_server_id = request.json.get("scrapydServerId")

    return {
        'list': StatsCollectionService.list(
            page=page, size=size,
            scrapyd_server_id=scrapyd_server_id,
            project=project, spider=spider,
            order_prop=order_prop, order_type=order_type
        ),
        'total': StatsCollectionService.count(project=project, spider=spider)
    }


@stats_collection_api.post('/delete')
def delete():
    project = request.json.get("project")
    spider = request.json.get("spider")
    scrapyd_server_id = request.json.get("scrapydServerId")

    StatsCollectionService.delete(
        project=project,
        scrapyd_server_id=scrapyd_server_id,
        spider=spider
    )



@stats_collection_api.post('/getTaskLog')
def getTaskLog():
    
    page = request.json.get("page", 1)
    size = request.json.get("size", 20)
    
    datas,count = LogCollectionService.get_data(page=page,PAGE_SIZE=size)

    return {
        'list': datas,
        'total': count
    }