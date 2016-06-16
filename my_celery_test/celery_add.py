#!/usr/bin/python
# coding: utf-8

"""
这种需要
celery worker -A my_celery_conf -l info 后
在cmd中，进入python ,然后
from celery_add import add
add.delay(3,4)
才好使
"""

from .my_celery_conf import app


@app.task
def add(x, y):
    return x + y


def main():
    for i in range(10):
        add.delay(i, i)


if __name__ == '__main__':
    main()
