# -*- coding: utf-8 -*-
# @Author: qinyue
# @Time: 2023/8/9 10:30
# @File: conftest.py
from typing import List


def pytest_collection_modifyitems(items: List["Item"]):
    # item表示每个测试用例，解决用例名称中文显示问题
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")