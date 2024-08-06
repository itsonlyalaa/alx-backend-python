#!/usr/bin/env python3
"""takes an integer max_delay"""

import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """ Waits for random delay and then returns asyncio.Task"""
    return asyncio.create_task(wait_random(max_delay))
