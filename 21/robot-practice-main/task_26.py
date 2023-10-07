#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    pass


run_tasks()