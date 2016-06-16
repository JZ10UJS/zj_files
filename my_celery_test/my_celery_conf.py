#!/usr/bin/python
# coding: utf-8

from celery import Celery

app = Celery('my_celery_conf', broker='redis://localhost:6379',
             include=['celery_add'])

