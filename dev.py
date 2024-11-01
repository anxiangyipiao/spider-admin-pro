# -*- coding: utf-8 -*-
"""
@File    : dev.py
@Date    : 2023-02-21
# 预留给windows用户开发使用
"""

from spider_admin_pro import app
# from spider_admin_pro.service.log_service import LogCollectionService


if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=18000)

    # print(LogCollectionService.get_today_info())
    