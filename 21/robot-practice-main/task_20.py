#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    pass


run_tasks()